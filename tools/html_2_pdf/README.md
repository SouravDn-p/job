# html_2_pdf — CV HTML → PDF exporter

Turns a CV written as HTML into a print-ready PDF with a filename a recruiter can
file without renaming it.

Rendering is done by the **Chrome or Edge already installed on this machine**, in
headless mode. That is deliberate: it is the same engine that draws the browser's
print preview, so what you see in the browser is what lands in the PDF — and it
means **no third-party packages to install or keep updated**.

---

## Setup

The venv already exists at `tools/html_2_pdf/venv`. It holds nothing but `pip` —
the script is pure standard library. Nothing was, or should be, installed into
system Python.

If the venv ever needs rebuilding:

```powershell
python -m venv "tools/html_2_pdf/venv"
```

Always call the tool through that interpreter:

| Platform | Interpreter |
|---|---|
| Windows | `tools/html_2_pdf/venv/Scripts/python.exe` |
| macOS / Linux | `tools/html_2_pdf/venv/bin/python` |

---

## Use

**Interactive — just run it and answer two questions:**

```powershell
tools\html_2_pdf\venv\Scripts\python.exe tools\html_2_pdf\html_to_pdf.py
```

```
HTML → PDF · CV export
Path to the CV HTML file (or its application folder): C:\...\jobs\Applied\26-07-25_well-dev_Trainee-Software-Engineer
PDF name (Enter to accept) [Abdullah_Md_Jahid_Hassan_CV_Trainee_Software_Engineer.pdf]:
Wrote C:\...\Abdullah_Md_Jahid_Hassan_CV_Trainee_Software_Engineer.pdf
  2 pages, 61 KB, rendered by chrome.exe
```

The **name prompt is optional** — press Enter and the tool names the file itself.
A pasted path may keep its quotes; drag-and-drop from Explorer works too.

**Non-interactive**, for scripts and for the `cv-builder` skill:

```powershell
$PY = "tools\html_2_pdf\venv\Scripts\python.exe"

# point it at the application folder — it finds cv.html and derives the name
& $PY tools\html_2_pdf\html_to_pdf.py jobs\Applied\26-07-25_well-dev_Trainee-Software-Engineer

# explicit name
& $PY tools\html_2_pdf\html_to_pdf.py cv.html --name "Abdullah Hassan CV"

# US application: Letter paper, company in the filename
& $PY tools\html_2_pdf\html_to_pdf.py cv.html --page-size letter --with-company

# open it as soon as it is written
& $PY tools\html_2_pdf\html_to_pdf.py cv.html --open
```

---

## How the filename is chosen

First rule that applies wins:

1. `--out <path>` — used verbatim. It sets the whole path, so combining it with
   `--name` or `--out-dir` is rejected rather than silently ignored.
2. `--name <name>` — or whatever you type at the prompt. `.pdf` is appended if
   missing, and characters Windows forbids (`\ / : * ? " < > |`) become `-`.
3. **Derived** — from the full name in `PROFILE.md` §1 plus the role read out of
   the application folder, which already follows `YY-MM-DD_<company>_<Role>`:

   ```
   jobs/Applied/26-07-25_well-dev_Trainee-Software-Engineer/cv.html
     └─> Abdullah_Md_Jahid_Hassan_CV_Trainee_Software_Engineer.pdf
   ```

   `--with-company` appends the company; `--role` / `--company` override what the
   folder says, for an HTML file living somewhere else.

The PDF is written **next to the source HTML** unless `--out-dir` says otherwise —
so it lands in the application folder alongside `cv.md` and `notes.md`.

---

## Page geometry

Chrome's `--print-to-pdf` has no paper-size switch: page size and margins come
from the CSS `@page` rule.

- **If the HTML already sets `@page`**, the tool leaves it alone — a designed
  template keeps its own geometry.
- **If it does not**, the tool injects `@page { size: A4; margin: 12mm }`
  (change with `--page-size` / `--margin`).
- `--force-page-setup` overrides the template's own rule.

The injection is written to a temp file **beside the source**, so relative paths
— the profile picture from `Assets/`, a local stylesheet — still resolve. It is
deleted afterwards, including when the render fails.

---

## Options

| Flag | Purpose |
|---|---|
| `-n, --name` | PDF filename (optional; extension added for you) |
| `-o, --out` | exact output path, overriding every naming rule |
| `--out-dir` | write the PDF somewhere other than beside the HTML |
| `--role`, `--company` | supply what the folder name cannot |
| `--with-company` | append the company to the derived filename |
| `--page-size` | `a4` (default), `letter`, `legal`, `a5` |
| `--margin` | any CSS length, default `12mm` |
| `--force-page-setup` | apply size/margin even if the HTML sets `@page` |
| `--wait MS` | time budget for fonts, images and layout JS (default 6000) |
| `--timeout SEC` | hard limit on the browser process (default 120) |
| `--browser PATH` | use a specific Chrome/Edge/Chromium binary |
| `-f, --force` | overwrite an existing PDF without asking |
| `--open` | open the PDF once written |
| `-q, --quiet` | print only the output path |
| `--no-input` | never prompt — fail instead (for unattended runs) |

Exit codes: `0` success · `1` usage or input error · `2` no browser found ·
`3` render failed · `130` cancelled (overwrite declined, or Ctrl+C).

---

## Notes and gotchas

- **An existing PDF is never replaced silently.** Interactively you get a y/N
  prompt; non-interactively it fails and asks for `--force`. Once a CV has been
  sent, the file that was sent should stay exactly as it was.
- **The write is atomic.** Rendering goes to a scratch file next to the target
  and is moved into place only after the output is confirmed to be a real PDF.
  A failed or interrupted render therefore cannot leave a truncated CV, and
  cannot leave an older PDF behind while reporting success. If the target is
  locked — open in a PDF viewer — the tool says so and leaves the file alone.
- **Browser discovery order:** `--browser`, then `$CV_PDF_BROWSER`, then `PATH`,
  then the usual install locations — Chrome first, then Edge, then Chromium and
  Brave. Verified working on both Chrome and Edge on this machine.
- **The render uses a throwaway browser profile**, so it works while Chrome is
  already open and cannot touch your real profile.
- **The output is real text, not an image** — embedded subset fonts with
  `/ToUnicode` maps, which is what an ATS needs in order to parse the CV.
  Verified: text, including accented characters and the email address, extracts
  cleanly from the generated PDF.
- **Web fonts and remote images** need network access at render time. For a CV
  that must render identically forever, prefer system fonts or embed assets.
- Page breaks work as in the browser: `page-break-before: always` or
  `break-inside: avoid` on a block you do not want split across pages.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `No Chrome/Edge/Chromium installation found` | `--browser "C:\path\to\chrome.exe"`, or set `CV_PDF_BROWSER` |
| PDF is one page too long | tighten `--margin`, or add `break-inside: avoid` to the block that spills |
| Fonts or images missing | raise `--wait` (e.g. `--wait 12000`); check paths are relative to the HTML |
| Paper size ignored | the HTML has its own `@page` — add `--force-page-setup` |
| Header/footer with date and URL | already suppressed; if it reappears, the browser is very old — update it |
