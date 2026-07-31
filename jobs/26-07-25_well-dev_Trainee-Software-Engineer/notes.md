# Notes — WellDev, Trainee Software Engineer

**Applied via:** WellDev recruitment portal — `recruitment.welldev.io`
**Posting deadline:** 2026-07-25 (same day the CV was generated)
**Next step per JD:** Onsite MCQ test, tentatively **31 July 2026**, notified by email to shortlisted candidates
**Recruitment process doc:** linked from the JD — [Google Drive](https://drive.google.com/file/d/1NHE5wISWjLuy84Pqe9si97GeCXAjBedV/view?usp=sharing)

---

## Status timeline

| Date | Status | Detail |
|---|---|---|
| 2026-07-25 | `Draft` | JD scraped and archived; CV generated. Not yet submitted. |
| 2026-07-25 | `Draft` | CV rebuilt as **`cv.html`** (2 pages A4) using `Assets/`. `cv.md` removed — see "Format and assets" below. |
| 2026-07-25 | `Draft` | **CV rebuilt a second time against the three-gate model** (`.claude/skills/cv-builder/references/ats-and-hiring-manager.md`). PDF exported. See "Rebuild against the three-gate model" below. |
| 2026-07-31 | `Draft` | **MCQ-exam preparation pack built** — one-day / 12-hour plan (11 sessions), 15 topics, **126 MCQs** in two sets, 4 read-aloud scripts. HR and technical-interview material written and parked without a plan. Research found two first-hand candidate reports naming all four rounds, the Quilgo platform and dozens of questions. See [`preparation/`](preparation/). |

---

## Format and assets

**The artifact of record is [`cv.html`](cv.html).** It is a standalone HTML file intended to be fed to my own HTML→CV builder tool. The earlier `cv.md` was deleted rather than kept alongside it: it had drifted (longer copy, CHYR as a full entry) and two divergent "CVs that were sent" in one folder is exactly what breaks retrieval when a recruiter calls back. `PROFILE.md` remains the source for anything trimmed out.

| Asset used | How |
|---|---|
| `Assets/CV Templates/cv_temp_1.png` | **Primary layout reference.** Single column, left-aligned bold section headings each with a full-width rule, dates right-aligned on the title row, photo top-right. Chosen over the other three because it is the plainest: `cv_temp_3` has decorative swirls, `cv_temp_2` centres its headings (harder to skim), `cv_temp_4` puts the summary in a side-by-side block with the photo. Simple + single-column is also what parses most reliably. |
| `Assets/CV Templates/Abdullah_Md_Jahid_Hassan_resume.pdf` | Phrasing and section-order precedent only. Its `Label: items` skills format was carried over. **No content was lifted** — its summary and skills are the stale 2025 versions superseded by `PROFILE.md` §3 and §15, and it prints the dead `amjh.space` link. |
| `Assets/Profile Pictures/Formal profile picture .png` | Copied into this folder as `profile-photo.png` (480×600, 4:5) and referenced by relative path so the folder stays self-contained. **Photo included** because this is a Bangladesh-market application and my own existing resume reserved space for one. Removable by deleting one `<img>` and the `.masthead__photo` rule — noted in a comment in the file. |

**ATS-safety choices in the markup:** semantic `<h1>/<h2>/<section>/<ul>`, DOM order identical to reading order, no multi-column layout, no layout tables, no text baked into images, real selectable text throughout. Verified by extracting text from the rendered PDF: `Claude Code`, `Cursor`, `object-oriented analysis`, `data-flow diagrams`, `Data Structures`, `Bangla` all present; `gRPC`, `amjh.space` and `pythonanywhere` all absent.

**Length:** 2 pages of A4, verified by headless render (93% / 96% page fill). Getting from an initial 4 pages down to 2 required two things — letting long entries break across pages (`break-inside: avoid` on an 8-bullet job was stranding 10–15% of every sheet) and cutting roughly a quarter of the copy.

---

## Rebuild against the three-gate model (2026-07-25, second rebuild)

The CV was rebuilt after the CV-building research landed in
`.claude/skills/cv-builder/references/ats-and-hiring-manager.md`. The substance,
the honest-senior framing and the project selection below all stood up and were
kept. What changed is how the document is structured for its three readers —
the parser, the 7.4-second recruiter skim, and the hiring manager.

**Gate 1 — parser fixes**

| Was | Now | Why |
|---|---|---|
| `Summary`, `Core Skills`, `Certifications & Additional` | `Professional Summary`, `Technical Skills`, `Certifications` | Parsers match section headings as literal strings; the non-standard names risked the section not being recognised. |
| `Jan – Jul 2026` (ProspectLead) | `Jan 2026 – Jul 2026` | A range whose first half has no year is a known extraction failure. |
| `Jul 2026 – ongoing` (Smartwatch) | `Jul 2026 – Present` | `Present` is the token parsers look for; `ongoing` is not. |
| `22 Jul 2025` / `5 Jun 2024` (certifications) | `Jul 2025` / `Jun 2024` | Consistent `Mon YYYY` throughout. |

**Gate 2 — the 7.4-second skim**

- **Tagline changed** from `Backend Software Engineer — Python · Django · FastAPI`
  to `Software Engineer — Backend · Python · Django · FastAPI · Cross-stack generalist`.
  Two reasons: the posted role title is *Software Engineer*, so the match is now
  literal in the top third; and *generalist* is one of the JD's stated
  additional requirements, which the old tagline actively worked against by
  reading as a narrow specialist.
- **`Software Development Life Cycle (SDLC)`** now spelled out as a skills-group
  label instead of the bare `SDLC`. It is the JD's own phrase, verbatim, in its
  first responsibility line.
- **Bullets re-front-loaded.** The DRF permission-gap bullet used to open
  *"Corrected framework behaviour by…"*; it now opens
  *"Closed a real security gap by reading framework source…"* — outcome first,
  because the left edge is what gets read and the right-hand half often does not.
- **English moved ahead of Bangla** in the languages line — the JD names both as
  mandatory and English first.

**Gate 3 — hiring manager**

- Body type raised **8.8pt → 9pt** and the copy cut to pay for it. The research
  puts 10–12pt as the norm and 8.8pt as the absolute floor; 9pt is still below
  the norm but is what fits without losing evidence.
- **Softvence kept at 8 bullets but tightened.** Eight is at the limit of what
  survives a skim, and dropping to six was considered. It was rejected because
  each of the last three answers a distinct JD requirement — deployment
  ownership, event-driven architecture, code review — so they were compressed
  instead of cut. Worth revisiting if this CV is reused for a JD that does not
  ask for all three.
- No metric was added, changed or inflated. Every number on the CV is one that
  can be defended against the scope described next to it — that was checked
  deliberately, because a metric that outruns its scope is a documented reason
  hiring managers distrust an entire document.

**What the second rebuild cost.** Roughly 100px of copy had to come out to buy
the type increase and enough page-break headroom. Cut: integration lists trimmed
(Cal.com and Google Calendar dropped from the event-driven bullet, both still in
`PROFILE.md` §7.1), the Omnyvora design-system parenthetical, the ArchiCoPro /
LookUp / Outdoorda descriptors in the "Also built" line reduced to bare
qualifiers, `ERD modelling` dropped from the Data skills row (still present in
the SDLC row), and HSC/SSC merged onto one line. **Nothing that answers a JD
requirement was removed.**

**Verification (measured, not estimated)**

| Check | Result |
|---|---|
| Page count | **2** (headless Chrome via `tools/html_2_pdf`) |
| Page 1 fill of printable area | **94.2%** (rule: ≥90% on every page but the last) |
| Page 2 fill of printable area | **99.0%** (rule: ≥75% on the last) |
| Page breaks | Clean — page 1 ends on the last Softvence bullet, page 2 opens on the Omnyvora title. No entry heading is stranded at a page foot. |
| Text layer | **Real, selectable text** — 10,967 characters extracted from the PDF |
| Section headings present | Professional Summary · Technical Skills · Professional Experience · Selected Projects · Education · Certifications |
| Dates extract correctly | `Aug 2025 – Present` · `Jun 2026 – Present` · `Feb 2024 – Jul 2024` · `Jan 2026 – Jul 2026` · `Jul 2026 – Present` · `May 2020 – Jun 2024` |
| JD keywords present | `Claude Code` · `Cursor` · `AI-generated code` · `object-oriented analysis and design` · `systems thinking` · `data-flow diagrams` · `flowcharts` · `Data Structures & Algorithms` · `REST APIs` · `event-driven` · `code review` · `Software Development Life Cycle (SDLC)` · `English` · `Bangla` |
| Forbidden strings absent | `gRPC` · `amjh.space` · `pythonanywhere` · every client internal folder name · the `$9,000` SafeTag figure · the unverified `3.42` CGPA |
| No date uses the word "to" | Confirmed — every ` to ` in the document is ordinary prose |

**A third pagination trap, found on this build.** The first render ended page 1
on the Omnyvora title plus its "Own organisation" meta line, with all three
bullets stranded overleaf. `break-after: avoid` on the title row does *not*
prevent this — the meta line sits between the title and the bullets and
satisfies the rule. The fix is `break-after: avoid` on `.entry__meta` and
`.entry__stack` as well, so the whole title block travels with its content.
Worth carrying into the skill's pagination notes.

**Exported file:** `Abdullah_Md_Jahid_Hassan_CV_Trainee_Software_Engineer.pdf`
(184 KB, 2 pages), written by
`tools/html_2_pdf/venv/Scripts/python.exe tools/html_2_pdf/html_to_pdf.py <folder> --no-input`.

> **Note on keyword density.** `Django` appears 20 times, `FastAPI` and `Docker`
> 6 each. That is above the 2–3 rule-of-thumb cap, but the cap exists to catch
> *forced* keywords — every instance here sits inside a real sentence describing
> real work on a Django codebase, which is what an LLM screener and a human both
> reward. Left as is deliberately.

**What the 2-page limit cost:** **CHYR was demoted** from a full project entry to the "Also built" line. It was the most redundant of the five against this JD — its unique signals were team-of-three collaboration and code review, and the Softvence bullets already carry both. Its payments/subscription depth survives in compressed form. Also compressed: Core Skills merged from 11 groups to 8; `django_templet` folded into the same tail line; HSC/SSC to a single two-line block; certifications and the self-directed-learning note merged into one closing section.

---

## The central strategic decision

**This is a fresher/trainee requisition and I am not a fresher.** The JD states the programme is *"specially designed to boost up the career in Software Industry just after graduation from university without any software development experience"*, lists the position level as `fresher`, and offers 50,000 BDT/month through a six-month probation.

I am a Senior Python Executive with eight production backends, promoted within eleven months.

**Decision taken (2026-07-25): apply anyway, with an honest senior CV.** No downplaying of the Softvence role, the promotion, or Omnyvora. The bet is that WellDev's JD has been deliberately rewritten for the AI era — it weights AI-output verification, specification skill and learning velocity above coding throughput — and that a candidate who can actually evidence all three is worth more to them than the fresher framing implies. The JD's own line *"6 Months in Standard Case — can be reduced for extraordinary performers"* is the lever to pull in conversation.

**Accepted risk:** being screened out as overqualified against a fresher req, and entering below current level and pay.

**Eligibility confirmed:** the only hard academic gate is *"complete graduation and obtain academic certificates by August 2026"* — degree certificate issued **30 May 2024**, so satisfied. Age limit 30 — satisfied. This is why the CV states the certificate issue date explicitly under Education.

---

## Summary variant used

**Adapted from `PROFILE.md` §3.2 (senior / lead-leaning)**, deliberately bent onto the JD's four stated axes rather than used as written:

1. Learning velocity ("learns unfamiliar stacks by building production systems in them")
2. AI-assistant fluency *with verification ownership* — given its own paragraph, because it is the JD's headline requirement
3. Specification and reasoning over coding throughput — explicitly called "my strongest half of this job"
4. Generalist / cross-stack breadth, plus the mandatory English + Bangla

§3.6 (junior-to-mid) was considered and rejected — it would have undercut the honest-senior decision above.

---

## Projects featured, and why

| Project | Why this one |
|---|---|
| **SafeTag** *(placed first, deliberately)* | The JD says *"Strong reasoning and specification skills are weighted more heavily than coding throughput"* and asks for help *"creating flowcharts, layouts and documentation"*. SafeTag is a pure specification deliverable — 9 chapters, use case / activity / swimlane / ERD / DFD, function-point estimation, RMMM. Nothing else in my profile answers that requirement as directly, so it leads. |
| **ProspectLead** | Lead-developer ownership + live public URL + the generalist proof point: I wrote the backend, designed the UI/UX *and* built the n8n workflow. Also carries the event-driven and OpenAI-cost-governance evidence. |
| **CHYR** | Team-of-three collaboration and code review (JD asks for both), plus payments/subscription depth and multi-region AWS. |
| **Long-Range Smartwatch** | Best single answer to *"comfortable with ambiguity"* — the value is the sequencing decision (build the service layer first, defer API design until the device protocol is known), not the code. Also self-directed. |
| **`django_templet`** | The *"track record of self-directed learning beyond formal coursework"* additional requirement. |

Remaining client work (OCReels, Tundra, ArchiCoPro, LookUp, Outdoorda) compressed to a single line to prove breadth without a project dump.

---

## JD keywords targeted (mirrored literally for ATS)

`software development life cycle (SDLC)` · `AI-assisted development tools` · `AI coding assistants` · `Claude Code` · `Cursor` · `AI-generated code` · `retaining full ownership of correctness, security, and code quality` · `REST APIs` · `event-driven` · `algorithms` · `data structures` · `systems thinking` · `object-oriented analysis and design` · `decompose ambiguous problems into precise specifications` · `flowcharts` · `documentation` · `code review` · `security practices` · `adapt across the stack` · `generalist` · `ownership` · `self-directed learning` · `English and Bangla` · `international clients` · `primary documentation` / `source code`

Reinforced with the profile's own evidence-backed terms: Docker, Docker Compose, GitHub Actions, CI/CD, AWS EC2/IAM/S3/SES, PostgreSQL, Redis, Celery, JWT, RBAC, Stripe, webhook idempotency, Next.js, React, TypeScript.

---

## Deliberately omitted — and why

| Omitted | Reason |
|---|---|
| **gRPC** | The JD lists it under *"Exposure to modern backend communication patterns (REST, gRPC, event-driven architectures)"*. **I have zero evidence for gRPC anywhere in `PROFILE.md`.** Not claimed, not implied, not softened into "familiar with". REST and event-driven are led with instead; the JD's own *"willingness to learn whatever the project demands"* covers the rest, and this is the honest thing to say if asked. |
| **`amjh.space` / `isp.amjh.space`** | Domain expired (`PROFILE.md` §17.5). Never printed. |
| **PythonAnywhere portfolio** | Live but ~1 year stale — no Softvence work, no Omnyvora, no FastAPI/AWS/CI-CD. This JD does **not** demand a live portfolio URL, so it was excluded rather than shipped as an underselling link. GitHub + LinkedIn + Omnyvora org used instead. |
| **SafeTag's $9,000 contract value** | `PROFILE.md` §13 permits it only for pre-sales/consulting-oriented JDs. This is a trainee engineering req — the figure would read as showing off. The *deliverable* is described; the money is not. |
| **All client internal folder names / codenames** | NDA (§13). Product names only: CHYR, ProspectLead, SafeTag, Tundra, OCReels, ArchiCoPro, LookUp, Outdoorda. |
| **The fitness-tracking platform's product name** | Not recorded in my working copy (§7.7) — described generically in the eight-backend count, never named. |
| **ESP8266 "evil twin" access-point lab work** | Genuine wireless-security experience, but this is not a security JD and the framing risks being misread. Omitted. |
| **Server IPs, IAM keys, `.pem` files, API keys** | Never, anywhere. |
| **Early CLI exercises** (calculators, contact manager, library management v1/v2) | Superseded — including them against a senior-framed CV would drag the level down. Covered by the "27 public repositories" line instead. |
| **Hindi** | Kept in the CV's spoken-languages line, but the JD's mandatory pair is English + Bangla, so those lead. |

---

## ⚠️ Flagged for verification before sending

**CGPA 3.59 / 4.00 is unverified.** `PROFILE.md` §17.1: the structured education record says 3.59, an older written bio says 3.42. **This matters more here than on a typical application** — fresher pipelines routinely check transcripts, and WellDev requires academic certificates as an eligibility gate. Confirm against the official IUBAT transcript before submitting.

---

## Interview preparation — specific to this posting

1. **The MCQ test (~31 July 2026) will likely be DSA, OOP and aptitude heavy.** This is my thinnest evidenced area: coursework and the C++ compiler-simulation project, but no competitive-programming record. Highest-value prep item, and the shortest runway.
2. **They explicitly ask for a prepared answer** on learning a stack while building it: *"Candidates should be prepared to discuss a concrete example during the interview."* Three available — (a) PHP/MySQL → production Django, self-taught in under a year; (b) FastAPI + Tortoise ORM learned on live client work under deadline; (c) Next.js 16 / React 19 / TypeScript self-taught to build Omnyvora. **(b) is the strongest** — highest stakes, real deadline, client-facing.
3. **Expect "why are you applying to a trainee role?"** Have a direct, non-defensive answer ready. Do not pretend to be less experienced than I am.
4. **Expect a commitment probe.** The JD screens out candidates planning higher studies abroad and says it seeks *"candidates who are committed to a long-term career with WellDev"*. Founding Omnyvora may also read as a competing commitment or flight risk — be ready to frame it honestly as self-directed learning and product curiosity, and be clear about what it does and does not demand of my time.
5. **AI-verification questions are near-certain** given how the JD is written. Best concrete examples: the `ai_rules.md` engineering constitution written for the LookUp project, and the DRF safe-method permission gap I found by reading framework source rather than accepting default behaviour.
