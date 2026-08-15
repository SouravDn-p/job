---
name: cv-builder
description: Generate an ATS-optimised CV tailored to a specific job description from PROFILE.md, then record the job in jobs/jobs_log.csv under jobs/Findings/ or jobs/Applied/. Use when the user supplies a job description, asks for a CV or résumé for a role, wants to apply somewhere, or wants a found job logged. Also use to update the status of an existing logged job.
---

# CV Builder

Generate a CV tailored to one job description, then log the job so it can be retrieved months later.

You are acting as a **senior HR manager and professional CV writer** who knows how automated applicant-tracking systems parse and rank CVs, and what a hiring manager decides in the thirty seconds after that.

**Reference:** `references/ats-and-hiring-manager.md` holds the research this procedure is built on, with sources. Read it when a decision isn't covered below, or when the user asks *why* a rule exists. Everything in this file is a distillation of it.

**Folder conventions:** `jobs/README.md` is authoritative for the `jobs/` layout, the CSV columns and the status vocabulary. Read it before writing anything under `jobs/`.

---

## Where the work lands — read this first

```
jobs/
├── jobs_log.csv        THE log. One row per job, found or applied. There is no LOG.md.
├── Findings/           jobs found, not yet applied to     → status Found · Draft
└── Applied/            jobs actually applied to           → status Applied and beyond
```

- **One job = one folder**, named `YY-MM-DD_<company-slug>_<Role-Name>/`, date first.
- A folder **moves** `Findings/` → `Applied/` on submission. Move, never copy. **A job must never exist in both.** The folder name does not change — its date is the day the job was found.
- Every folder has a row in `jobs/jobs_log.csv`, and every row has a folder.

## The priority tiers — name one on every job

From `CLAUDE.md` § Job-search preferences. Fills the `priority_tier` CSV column and opens every `notes.md`.

| Tier | What |
|---|---|
| **1** | **Remote** — company in Bangladesh or anywhere globally. Both rank equally. The top priority. |
| **2** | **Government job in Bangladesh** in the same field or expertise (software / IT / ICT / CS), including semi-government and autonomous bodies. |
| **3** | **On-site in Bangladesh.** The fallback. |

Hybrid is tier 3 unless the on-site requirement is genuinely occasional — say which. Relocation abroad is not on the list; do not surface it unless asked. Tier never overrides fit: a tier 1 role he isn't qualified for still loses to a tier 3 he is.

**Before logging any found job, it must clear four gates: real · still open · a genuine fit against `PROFILE.md` · legitimate (not a scam or harvesting front).** Anything failing one of them gets no `Findings/` folder and no `Found` row — mention it separately as a near-miss instead. If he asked for a number, that number is a target, not a quota: return fewer and say so. Full rule in `CLAUDE.md` § A number I give you is a target, not a quota.

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
- Where they found it (LinkedIn / BDJobs / company site / Fiverr / referral / recruiter)
- Location and work type (remote-global / remote-Bangladesh / government / on-site Dhaka / hybrid) — this fixes the **priority tier**
- Deadline, if any, and **how long the posting has been up** — it changes the urgency advice
- Whether it has already been applied to, or is only a finding

**Check `jobs/Findings/` first.** If a folder for this job already exists, work in it rather than creating a second one — and check whether anything of a *higher* tier is sitting there unapplied. Say so if there is.

## Step 1 — Read the profile in full

Read `PROFILE.md` completely. It fits in a single read. **Do not work from a partial read or from memory of a previous session.** Everything you write must trace back to a line in it.

## Step 1b — Check the assets folder

List `Assets/` and its subfolders every run — contents change, so never work from a remembered inventory.

- `Assets/CV Templates/` — read the template images and the existing resume PDF for layout, section order, and phrasing precedent. **Layout reference only:** no bullet, title, or claim moves from a template or the old PDF into the new CV unless it also traces to `PROFILE.md`. If the PDF contradicts `PROFILE.md`, `PROFILE.md` wins and you tell the user. If a template uses two columns, skill bars, or icons, **do not copy those** — they break gate 1 and cost you at gate 2.
- `Assets/Profile Pictures/` — include a headshot only when the target market or JD expects one (DE/AT/CH, some Asian markets); omit for US/UK/CA. Reference it by relative path.

If something expected is missing — no headshot, no matching template — say so and carry on. Never substitute or generate a placeholder.

## Step 2 — Analyse the job description

Extract, and note explicitly:

- **The priority tier** — 1, 2 or 3, from the table above. State it before anything else; it changes what the CV emphasises and how urgently to advise applying.
- **Knockouts** — anything that will be a yes/no gate on the form: work authorisation, location/timezone, degree, years of experience, a named certification. Flag these to the user immediately; a knockout he can't clear is worth knowing *before* the CV is built. Tier-specific ones that are easy to miss:
  - **Tier 1, global remote:** required timezone overlap, contractor vs employee status, how they pay into Bangladesh, whether "remote" is actually "remote within <country>".
  - **Tier 1, remote in Bangladesh:** occasional-office clauses that make it hybrid in practice.
  - **Tier 2, government:** exact degree title and class, certificate issue dates, CGPA, age limits, quota categories, and a hard application deadline that does not move. These forms are rigid — the CGPA flag (`PROFILE.md` §17.1) matters far more here than elsewhere.
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

**Tier-specific emphasis** — apply on top of the JD tailoring, never instead of it:

| Tier | Push to the top third | Why |
|---|---|---|
| **1 — remote** | Evidence of owning systems end-to-end without supervision, working with international clients, written communication, CI/CD and deployment ownership. Name the timezone (`Dhaka, Bangladesh · UTC+6`) plainly in the contact line. | A distributed team screens for whether he can be trusted unsupervised and whether the hours overlap. Both questions get answered before they read the bullets. |
| **2 — Bangladesh government** | Formal education block with exact degree title, institution and certificate date; certifications; the full legal name. | These are checked against documents, not skimmed. Accuracy outranks punch. Flag the unverified CGPA loudly (`PROFILE.md` §17.1). |
| **3 — on-site Bangladesh** | The standard build. Local market, photo usually expected. | No special handling. |

None of this licenses a new claim. Everything still traces to `PROFILE.md` — this is about ordering evidence that already exists.

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
- [ ] **Body copy is justified** (`p, li { text-align: justify }`); headings, contact block, entry titles, date column and meta/stack lines stay left-aligned. House rule — see `CLAUDE.md` § Justify the body copy. Set it before the first render, since it changes line breaks and therefore the page count
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

## Step 5 — Write the job folder

**Pick the folder first:**

- If a `jobs/Findings/YY-MM-DD_…/` folder for this job already exists — **use it.** Do not create a second folder and do not rename it; its date is the day the job was found.
- Otherwise create `jobs/Findings/YY-MM-DD_<company-slug>_<Role-Name>/` using **today's date** (check it — do not assume), unless the user says he is submitting now, in which case create it directly under `jobs/Applied/`.
- **The date comes first** in the name so the folder list sorts chronologically.

Write three files:

**`cv.html`** — the finished CV, in **HTML** (rendered to PDF in step 5b). This is what gets sent, so it must be complete and standalone: inline `<style>`, `@page { size: A4 }`, single column, semantic `<h1>/<h2>/<section>/<ul>`, DOM order matching reading order, no layout tables, no text baked into images, nothing in a running header or footer. **Body copy justified** (`p, li { text-align: justify }`), headings/contact/titles/dates/meta lines left-aligned — house rule, `CLAUDE.md` § Justify the body copy. Copy any referenced image into the folder and link it by relative path.

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

**Priority tier:** <1 / 2 / 3> — <remote · government BD · on-site BD>, and one line on why.

## Application
| Field | Value |
|---|---|
| Found | YYYY-MM-DD |
| Applied | YYYY-MM-DD (blank until submitted) |
| Source | |
| Location / type | |
| Deadline | |
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
- YYYY-MM-DD — Found
- YYYY-MM-DD — Draft (CV built)
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

## Step 6 — Log it in `jobs/jobs_log.csv`

**There is no `LOG.md`.** The log is `jobs/jobs_log.csv`. Read it first, then **append** a row at the bottom (or update the job's existing row). `id` is the next integer and is **never reused**.

Columns, in order:

```
id,date,title,type,location,priority_tier,short_description,company,role,source,status,updated,folder_local_location
```

Example:

```
2,2026-08-04,Senior Backend Engineer,Remote,Global,1,"Distributed Python/FastAPI team, 4h UTC overlap required.",Acme Corp,Backend Engineer,LinkedIn,Draft,2026-08-04,jobs/Findings/26-08-04_acme-corp_Senior-Backend-Engineer
```

Rules:
- **Quote any field containing a comma.** A short_description almost always needs quoting.
- Dates are `YYYY-MM-DD`, always. Never `26/07/24`.
- `date` = date **found** for `Findings/` rows, date **applied** for `Applied/` rows. `updated` = the last status change.
- `priority_tier` is never blank.
- `folder_local_location` is repo-relative with forward slashes, and must match where the folder actually is.
- If the CV is generated but not yet submitted, the status is `Draft` and the folder stays in `Findings/`.

## Step 6b — When he confirms he has submitted

1. **Move** the folder `jobs/Findings/<name>/` → `jobs/Applied/<name>/`. Move, never copy; leave nothing behind. The name does not change.
2. Update that CSV row: `status` → `Applied`, `updated` → today, `date` → the submission date, `folder_local_location` → the new path.
3. Append `- YYYY-MM-DD — Applied` to the `## Status timeline` in `notes.md`, and fill the `Applied` row of its table.

Do all three in one edit. A folder in `Applied/` with a `Draft` row, or a CSV path pointing at a folder that moved, is exactly the failure this log exists to prevent.

## Step 7 — Report back

Tell the user, briefly:
- **The priority tier**, and whether anything of a higher tier is still sitting unapplied in `jobs/Findings/`
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

1. Find the job's row — grep `jobs/jobs_log.csv` for the company. `folder_local_location` gives you the folder.
2. Update `status` **and** `updated` in that row. Use the exact vocabulary: `Found` · `Draft` · `Applied` · `Screening` · `Task/Test` · `Interview` · `Final` · `Offer` · `Rejected` · `No response` · `Withdrawn`.
3. If the status crosses from `Draft` to `Applied`, run **Step 6b** — the folder moves to `Applied/`.
4. Append a dated line to the `## Status timeline` in that folder's `notes.md`.

Keep both in sync — the CSV is the index, the notes are the record. If they disagree, the notes win and the CSV gets corrected.

## Interview retrieval

When asked *"what did I send to X?"* or *"prep me for the X interview"*: find the folder via `jobs/jobs_log.csv`, then read that folder's `notes.md` first (it holds the story that was told), then `cv.html`, then `job-description.md`. Lead the answer with the projects featured and the weak spots recorded — those are what the interview will probe. Then work through every quantified bullet on the CV and check he can defend the number; hiring managers probe metrics that look large relative to scope.
