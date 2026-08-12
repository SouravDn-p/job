#!/usr/bin/env python3
"""Convert a CV written as HTML into a print-ready, properly-named PDF.

Rendering is done by headless Chrome (or Edge / Chromium / Brave — whichever is
found first). No pip packages are required: the browser is already on this
machine, and it is the highest-fidelity HTML renderer available, so the PDF
looks exactly like the page does in a browser's print preview.

The output filename is what a recruiter sees in their inbox, so it defaults to
the candidate's full name rather than "cv.pdf":

    Abdullah_Md_Jahid_Hassan_CV_Trainee_Software_Engineer.pdf

The role is derived from the application folder name, which already follows the
`YY-MM-DD_<company-slug>_<Role-Name>` convention from CLAUDE.md.

Usage
-----
Always run it with this tool's own interpreter — never system Python:

    PY=tools/html_2_pdf/venv/Scripts/python.exe          # Windows
    PY=tools/html_2_pdf/venv/bin/python                  # macOS / Linux

Run it bare and it asks for what it needs — the HTML path, then the PDF name
(optional: press Enter and it names the file for you):

    $PY tools/html_2_pdf/html_to_pdf.py

Or pass everything up front, which is how a script or the cv-builder skill
should call it:

    $PY tools/html_2_pdf/html_to_pdf.py jobs/Applied/26-07-25_well-dev_Trainee-Software-Engineer
    $PY tools/html_2_pdf/html_to_pdf.py cv.html --name "Abdullah Hassan CV.pdf"
    $PY tools/html_2_pdf/html_to_pdf.py cv.html --role "Backend Engineer" --with-company
    $PY tools/html_2_pdf/html_to_pdf.py cv.html --out "~/Desktop/Custom Name.pdf"
    $PY tools/html_2_pdf/html_to_pdf.py cv.html --page-size letter --margin 15mm --open

The venv deliberately holds no third-party packages: rendering is done by the
Chrome/Edge install already on the machine, and everything else is stdlib.

Exit codes: 0 success, 1 usage/input error, 2 no browser found, 3 render failed.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NoReturn

FALLBACK_CANDIDATE_NAME = "Abdullah Md Jahid Hassan"


def find_profile() -> Path | None:
    """Walk up from this file to the workspace root that holds PROFILE.md."""
    for directory in Path(__file__).resolve().parents:
        candidate = directory / "PROFILE.md"
        if candidate.is_file():
            return candidate
    return None


PROFILE = find_profile()

PAGE_SIZES = {"a4": "A4", "letter": "Letter", "legal": "Legal", "a5": "A5"}

# Folder convention from CLAUDE.md: 26-07-25_well-dev_Trainee-Software-Engineer
JOB_FOLDER_RE = re.compile(r"^\d{2}-\d{2}-\d{2}_(?P<company>[^_]+)_(?P<role>.+)$")

BROWSER_ENV_VAR = "CV_PDF_BROWSER"

# Chrome first (most predictable print pipeline), then Edge — always present on
# Windows 11 — then the other Chromium forks.
BROWSER_EXE_NAMES = [
    "chrome", "chrome.exe",
    "msedge", "msedge.exe",
    "chromium", "chromium-browser",
    "brave", "brave.exe",
    "google-chrome", "google-chrome-stable",  # Linux, if this ever runs there
]

BROWSER_KNOWN_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #

def find_browser(explicit: str | None = None) -> Path:
    """Locate a Chromium-family browser, or exit with an actionable message."""
    if explicit:
        path = Path(os.path.expandvars(explicit)).expanduser()
        if not path.is_file():
            fail(f"--browser path does not exist: {path}", code=2)
        return path

    env_value = os.environ.get(BROWSER_ENV_VAR)
    if env_value:
        path = Path(os.path.expandvars(env_value)).expanduser()
        if path.is_file():
            return path
        fail(f"${BROWSER_ENV_VAR} points at a missing file: {path}", code=2)

    for name in BROWSER_EXE_NAMES:
        found = shutil.which(name)
        if found:
            return Path(found)

    for raw in BROWSER_KNOWN_PATHS:
        path = Path(os.path.expandvars(raw))
        if path.is_file():
            return path

    fail(
        "No Chrome/Edge/Chromium installation found.\n"
        f"  Set {BROWSER_ENV_VAR} to the browser executable, or pass --browser <path>.",
        code=2,
    )


def ask(question: str, default: str = "") -> str:
    """Prompt on the terminal; blank input returns the default.

    EOFError is left to propagate: a caller that can carry on with its default
    catches it, while one that genuinely needs an answer must not spin.
    """
    suffix = f" [{default}]" if default else ""
    answer = input(f"{question}{suffix}: ").strip()
    # Drag-and-drop and "Copy as path" both hand over a quoted string.
    answer = answer.strip('"').strip("'").strip()
    return answer or default


def ask_optional(question: str, default: str = "") -> str:
    """As ask(), but a closed stdin silently accepts the default."""
    try:
        return ask(question, default)
    except EOFError:
        return default


def prompt_for_source() -> str:
    """Ask for the HTML path until something usable is given."""
    print("HTML → PDF · CV export")
    while True:
        try:
            raw = ask("Path to the CV HTML file (or its application folder)")
        except EOFError:
            fail("no input received — stdin closed before a path was given")
        if raw:
            return raw
        print("  A path is required. Ctrl+C to quit.")


def resolve_source(raw: str) -> Path:
    """Accept an .html file, or an application folder containing one."""
    src = Path(raw).expanduser()
    if not src.is_absolute():
        src = (Path.cwd() / src).resolve()

    if src.is_dir():
        preferred = src / "cv.html"
        if preferred.is_file():
            return preferred
        candidates = sorted(
            p for p in src.glob("*.html")
            # Ignore archived job postings and our own build leftovers.
            if not p.name.startswith(".") and "job" not in p.stem.lower()
        )
        if len(candidates) == 1:
            return candidates[0]
        if not candidates:
            fail(f"No CV HTML found in {src}\n  Expected {src / 'cv.html'}")
        listing = "\n".join(f"    {p.name}" for p in candidates)
        fail(f"{src} holds several HTML files — name one explicitly:\n{listing}")

    if not src.is_file():
        fail(f"Input not found: {src}")
    if src.suffix.lower() not in {".html", ".htm"}:
        fail(f"Expected an .html file, got {src.suffix or 'no extension'}: {src.name}")
    return src


def candidate_name() -> str:
    """Read the full name out of PROFILE.md §1 so it is never hardcoded twice."""
    if PROFILE is None:
        return FALLBACK_CANDIDATE_NAME
    try:
        text = PROFILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return FALLBACK_CANDIDATE_NAME
    match = re.search(r"\|\s*\*{0,2}Full name\*{0,2}\s*\|\s*([^|\n]+?)\s*\|", text, re.I)
    if match:
        return match.group(1).strip()
    return FALLBACK_CANDIDATE_NAME


# --------------------------------------------------------------------------- #
# Naming
# --------------------------------------------------------------------------- #

ILLEGAL_FILENAME_CHARS = r'<>:"/\|?*'
# Windows refuses these as filenames whatever the extension.
RESERVED_FILENAMES = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)),
                      *(f"LPT{i}" for i in range(1, 10))}


def clean_filename(name: str) -> str:
    """Make a user-typed CV name safe to write, keeping their spacing intact."""
    name = name.strip().strip('"').strip("'")
    # Path separators become dashes, so a typed name can never escape the folder.
    name = "".join("-" if ch in ILLEGAL_FILENAME_CHARS or ord(ch) < 32 else ch
                   for ch in name)
    name = name.strip().rstrip(" .")  # Windows rejects trailing dots and spaces
    if not name:
        return ""
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    if name.rsplit(".", 1)[0].upper() in RESERVED_FILENAMES:
        name = f"CV_{name}"
    return name


def to_filename_part(text: str) -> str:
    """'Trainee-Software Engineer (Python)' -> 'Trainee_Software_Engineer_Python'."""
    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", text)
    return cleaned.strip("_")


def derive_output_name(src: Path, role: str | None, company: str | None,
                       with_company: bool) -> str:
    """Build the recruiter-facing filename."""
    folder_role, folder_company = None, None
    match = JOB_FOLDER_RE.match(src.parent.name)
    if match:
        folder_role = match.group("role").replace("-", " ")
        folder_company = match.group("company").replace("-", " ")

    role = role or folder_role
    company = company or folder_company

    parts = [to_filename_part(candidate_name()), "CV"]
    if role:
        parts.append(to_filename_part(role))
    if with_company and company:
        parts.append(to_filename_part(company))

    # Nothing to tailor with (loose HTML file, no role given): plain CV name.
    return "_".join(p for p in parts if p) + ".pdf"


# --------------------------------------------------------------------------- #
# Page setup
# --------------------------------------------------------------------------- #

HAS_PAGE_RULE_RE = re.compile(r"@page\b", re.I)


def build_page_style(page_size: str, margin: str) -> str:
    return (
        "<style id=\"cv-pdf-page-setup\">"
        f"@page {{ size: {page_size}; margin: {margin}; }}"
        "</style>"
    )


CLOSING_TAG_RE = re.compile(r"</\s*(body|html)\s*>", re.I)


def inject_page_style(html: str, style: str) -> str:
    """Append the @page rule last so it wins the cascade over the document's own.

    Matched on the original string — indexing `html` with offsets taken from
    `html.lower()` would misplace the tag, because lowercasing is not
    length-preserving for every character ('İ'.lower() is two code points).
    """
    matches = list(CLOSING_TAG_RE.finditer(html))
    if not matches:
        return html + "\n" + style
    bodies = [m for m in matches if m.group(1).lower() == "body"]
    anchor = (bodies or matches)[-1].start()
    return html[:anchor] + style + "\n" + html[anchor:]


def prepare_html(src: Path, page_size: str, margin: str, forced: bool) -> tuple[Path, bool]:
    """Return the file to render and whether it is a temp file we must delete.

    Chrome's --print-to-pdf has no paper-size flag: page geometry comes from the
    CSS @page rule. If the HTML already declares one, we leave the template's
    design alone unless the user explicitly asked for different geometry.

    The temp copy is written *beside* the source so relative paths — the profile
    picture in Assets/, local stylesheets — still resolve.
    """
    try:
        html = src.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        fail(f"could not read {src.name}: {exc}")

    if HAS_PAGE_RULE_RE.search(html) and not forced:
        return src, False

    temp = src.with_name(f".{src.stem}.pdfbuild{src.suffix}")
    try:
        temp.write_text(inject_page_style(html, build_page_style(page_size, margin)),
                        encoding="utf-8")
    except OSError as exc:
        # The copy has to live beside the source for relative assets to resolve,
        # so a read-only folder cannot be worked around silently.
        fail(f"could not write the page-setup copy next to {src.name}: {exc}\n"
             f"  Add an @page rule to the HTML, or make {src.parent} writable.")
    return temp, True


# --------------------------------------------------------------------------- #
# Render
# --------------------------------------------------------------------------- #

def chrome_command(browser: Path, profile_dir: str, source: Path, target: Path,
                   headless_flag: str, wait_ms: int) -> list[str]:
    return [
        str(browser),
        headless_flag,
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--disable-sync",
        "--disable-background-networking",
        # A throwaway profile, so an already-running Chrome cannot hijack this run.
        f"--user-data-dir={profile_dir}",
        # Let webfonts, images and any layout JS settle before the snapshot.
        f"--virtual-time-budget={wait_ms}",
        "--run-all-compositor-stages-before-draw",
        # Drop the browser's date/URL header and footer. Chrome ignores whichever
        # of these two spellings its version does not know.
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={target}",
        source.as_uri(),  # percent-encodes the spaces in "My Files"
    ]


def is_pdf(path: Path) -> bool:
    """A real PDF, not a zero-byte stub or an error page."""
    try:
        if path.stat().st_size == 0:
            return False
        with path.open("rb") as handle:
            return handle.read(5) == b"%PDF-"
    except OSError:
        return False


def render(browser: Path, source: Path, target: Path, wait_ms: int,
           timeout: int) -> None:
    """Render to a scratch file, then move it into place only once it is valid.

    Writing straight to `target` would be unsafe twice over: a failed render
    would leave a previous run's PDF sitting there and be mistaken for success,
    and a CV that has already been sent would be destroyed by a render that
    never completed. The move is atomic — same directory, so os.replace().
    """
    handle_fd, scratch_name = tempfile.mkstemp(prefix=".cv-pdf-", suffix=".pdf",
                                               dir=target.parent)
    os.close(handle_fd)
    scratch = Path(scratch_name)

    last_error = "no output"
    try:
        # "--headless=new" on Chrome 112+; plain "--headless" for older builds.
        for headless_flag in ("--headless=new", "--headless"):
            # Not TemporaryDirectory(): on Windows, Chrome's crashpad helper can
            # still hold the profile open as we exit, and the automatic cleanup
            # would then raise PermissionError *after* a successful render.
            profile_dir = tempfile.mkdtemp(prefix="cv-pdf-profile-")
            try:
                cmd = chrome_command(browser, profile_dir, source, scratch,
                                     headless_flag, wait_ms)
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True,
                                            timeout=timeout)
                except subprocess.TimeoutExpired:
                    last_error = f"browser did not finish within {timeout}s"
                    continue
                except OSError as exc:
                    fail(f"could not start {browser}: {exc}", code=2)
            finally:
                shutil.rmtree(profile_dir, ignore_errors=True)

            if is_pdf(scratch):
                try:
                    os.replace(scratch, target)
                except OSError as exc:
                    # Windows locks a file that a PDF viewer has open.
                    fail(f"rendered the PDF but could not save it over "
                         f"{target.name}: {exc}\n"
                         f"  Close the file if it is open in a PDF viewer.", code=3)
                return

            stderr = (result.stderr or result.stdout or "").strip()
            last_error = stderr.splitlines()[-1] if stderr else \
                f"browser exited {result.returncode} without writing a PDF"
    finally:
        scratch.unlink(missing_ok=True)

    fail(f"PDF render failed using {browser.name}: {last_error}", code=3)


def page_count(pdf: Path) -> int | None:
    """Best-effort page count for the summary line.

    Counts page objects directly; /Count is only a fallback because outline
    trees carry one too and would inflate the number.
    """
    try:
        blob = pdf.read_bytes()
    except OSError:
        return None
    pages = len(re.findall(rb"/Type\s*/Page(?![a-zA-Z])", blob))
    if pages:
        return pages
    counts = [int(m) for m in re.findall(rb"/Count\s+(\d+)", blob)]
    return max(counts) if counts else None


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def fail(message: str, code: int = 1) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(code)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="html_to_pdf.py",
        description="Render a CV written in HTML to a properly-named PDF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Naming: <Full_Name>_CV_<Role>[_<Company>].pdf — role and company "
               "are read from the YY-MM-DD_<company>_<Role> folder unless overridden.",
    )
    parser.add_argument("source", nargs="?",
                        help="cv.html, or an application folder containing one; "
                             "omit it and you will be asked for the path")
    parser.add_argument("-n", "--name",
                        help="PDF filename (optional — defaults to the derived name)")
    parser.add_argument("-o", "--out",
                        help="exact output path (overrides all naming rules)")
    parser.add_argument("--out-dir",
                        help="directory for the PDF (default: next to the HTML)")
    parser.add_argument("--role", help="role title, if not derivable from the folder")
    parser.add_argument("--company", help="company name, used with --with-company")
    parser.add_argument("--with-company", action="store_true",
                        help="append the company to the filename")
    parser.add_argument("--page-size", default="a4",
                        choices=sorted(PAGE_SIZES),
                        help="paper size when the HTML has no @page rule (default: a4)")
    parser.add_argument("--margin", default="12mm",
                        help="page margin, any CSS length (default: 12mm)")
    parser.add_argument("--force-page-setup", action="store_true",
                        help="apply --page-size/--margin even if the HTML sets @page")
    parser.add_argument("--wait", type=int, default=6000, metavar="MS",
                        help="time budget for fonts/images/JS (default: 6000)")
    parser.add_argument("--timeout", type=int, default=120, metavar="SEC",
                        help="hard limit on the browser process (default: 120)")
    parser.add_argument("--browser", help="path to a Chrome/Edge/Chromium binary")
    parser.add_argument("-f", "--force", action="store_true",
                        help="overwrite an existing PDF")
    parser.add_argument("--open", dest="open_after", action="store_true",
                        help="open the PDF when it is written")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="print only the output path")
    parser.add_argument("--no-input", action="store_true",
                        help="never prompt; fail instead (for scripted runs)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    # Prompting only happens when the tool is run bare on a terminal. Given a
    # source argument, or a pipe, it behaves as a plain non-interactive CLI.
    interactive = (
        args.source is None and not args.no_input and sys.stdin is not None
        and sys.stdin.isatty()
    )

    # Silently ignoring a flag the user meant to take effect is worse than
    # stopping: --out already fixes the whole path.
    if args.out and (args.out_dir or args.name):
        fail("--out sets the full path — drop --out-dir/--name, or drop --out.")
    if args.wait < 0:
        fail("--wait must be zero or more milliseconds")
    if args.timeout <= 0:
        fail("--timeout must be a positive number of seconds")

    raw_source = args.source
    if raw_source is None:
        if args.no_input or not interactive:
            fail("no HTML path given (and prompting is disabled)\n"
                 "  Pass the path as an argument, or run the tool without --no-input.")
        raw_source = prompt_for_source()

    source = resolve_source(raw_source)
    browser = find_browser(args.browser)

    if args.out:
        target = Path(os.path.expandvars(args.out)).expanduser()
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        if target.is_dir():
            fail(f"--out is a directory: {target}\n  Use --out-dir instead.")
    else:
        default_name = derive_output_name(source, args.role, args.company,
                                          args.with_company)
        name = clean_filename(args.name) if args.name else ""
        if not name and interactive:
            # Optional: Enter accepts the name derived from the folder.
            name = clean_filename(ask_optional("PDF name (Enter to accept)",
                                               default_name))
        out_dir = Path(args.out_dir).expanduser() if args.out_dir else source.parent
        target = (out_dir / (name or default_name)).resolve()

    # A CV that has already been sent should never be replaced silently.
    if target.exists() and not args.force:
        if interactive:
            if ask_optional(f"{target.name} already exists — overwrite? (y/N)",
                            "n").lower() not in {"y", "yes"}:
                print("Cancelled — nothing was written.")
                return 130
        else:
            fail(f"{target.name} already exists in {target.parent}\n"
                 f"  Pass --force to overwrite it.")

    try:
        target.parent.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        fail(f"cannot create the output folder {target.parent}: {exc}")

    render_source, is_temp = prepare_html(
        source, PAGE_SIZES[args.page_size], args.margin, args.force_page_setup
    )
    try:
        render(browser, render_source, target, args.wait, args.timeout)
    finally:
        if is_temp:
            render_source.unlink(missing_ok=True)

    if args.quiet:
        print(target)
    else:
        pages = page_count(target)
        size_kb = target.stat().st_size / 1024
        detail = f"{pages} page{'s' if pages != 1 else ''}, " if pages else ""
        print(f"Wrote {target}")
        print(f"  {detail}{size_kb:.0f} KB, rendered by {browser.name}")
        if is_temp:
            print(f"  page setup applied: {PAGE_SIZES[args.page_size]}, "
                  f"{args.margin} margins")

    if args.open_after:
        try:
            if sys.platform == "win32":
                os.startfile(target)  # noqa: S606 - intentional, user asked
            else:
                subprocess.run(["open" if sys.platform == "darwin" else "xdg-open",
                                str(target)], check=False)
        except OSError as exc:
            print(f"  (could not open the file: {exc})", file=sys.stderr)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        raise SystemExit(130)
