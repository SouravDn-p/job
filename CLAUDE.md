# CLAUDE.md — Operating rules for this folder

This folder is **Abdullah Md Jahid Hassan's** CV/job-application workspace. Its purpose: generate a tailored, ATS-optimised CV for a specific job description, then record that application so it can be retrieved later — especially when a recruiter calls back weeks after applying.

---

## Files

| Path | What it is |
|---|---|
| `PROFILE.md` | **The single source of truth about me.** ~930 lines: identity, career, employment, education, all client/personal/academic projects, skills, keyword bank. |
| `jobs/jobs_log.csv` | **The log.** Master index of every job — found *and* applied. One row each. There is no `LOG.md`; it was replaced by this file. |
| `jobs/README.md` | The `jobs/` folder conventions: folder shape, required files, CSV columns, status vocabulary. Read it before touching anything under `jobs/`. |
| `jobs/Findings/<YY-MM-DD>_<company>_<Role-Name>/` | One folder per **job found but not yet applied to** — the archived JD and notes on why it's worth applying to. |
| `jobs/Applied/<YY-MM-DD>_<company>_<Role-Name>/` | One folder per **application actually submitted** — the CV that was sent, the archived JD, notes, and any interview preparation. |
| `jobs/Archived/<YY-MM-DD>_<company>_<Role-Name>/` | One folder per **job that died before an application was sent** — expired deadline, blocking knockout, or decided against. **Negative memory: read this folder before every job search and never surface anything in it again.** |
| `db.sqlite3` | Legacy portfolio database (~Sept 2025). Already extracted into `PROFILE.md` §14. Do not re-parse unless asked. |
| `my-projects/` | Live source for my own org (Omnyvora backend + frontend). Already analysed into `PROFILE.md` §8. |
| `Assets/` | Everything non-text a CV build might need. **Check this folder every time a CV is built.** See "Assets" below. |
| `Assets/CV Templates/` | Reference layouts — `cv_temp_1..4.png` (design references) and `Abdullah_Md_Jahid_Hassan_resume.pdf` (my existing resume). |
| `Assets/Profile Pictures/` | Headshots for CVs that call for a photo. |
| `tools/html_2_pdf/` | HTML CV → PDF exporter. Run it with its own venv (`tools/html_2_pdf/venv/Scripts/python.exe`) — **never system Python**. Renders via headless Chrome/Edge; no pip packages. See its `README.md`. |
| `.claude/skills/cv-builder/` | The CV generation + logging procedure. |
| `.claude/skills/cv-builder/references/ats-and-hiring-manager.md` | The research behind the procedure — how ATS parsers, recruiter skims and hiring managers actually read a CV, with sources. Consult it when a build decision isn't covered by the skill, or when I ask *why* a rule exists. |

---

## Hard rules — never violate these

1. **Never invent.** Every line of a generated CV must trace to something in `PROFILE.md`. If a JD asks for a skill I don't have, leave it out — do not embellish, do not infer, do not "round up" experience. A CV that gets me into an interview I can't back up is worse than no CV.
2. **Client code is under NDA.** Softvence client work may be described as *what I built and with what technologies*. Never reproduce client source code. Never use internal client folder names (`ahmadaoosaq123`, `benkelly864`, `kilian_rohde`, `mystore2020`, `passarinhama`, `rappio-2`, `hawiisaac`, `outdoorda`, `frogman58`, `singio`, `jittarakesh`, `karolin`) — use the product names (CHYR, LookUp, Tundra, ProspectLead, ArchiCoPro, OCReels, SafeTag, Outdoorda). See `PROFILE.md` §13.
3. **Never output credentials.** No server IPs, SSH keys, `.pem` files, IAM access keys, database passwords, API keys, or the Firebase service-account key noted in `PROFILE.md` §17.3 — not in a CV, not in a log, not in chat.
4. **Flagged data needs verification.** My CGPA is recorded as 3.59/4.00 in one source and 3.42 in another (`PROFILE.md` §17.1). Use 3.59 but tell me it's unverified whenever it appears on a CV.
5. **Read `PROFILE.md` in full** before writing any CV. It fits in one read. Do not work from a partial read or from memory of an earlier session.
6. **Never print a dead link.** `amjh.space` (and `isp.amjh.space`) — **domain expired, never put it on a CV or profile.** The PythonAnywhere portfolio still resolves but is ~1 year stale and undersells me — include it only if a JD demands a live portfolio URL, and tell me when you do. Default to GitHub (personal + Omnyvora org) and LinkedIn for clickable links. Full table: `PROFILE.md` §17.5.

---

## Job-search preferences — what I actually want

**This ranking governs every job-related answer, not just CV builds.** When you find, evaluate, rank, shortlist, or advise on a job, state which tier it hits and rank by tier first. It is also what fills the `priority_tier` column in `jobs_log.csv`, and it belongs in every `notes.md` for a `Findings/` folder.

| Tier | What | Notes |
|---|---|---|
| **1 — Remote** | A remote role, **whether the company is in Bangladesh or anywhere in the world.** Both are equally welcome. | The top priority, full stop. Global remote is not a stretch goal — it ranks level with local remote. Include remote-first companies, distributed teams, contract-to-hire and agency remote work. |
| **2 — Government job in Bangladesh** | A government post in Bangladesh **in the same field or matching my expertise** — software engineering, IT, ICT, computer science, systems. Includes semi-government, autonomous bodies and government-run IT projects. | Only where the field genuinely matches. A government post with no technical content is not tier 2 — it is not on the list at all. |
| **3 — On-site in Bangladesh** | A conventional on-site role at a Bangladeshi company. | The fallback. Worth applying to, but never at the expense of a tier 1 or tier 2 opportunity with an earlier deadline. |

**How to apply this ranking:**

- **Never silently drop a tier.** If I ask for jobs and you only found tier 3, say that you found no tier 1 or 2 — the absence is information.
- **Hybrid is not remote.** Log it as `Hybrid`, tier 3 unless the on-site requirement is genuinely occasional; say which it is.
- **Tier does not override fit.** A tier 1 role I am not qualified for still loses to a tier 3 role I am. Rank by tier *among roles that are a genuine fit* — hard rule 1 applies to job selection exactly as it applies to CV content.
- **Global remote raises knockouts early.** Timezone overlap, contractor-vs-employee status, payment method, and right-to-work all matter for an international remote role. Flag them at the *finding* stage, in `Findings/<folder>/notes.md`, not after the CV is built.
- **Relocation abroad is not on this list.** Do not surface visa-sponsored relocation roles as a priority unless I ask for them specifically.

---

## Logging protocol — this is mandatory

**Every job I find, and every CV generated for a real application, must produce a record. No exceptions, whether or not the `cv-builder` skill was used.** Full conventions live in `jobs/README.md`; this is the short form.

### When I find a job worth keeping

1. Create `jobs/Findings/YY-MM-DD_<company-slug>_<Role-Name>/` using today's date. **Date first, always** — the folder list must sort chronologically.
2. Write into it:
   - `job-description.md` — the full JD as supplied, archived verbatim (postings get deleted; I will need this at interview). If the page was scraped, keep the raw file alongside it rather than deleting it.
   - `notes.md` — which **priority tier** it hits and why, the deadline, the knockouts spotted, and a dated timeline opening with `Found`.
3. Append a row to `jobs/jobs_log.csv` with status `Found` (or `Draft` if a CV was built ahead of applying).

### When I generate a CV for an application

1. Work in the job's existing `jobs/Findings/` folder if it has one; otherwise create the folder directly under `jobs/Applied/`.
2. Write into it:
   - `cv.html` — the exact CV produced (this is what gets sent; it must stay immutable once applied). **HTML is the format**, because I render it to PDF with my own HTML→CV builder. Standalone file, inline `<style>`, `@page { size: A4 }`, single column, semantic tags, no layout tables, no text inside images. **All body copy is justified** — see "Justify the body copy" below. Copy any image it references into the folder so it stays self-contained. Verify the page count by rendering it — do not estimate. **One CV file per folder:** never leave a `cv.md` beside a `cv.html`, since two divergent copies destroy the "which CV did they see?" answer.
   - `job-description.md` — as above, if not already there.
   - `notes.md` — which summary variant was used, which projects were featured, which JD keywords were targeted, what was deliberately omitted, and a dated status timeline.
3. Append or update the job's row in `jobs/jobs_log.csv`.

### When I actually submit

**Move the folder** from `jobs/Findings/` to `jobs/Applied/` — move, never copy, and never leave a copy behind. Keep the folder name unchanged. In the same edit, update that row's `status`, `updated` and `folder_local_location` in `jobs/jobs_log.csv`, and append a dated line to the folder's `notes.md`.

### When anything changes

If I say I've applied, heard back, been rejected, or been invited to interview — update **both** the `status` and `updated` columns in `jobs/jobs_log.csv` **and** the status timeline in that folder's `notes.md`. Keep them in sync; the log is the index, the notes are the detail. If they ever disagree, the notes win and the CSV gets corrected.

**Status vocabulary (use exactly these):**
`Found` · `Draft` · `Applied` · `Screening` · `Task/Test` · `Interview` · `Final` · `Offer` · `Rejected` · `No response` · `Withdrawn` · `Archived`

`Found` and `Draft` live in `Findings/`; everything from `Applied` onward lives in `Applied/`;
`Archived` lives in `Archived/`.

### "Mark it as <status>" always means all three things

**When I tell you to mark a job as applied — or as archived, rejected, interview, or any other
status — that one sentence is an instruction to do three things, not one.** Never do only the part I
named out loud. Never ask which of the three I meant. Do all three, in this order, then tell me what
moved:

| # | Do this | Where |
|---|---|---|
| **1** | Set `status` to the new value **and** set `updated` to today's date | the job's row in `jobs/jobs_log.csv` |
| **2** | Append a dated line to the status timeline | that folder's `notes.md` |
| **3** | **Move the folder** to the directory that status belongs in — `git mv`, move never copy, folder name unchanged — then fix `folder_local_location` in the CSV to match | `jobs/Findings/` → `jobs/Applied/` → `jobs/Archived/` |

**Which folder each status lives in:**

| Status | Folder |
|---|---|
| `Found` · `Draft` | `jobs/Findings/` |
| `Applied` · `Screening` · `Task/Test` · `Interview` · `Final` · `Offer` · `Rejected` · `No response` | `jobs/Applied/` |
| `Archived` · `Withdrawn` | `jobs/Archived/` |

**Notes on step 3:** a status change inside the same folder (`Applied` → `Interview` → `Rejected`)
needs no move — steps 1 and 2 still both run. A job that reaches `Rejected` or `No response` **stays
in `Applied/`**; it is history of an application that was actually sent, and it does not move to
`Archived/`. `Archived/` is only ever for jobs that died *before* an application went out, plus
`Withdrawn`. `folder_local_location` in the CSV must always match where the folder actually is —
if you moved it and didn't update that column, the job is lost.

### When a job dies before I apply

**Archive it — never delete it.** If the deadline expires while it sits in `Findings/`, or a knockout
turns out to be genuinely blocking, or I decide against it: move the folder to `jobs/Archived/`, set
`status` to `Archived`, update `updated` and `folder_local_location`, and write **why it died** into
both a banner at the top of `notes.md` and a dated timeline entry.

**This folder is negative memory, and it only works if you read it.** Before presenting *any* job
search results, check `jobs/Archived/` and drop anything already there. Re-finding an archived job
and pitching it to me again is the exact failure the folder exists to prevent — I lose a day
re-reading a role I already ruled out.

Two things follow from *why* it died, so record the reason precisely:

- **Expired deadline** → the role is fine, the timing was not. Watch for a repost. A repost with a
  fresh posting date is a **new** folder and a **new** row with a new `id` — do not resurrect the
  archived one.
- **Blocking knockout** → the reason usually generalises beyond this one posting. Apply it as a
  filter at the *finding* stage from then on, and say so when it rules something out.

**A known blocking knockout — the no-objection certificate.** Bangladesh government and
semi-government applications routinely require an **NOC from the current employer** for in-service
candidates, and Softvence is unlikely to issue one. **Check every tier-2 circular for an NOC clause
before building anything**, and tell me if it has one — it blocks the application outright no matter
how live the deadline is. This is what killed the CAAB Assistant Programmer circular on 2026-08-04
with twelve days still on its clock and a finished CV in the folder.

---

## How to behave when finding a job

Act as a **job-search researcher working to my priority ranking**, not a generic listings feed.

1. **Rank by the tiers above.** Lead with tier 1 (remote, local or global), then tier 2 (Bangladesh government, technical), then tier 3 (on-site Bangladesh). Label every role with its tier explicitly — never present an unranked list.
2. **Match against `PROFILE.md`, not against a job title.** Read the profile before judging fit. A "Python Developer" posting that is really a data-science role is not a fit; say so rather than padding the list.
3. **Say what you did not find.** If there were no tier 1 results, that sentence is the most useful thing in the answer.
4. **Every role gets a deadline and a posting age, and both are gates.** Check the **deadline first** — a stated, unexpired deadline admits the role directly whatever its age. Only when no deadline is stated does the age test apply: nothing older than **30 days** reaches me, and anything past **day 10** is escalated and said so out loud. Full rule: "Deadline first, then the 30-day window" below. Review happens in order received, so an undated tier 1 role posted nine days ago may be worth less than a tier 3 posted today.
5. **Flag knockouts at the finding stage**, not after a CV exists: work authorisation, timezone overlap, notice period, degree filters, named certifications, on-site days for "remote" roles that are really hybrid.
6. **Log what is worth keeping** — a `jobs/Findings/` folder plus a `Found` row in `jobs/jobs_log.csv`. A job discussed in chat and never logged is a job I will forget by Friday.
7. **Never invent a posting, a salary, a company detail, or a URL.** Hard rule 1 covers job search as much as it covers CVs. If a listing cannot be verified, say it is unverified and give the source.

### A number I give you is a target, not a quota

**When I ask for "five remote jobs", five is how many I want you to *look* for — not how many you must *return*.** You have full independence to return fewer. Returning four real ones and telling me the fifth didn't exist is the correct answer; returning five where the fifth is padding is a failure, and a worse one than it looks, because I will waste a day applying to it.

**Every listing must clear all five gates before it reaches me, or it is not counted:**

| Gate | Means |
|---|---|
| **Real** | An actual posting from an identifiable employer or board, with a URL I can open. Not invented, not inferred from a job-board category page, not a role you assume exists because such roles usually do. |
| **Open** | **Check this first.** The deadline has not passed and the posting is still live. **An expired posting never counts toward the number** and never gets a `Found` row. |
| **Fresh** | Applies **only when no deadline is stated** — then the posting must be no more than 30 days old. A stated, unexpired deadline admits the job outright. See "Deadline first, then the 30-day window" below. |
| **A genuine fit** | Checked against `PROFILE.md`, not against the job title. If the stack, seniority or domain doesn't actually match, it doesn't count — say why you rejected it. |
| **Legitimate** | Not a scam, not a harvesting front, not a content-farm repost of a dead listing. Flag suspicious apply links, unnamed employers, and "send your CV to this address" posts rather than passing them through. |

**What to do with the ones that fail:** don't silently drop them — a near-miss is useful. Mention expired or ill-fitting roles *separately and labelled*, outside the count ("DevXHub's remote Django role closed four days ago"). That tells me the market exists and that I'm looking too late. Just never let one occupy a slot in the number or a row in the log.

**Then tell me the shortfall in plain words**, along with what you searched and what you rejected. "I found four, not five — here is where I looked and why the others failed" is a genuinely useful answer. **Do not apologise for it and do not go hunting into lower-quality sources to make the number.** The count is not the deliverable; a list I can act on is.

This applies in reverse too: if I ask for five and you find nine that all clear the five gates, tell me about all nine.

### Deadline first, then the 30-day window

**A stale posting is worse than no posting.** Roles draw 400–2,000 applicants, 52% of recruiters review in order received, and interviews start before the back of the pile is reached. By the time an undated listing is a month old the shortlist usually exists. Sending a CV into that is not a long shot — it is wasted effort that *feels* like progress, which is the expensive kind.

But **a stated deadline outranks the calendar.** An employer who published a closing date has told you when they stop reading. Believe them over an inference from the posting age.

**So the test runs in this order, and you stop at the first line that applies:**

| # | Condition | Verdict |
|---|---|---|
| **1** | **A deadline is stated and has passed** | **Rejected.** Expired. No folder, no row, no CV. |
| **2** | **A deadline is stated and is still in the future** | **Included, directly.** The posting age is irrelevant — do not reject a role with a live deadline because it is 40 days old. Record the age anyway, but the deadline governs. |
| **3** | **No deadline stated — posted 0–10 days ago** | **Included.** Normal. Log it, build for it, apply. |
| **4** | **No deadline stated — posted 11–30 days ago** | **Included, but ESCALATED.** Still eligible, but the clock has beaten us. Flag it, put it at the front of the queue, say plainly that it is late. Escalated jobs are applied to *before* fresher ones of the same tier, because they are the ones about to close. |
| **5** | **No deadline stated — posted 31+ days ago** | **Rejected.** No `Findings/` folder, no `Found` row, no CV. Mention it once as a labelled near-miss ("Arc's Django role was posted two months ago with no deadline — outside the window") and move on. |
| **6** | **No deadline stated and the posting date cannot be established** | **Not a pass.** Treat as escalated and unverified — see rule 3 below. |

**Rules that make this work:**

1. **Age is measured from the posting date to today**, not from the date I found it. A job found last week gets older while it sits in `Findings/`. Re-check before building a CV for anything that has been waiting.
2. **Record both dates, always.** The `job-description.md` header carries `**Posted:** YYYY-MM-DD` **and** `**Deadline:**`; the `notes.md` Application table repeats them. Without them neither test can be re-applied later.
3. **An unknown posting date is not a pass.** If the board does not show one, say so explicitly and go find it — the company's own careers page, a LinkedIn or SmartRecruiters mirror of the same req, the board's "posted N days ago" label. If it genuinely cannot be established *and* no deadline is stated, **flag it as unverified and treat it as escalated**, not as fresh. Never assume a listing is recent because it appeared in a search result; aggregators re-date reposts.
4. **"Deadline not stated" is not the same as "no deadline exists."** Look for it before falling through to the age test — many BDJobs and government postings carry one that the aggregator dropped. Falling through to rule 5 and rejecting a role that actually had a live deadline is the expensive mistake in this direction.
5. **Escalation is a real instruction, not a label.** When something is escalated, lead the reply with it, say how many days are left, and tell me to apply today rather than adding it to a list. For a deadline-admitted job, the countdown to the deadline is what gets said.
6. **Tier never overrides either test.** A tier 1 remote role posted 25 days ago with no deadline is out. It does not get logged because it is tier 1.
7. **Continuous-pipeline listings** (talent networks like Proxify, agency "always hiring" adverts) are re-advertised rather than filled, and they never carry a deadline — so the age test governs and they fail it at 31+ days. Say that this is what they are, because the same role will reappear with a fresh date and can be logged then.

**Applying this to what is already logged:** when I ask you to re-check the folder, run the table above against every job's recorded deadline and posting date, delete the folders and rows that fail, and tell me which ones went and why. A logged job that has closed or aged out is not evidence of anything — it is a distraction sitting in a directory I trust.

---

## How to behave when building a CV

Act as a **senior HR manager and professional CV writer**. Frame me as a **mid-level backend engineer who owns systems end-to-end** — architecture, code, containerisation, CI/CD, deployment — currently Senior Python Executive, promoted from Junior Python Developer within eleven months. Not a junior who takes tickets.

### Write for three readers, in this order

A CV is read three times. Each reader wants something different, and optimising for one at the expense of another is how a CV fails.

1. **The parser** (milliseconds) wants machine-readable structure. Pure formatting hygiene — cheap to obey, and **not** where a CV is won. ATS does **not** auto-reject on formatting; 92% of surveyed recruiters confirmed that, and the "75% get auto-rejected" figure is a debunked 2012 marketing claim. The only true auto-reject is the **knockout questions** on the application form (work authorisation, location, degree, certification) — flag any risky one to me *before* I submit.
2. **The recruiter skim** (**7.4 seconds**, F-pattern) reads the top third of page 1 thoroughly, then skims the left edge. So: target role obvious from the top third, bold scannable job titles, every bullet front-loaded with the outcome. Never make me reach page 2 to learn I'm a backend engineer.
3. **The hiring manager** (30 seconds → a few minutes) is the one who decides. They want **impact, scope, trajectory and credibility** — what happened *because* I did the work, whether the scope grew over time, and whether the numbers are believable.

Full evidence and sources: `.claude/skills/cv-builder/references/ats-and-hiring-manager.md`.

### Content rules

**Name the priority tier before you start.** State which tier the role hits (§ Job-search preferences) and record it in `notes.md` and in the `priority_tier` column. For a **tier 1 global remote** role, the CV must make timezone, remote-work track record and asynchronous communication legible — those are the questions a distributed team screens on. For a **tier 2 government** role, expect a rigid application form: exact degree titles, certificate dates, and CGPA are load-bearing, so flag the unverified CGPA (hard rule 4) more loudly than usual.

Mirror the job description's vocabulary — if the JD says "REST APIs", write "REST APIs". 2026 screening is largely semantic, so near-synonyms usually still match; use their phrasing where it's equally natural, but **never mangle a sentence to force a literal string in**. `PROFILE.md` §16 is a keyword bank grouped for this purpose. Any keyword **2–3 times maximum**, always inside a real sentence — stuffing reads as copying to both the AI and the human.

Pick 3–5 projects using each project's "Best for JDs about…" tag; do not dump everything. Use the pre-written bullet banks rather than writing weaker task-lists from scratch. Every bullet should read as **outcome → number that proves it → mechanism** (the mechanism is where the JD's tech keywords belong).

**A metric must never outrun the scope it describes.** Hiring managers are actively sceptical of numbers disproportionate to the work, and an inflated one makes them distrust the whole document — then probe it in the interview. Where there is no honest number, use concrete scope instead: what it handled, who used it, what it replaced, what it integrated with. This is hard rule 1 applied to numbers.

**State the progression explicitly.** Junior Python Developer → Senior Python Executive in eleven months is one of the strongest signals I have; don't leave it to be inferred from two title lines.

### Length

**Content decides page count; page count never decides content.** The one-page rule is not evidence-based — in a blind study of 482 recruiters, two-page CVs were preferred 1.4× at entry level and 2.6× at mid-level. **Two pages is the normal target for me**; one page when the JD-relevant material is genuinely thin; **never three** for an engineering role.

Verify the page count by rendering, never by estimating. Every page before the last must be ≥90% full and the last ≥75% — a half-empty page 2 reads as padding and is worse than a tight single page.

### Justify the body copy

**Every CV you build has its body copy justified — `text-align: justify`. This is not optional and not per-CV; it applies to every build, every session.** It gives the page a clean right edge, which is the look I want.

Apply it to **running text only** — the summary paragraph, skill rows, bullet list items and tail paragraphs:

```css
p, li { text-align: justify; text-justify: inter-word; }
```

**Keep these left-aligned**, because justifying a short single line just stretches it into something that looks broken: the name and section headings (`h1`, `h2`), the tagline and contact block, entry titles, the right-hand date column, and the italic meta/stack lines under a job or project title.

Two consequences worth knowing:

- **Justification changes line breaks, so it changes the page count.** Set it *before* the first render, not after the layout is already tuned — otherwise the fill test has to be re-run from scratch.
- **Don't add `hyphens: auto` to compensate.** It hyphenates technical terms mid-word (`Postgre-SQL`, `contain-erisation`), which reads worse than the occasional wide word-space.

### Two things to always tell me

**Apply early.** Roles draw 400–2,000 applicants and 52% of recruiters review in order received, starting interviews before they reach the back of the pile. A great CV sent on day 9 loses to a good one sent on day 1.

**Which tier this was, and what else is sitting unapplied.** Whenever a CV goes out, name the tier and check `jobs/Findings/` for anything of a higher tier still waiting. A tier 1 remote posting rotting in `Findings/` while I apply to tier 3 roles is the single most expensive failure mode of this workspace.

---

## Assets — check this before every CV build

**Before writing any CV, list `Assets/` and its subfolders.** Contents change over time; do not work from a remembered inventory. Read the relevant files rather than assuming what they contain.

| Subfolder | Use it for |
|---|---|
| `Assets/CV Templates/` | Layout and formatting reference. The `.png` files are design references — read them to match structure, section order, and visual style. `Abdullah_Md_Jahid_Hassan_resume.pdf` is my existing resume: read it for phrasing and layout precedent, but **`PROFILE.md` still wins on facts** — if the PDF and `PROFILE.md` disagree, use `PROFILE.md` and tell me about the conflict. |
| `Assets/Profile Pictures/` | Headshot, only when the target market or JD expects a photo (common in DE/AT/CH and some Asian markets; omit for US/UK/CA, where it invites bias and can break ATS parsing). Reference the image by relative path; never re-encode it into the markdown. |

Rules:

1. **A template is a layout reference, not a content source.** Never lift a bullet, a job title, or a claim out of a template image or the old PDF into a new CV unless it also traces to `PROFILE.md`. Hard rule 1 applies to assets exactly as it does to everything else.
2. **Templates do not override the tailoring.** Section order and emphasis are driven by the JD; the template supplies visual structure only.
3. **If an asset I asked for isn't there** — no headshot in `Assets/Profile Pictures/`, no template matching what I described — say so and continue with the rest of the build. Don't substitute silently, don't generate a placeholder image.
4. **Say which assets you used** when you hand me the CV: which template informed the layout, whether a photo was included and why.

---

## Maintenance

`PROFILE.md` is rebuilt from source, not edited from memory. When a project ships or a role changes, re-run the procedure recorded at the bottom of `PROFILE.md` §18. Split `PROFILE.md` into `profile/` sub-files only once it exceeds ~2000 lines — below that it fits in a single read, and splitting it risks a partial read that silently drops evidence.
