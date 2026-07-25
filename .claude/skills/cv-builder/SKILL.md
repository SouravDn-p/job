---
name: cv-builder
description: Generate an ATS-optimised CV tailored to a specific job description from PROFILE.md, then record the application in jobs/LOG.md. Use when the user supplies a job description, asks for a CV or résumé for a role, or wants to apply somewhere. Also use to update the status of an existing logged application.
---

# CV Builder

Generate a CV tailored to one job description, then log the application so it can be retrieved months later.

You are acting as a **senior HR manager and professional CV writer** who knows how automated applicant-tracking systems parse and rank CVs, and what a hiring manager decides in the thirty seconds after that.

**Reference:** `references/ats-and-hiring-manager.md` holds the research this procedure is built on, with sources. Read it when a decision isn't covered below, or when the user asks *why* a rule exists. Everything in this file is a distillation of it.

---

## The three gates — design for all three

A CV is read three times, by three different readers who want different things. Optimising for one at the expense of another is the usual way a CV fails.

| Gate | Reader | Time | Wants | Fails when |
|---|---|---|---|---|
| **1** | ATS parser | ms | Machine-readable structure | Data lands in the wrong field or vanishes |
| **2** | Keyword search / AI match score / recruiter skim | **7.4 s** | Literal relevance in the **top third of page 1** | Ranked below the batch they have time for |
| **3** | Hiring manager | 30 s → 4 min | Evidence of impact, scope, trajectory | Reads as a task list; nothing to evaluate |

Gate 1 is formatting. Gate 2 is vocabulary and placement. **Gate 3 is content — and it's the one that gets the interview.** Do not spend the whole build on gate 1.

Two things that are true and worth saying out loud when relevant:
- **ATS does not auto-reject on formatting.** 92% of surveyed recruiters confirmed this. The only true auto-reject is the **knockout questions** in the application form (work authorisation, location, degree, certification) — 100% of recruiters use those. Formatting rules below are cheap hygiene, not survival.
- **Volume beats optimisation.** Roles draw 400–2,000 applicants; 52% of recruiters review in order received and start interviewing before reaching the back of the pile. Tell the user to apply early.

---

## Step 0 — Get the job description

If the user hasn't supplied one, ask for it before doing anything else. You need the actual posting text, not a job title. If they only have a URL, ask them to paste the text — postings are often behind auth and will be deleted later anyway.

Also ask (one message, not one at a time) for anything missing that changes the output:
- Company name and exact role title as posted
- Where they found it (LinkedIn / company site / Fiverr / referral / recruiter)
- Location and work type (on-site Dhaka / remote / hybrid / relocation)
- Deadline, if any, and **how long the posting has been up** — it changes the urgency advice

## Step 1 — Read the profile in full

Read `PROFILE.md` completely. It fits in a single read. **Do not work from a partial read or from memory of a previous session.** Everything you write must trace back to a line in it.

## Step 1b — Check the assets folder

List `Assets/` and its subfolders every run — contents change, so never work from a remembered inventory.

- `Assets/CV Templates/` — read the template images and the existing resume PDF for layout, section order, and phrasing precedent. **Layout reference only:** no bullet, title, or claim moves from a template or the old PDF into the new CV unless it also traces to `PROFILE.md`. If the PDF contradicts `PROFILE.md`, `PROFILE.md` wins and you tell the user. If a template uses two columns, skill bars, or icons, **do not copy those** — they break gate 1 and cost you at gate 2.
- `Assets/Profile Pictures/` — include a headshot only when the target market or JD expects one (DE/AT/CH, some Asian markets); omit for US/UK/CA. Reference it by relative path.

If something expected is missing — no headshot, no matching template — say so and carry on. Never substitute or generate a placeholder.

## Step 2 — Analyse the job description

Extract, and note explicitly:

- **Knockouts** — anything that will be a yes/no gate on the form: work authorisation, location/timezone, degree, years of experience, a named certification. Flag these to the user immediately; a knockout he can't clear is worth knowing *before* the CV is built.
- **Hard requirements** — the must-haves, usually under "Requirements" or "You have"
- **Nice-to-haves** — "Bonus", "Preferred", "It's a plus"
- **The exact vocabulary used.** Record the literal phrases. Mirror them: if the JD says "REST APIs", write "REST APIs". Semantic/LLM matching in 2026 means near-synonyms usually still match, so **do not mangle a sentence to force a literal string in** — but where the phrasing is equally natural, use theirs. It costs nothing, it survives the keyword search that 99.7% of recruiters still run, and it reads as deliberate to a human.
- **Seniority signal** — junior / mid / senior, team size, ownership expectations
- **The domain** — fintech, health, e-commerce, AI, marketplace — so you can lead with a matching project
- **Gaps** — requirements the profile genuinely doesn't cover

Cross-reference the JD's vocabulary against `PROFILE.md` §16 (Keyword Bank). Every keyword there is legitimately claimable. **Anything the JD asks for that is not in §16 or elsewhere in the profile does not go on the CV.**

## Step 3 — Assemble

### Order and placement

Reverse-chronological throughout — oldest-first was explicitly criticised by recruiters. Section order by default: **Contact → Summary → Skills → Experience → Projects → Education → Certifications**, adjusted so whatever the JD cares most about sits highest.

**The top third of page 1 carries the pitch.** Recruiters scan in an F-pattern: the top third thoroughly, then down the left edge, rarely to the right. Name, a summary aligned to the target role, and the JD's top skills all live there. If a reader must reach page 2 to learn he's a backend engineer, the CV has failed.

**Front-load every bullet.** The left edge gets read; the right does not. Outcome and technology at the start, qualifiers at the end.

### Content

**Summary** — pick the closest of the six pre-written variants in `PROFILE.md` §3 and adapt it to the JD's language. Do not write one from scratch; they are already calibrated.

**Skills section** — build from §15, ordered so the JD's stated requirements appear first. Omit categories the JD doesn't care about; a Django JD does not need the electronics section. Plain comma-separated text under grouped labels — **never skill bars, ratings, or tables.** The skills section exists for keyword search; the *evidence* lives in the bullets.

**Experience bullets** — pull from the bullet banks in §4 and re-order so the most JD-relevant bullet leads. Every bullet should read as:

> **Accomplished [X], as measured by [Y], by doing [Z]** — outcome, then the number that proves it, then the mechanism.

Z is where the JD's technology keywords belong; that's what an LLM screener rewards and what a hiring manager believes. **Do not weaken bullets into task lists** ("Responsible for…") — the banks are written as quantified achievements on purpose.

**When there is no honest number, do not invent one** — substitute concrete scope: what was built, what it handled, who used it, what it replaced, what it integrated with. A scoped bullet with no metric is evaluable; a fabricated metric is not recoverable.

**Never let a metric outrun its scope.** Hiring managers are actively sceptical of numbers disproportionate to the work described, and a number that doesn't add up makes them distrust the whole document — and it *will* be probed in the interview.

**Show trajectory.** Promotion from Junior Python Developer to Senior Python Executive within eleven months is one of the strongest signals in the profile. State it explicitly; don't let it be inferred from two title lines.

**Projects** — select 3–5 using each project's *"Best for JDs about…"* tag. Prefer recent and substantial over old and simple; recent work weighs most because the stack moves. Client work (§7) generally outranks personal work (§9) unless the JD is for a domain a personal project matches better. For anything under §7, obey the NDA rules in `CLAUDE.md`: product names only, never internal folder names, never client source.

**Education / certifications** — §5 and §6. If the CGPA appears, flag to the user that it is unverified (§17.1).

**Keyword discipline** — any given keyword **2–3 times maximum**, in different sections, each time inside a genuine readable sentence. Stuffing reads as copying to both the AI and the human; 76% of recruiters specifically value *natural* usage. **Never hide text** in white or 1pt font, and never embed instructions aimed at an LLM screener — recruiters find it the moment they paste into a notes field, and it gets candidates blacklisted across a network.

### Length

**Content decides page count; page count never decides content.** Every line earns its place — but do not amputate strong material to hit a target, and never pad to fill.

| Situation | Target |
|---|---|
| Thin JD-relevant material | 1 page |
| Substantial, JD-relevant material to show | **2 pages — the normal case for this profile** |
| Executive / academic / government application | 3+, by convention |
| Non-executive engineering role | **never 3 pages** |

The one-page rule is not supported by evidence: in a blind simulation of 482 recruiters, two-page CVs were preferred **1.4× at entry level and 2.6× at mid-level**, scored 21% higher on conveying credentials, and got 4+ minutes of attention versus under 2.5. But 64% of recruiters cap it at two, and a half-empty page 2 reads as padding.

**Page 2 is for the hiring manager at gate 3, never the recruiter at gate 2.** Nothing decision-critical goes on it.

## Step 4 — Self-check before writing

Three passes, one per gate. Verify every line.

**Gate 1 — will it parse?**
- [ ] Single column; no layout tables, no text boxes
- [ ] Contact details are plain text at the top of page 1, **not** in a header/footer
- [ ] Standard section headings (`Professional Summary`, `Work Experience`, `Skills`, `Projects`, `Education`, `Certifications`) — no creative names
- [ ] All dates as `Mon YYYY – Mon YYYY` (e.g. `Aug 2025 – Present`). Not numeric, not `January 2023 to March 2025`, not seasons or quarters
- [ ] Standard font, body 10–12pt; bullets are `•` or `-` only
- [ ] No information carried by an icon, graphic, or skill bar
- [ ] Exported PDF has selectable text (verify after rendering — see Step 5b)

**Gate 2 — will it survive 7.4 seconds?**
- [ ] Target role is obvious from the top third of page 1 alone
- [ ] The JD's top 5 hard requirements each appear, in the JD's own wording, where genuinely true
- [ ] Job titles bold and scannable down the left edge
- [ ] Every bullet front-loaded — outcome first, not preamble
- [ ] No paragraph blocks in the experience section
- [ ] No keyword appears more than 2–3 times; no hidden text anywhere

**Gate 3 — will a hiring manager act on it?**
- [ ] Every claim traces to a line in `PROFILE.md` — nothing inferred, nothing rounded up
- [ ] Every bullet has an outcome or a concrete scope, not just a duty
- [ ] No metric outruns the scope of the work it describes
- [ ] Progression is visible and stated, not left to be inferred
- [ ] Framing is mid-level engineer with end-to-end ownership, not a junior taking tickets
- [ ] Reverse-chronological throughout
- [ ] No internal client folder names anywhere
- [ ] No credentials, server IPs, keys, or passwords
- [ ] No dead links (`amjh.space`) — see `CLAUDE.md` hard rule 6
- [ ] Contact details correct (§1)

## Step 5 — Write the application folder

Create `jobs/YY-MM-DD_<company-slug>_<Role-Name>/` using **today's date** (check it — do not assume). **The date comes first** so the folder list sorts chronologically.

Write three files:

**`cv.html`** — the finished CV, in **HTML** (rendered to PDF in step 5b). This is what gets sent, so it must be complete and standalone: inline `<style>`, `@page { size: A4 }`, single column, semantic `<h1>/<h2>/<section>/<ul>`, DOM order matching reading order, no layout tables, no text baked into images, nothing in a running header or footer. Copy any referenced image into the folder and link it by relative path.

**Verify the page count by actually rendering it** — never estimate. Headless Edge works:
`& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="out.pdf" "file:///C:/.../cv.html"`
then count `/Type /Page` or use `pymupdf`.

**The fill test, applied to the rendered PDF and never to an estimate:**
- Every page before the last: **≥ 90% full**
- The last page: **≥ 75% full**. A page 2 that's 40% full is worse than a tight single page — cut to one page.

Three pagination traps, all learned the hard way:
- `break-inside: avoid` on a tall entry (an 8-bullet job, a 3-bullet degree) strands 10–15% of *every* page and silently adds a sheet. Let long entries flow; use `orphans: 2; widows: 2` instead, and `break-after: avoid` on the title row so a heading never ends a page.
- **`break-after: avoid` on the title row alone is not enough.** If a meta or stack line sits between the title and the bullets, the renderer satisfies the rule by breaking *after the meta line* — leaving the job title and its location stranded at the foot of a page with the content overleaf. Put `break-after: avoid` on the meta and stack lines too, so the whole title block travels with its content.
- If it still overflows, **cut copy before shrinking type**. 8.8pt Arial is the sensible floor.

**Total height fitting inside two pages does not mean it paginates to two pages.** Block-break slack means content measuring 1.99 pages routinely renders as three. Leave real headroom — aim for ~1.90 pages of raw content — rather than trimming to a hairline and re-rendering hopefully.

Once the status is `Applied`, treat the file as immutable: a revised CV for the same company means a new dated folder, not an edit. **Exactly one CV file per folder** — never leave a `cv.md` next to a `cv.html`.

**`job-description.md`** — the JD archived verbatim, with a small header:
```markdown
# <Role> — <Company>
**Source:** <where found> · **Archived:** <date> · **Deadline:** <if any>
**URL:** <if supplied>

---
<the posting, unedited>
```

**`notes.md`** — use this structure:
```markdown
# <Company> — <Role>

## Application
| Field | Value |
|---|---|
| Applied | YYYY-MM-DD |
| Source | |
| Location / type | |
| Reference / application ID | |
| Contact | |
| Salary discussed | |

## CV decisions
- **Summary variant used:** §3.x — <which and why>
- **Projects featured:** <list, and why these>
- **Keywords targeted:** <literal phrases lifted from the JD>
- **Deliberately omitted:** <what was left out and why — matters if they ask>
- **Knockouts:** <the form's yes/no gates and how they were answered>
- **Weak spots:** <JD requirements not fully covered — prepare answers for these>

## Status timeline
- YYYY-MM-DD — Applied

## Interview prep
<filled in later — questions asked, people met, follow-ups owed>
```

## Step 5b — Export the PDF

Render `cv.html` with the workspace tool. Use its own venv interpreter; **never system Python, and never pip-install anything**:

```
tools/html_2_pdf/venv/Scripts/python.exe tools/html_2_pdf/html_to_pdf.py jobs/<folder> --no-input
```

It derives the recruiter-facing filename from `PROFILE.md` and the folder name (`Abdullah_Md_Jahid_Hassan_CV_<Role>.pdf`) and writes it into the application folder. Add `--page-size letter` for US applications. If the PDF already exists it will refuse rather than overwrite — that is deliberate for a CV that has been sent; only pass `--force` when the user has asked for a revision. Full options: `tools/html_2_pdf/README.md`.

**Then verify the text layer and the fill, by measuring — never by eye.** A PDF whose text can't be selected is invisible to every parser.

`PyMuPDF` (`import fitz`) is available in **system** Python on this machine. Use it for read-only verification only — the "venv, never system Python" rule governs *running the exporter*, not inspecting its output, and nothing gets installed:

```python
import fitz
doc = fitz.open(pdf_path)
M = 10/25.4*72                      # the 10mm @page margin, in points
for i, page in enumerate(doc):
    blocks = [b for b in page.get_text("blocks") if b[4].strip()]
    bottom = max(b[3] for b in blocks)
    fill = (bottom - M) / (page.rect.height - 2*M) * 100
```

Check all of:
- **Page count** and the **fill test** (≥90% on every page but the last, ≥75% on the last)
- **Required strings** extract as real text — name, current job title, email, every section heading, and the JD's top keywords
- **Forbidden strings** are absent — client internal folder names, `amjh.space`, `pythonanywhere`, unverified figures, anything the JD asked for that the profile can't support
- **Every date** extracts in `Mon YYYY – Mon YYYY` form, and no date uses the word "to"

Do not naively pull `(...)` strings out of the raw PDF — Chrome embeds subset fonts, so those bytes are glyph codes, not text. It looks like total extraction failure when the text layer is actually fine.

**Render the pages to images and look at them.** `page.get_pixmap(dpi=110).save(...)` then read the image. This is how stranded headings and bad breaks get caught; no measurement finds them.

## Step 6 — Log it

Prepend a row to the table in `jobs/LOG.md` (newest first, renumber so #1 is newest):

```
| 1 | 2026-07-25 | Acme Corp | Senior Backend Engineer | Remote (EU) | LinkedIn | Applied | 2026-07-25 | [folder](26-07-25_acme-corp_Senior-Backend-Engineer/) |
```

If the CV is generated but not yet submitted, use `Draft` and leave the `Applied` date blank until the user confirms submission.

Then **recompute the counts in the header table** at the top of `LOG.md`.

Remove the placeholder `*No applications logged yet.*` row the first time a real row is added.

## Step 7 — Report back

Tell the user, briefly:
- Where the CV was written, and the **verified** page count and text-layer check
- Which summary variant and which projects you chose, and why
- Which assets you used — which template informed the layout, whether a photo was included and why
- **Which JD requirements the profile does not cover** — the most useful thing you can say, because it's what he'll be asked about
- **Any knockout question that looks risky** (authorisation, location, degree, years) — before he submits, not after
- **Apply early.** If the posting is fresh, say so plainly; review happens in order received and the pile is 400+ deep
- Anything needing verification before sending (CGPA, unconfirmed product names)

---

## Updating a status later

When the user says anything like *"got a call from Acme"*, *"rejected by X"*, *"interview Thursday"*:

1. Find the application folder (grep `jobs/LOG.md` for the company).
2. Update the `Status` and `Updated` columns in `LOG.md`.
3. Append a dated line to the `## Status timeline` in that folder's `notes.md`.
4. Recompute the header counts in `LOG.md`.

Keep both in sync — the log is the index, the notes are the record.

## Interview retrieval

When asked *"what did I send to X?"* or *"prep me for the X interview"*: read that folder's `notes.md` first (it holds the story that was told), then `cv.html`, then `job-description.md`. Lead the answer with the projects featured and the weak spots recorded — those are what the interview will probe. Then work through every quantified bullet on the CV and check he can defend the number; hiring managers probe metrics that look large relative to scope.
