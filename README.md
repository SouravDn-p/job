# CV & Job Application Workspace

Personal workspace for **Abdullah Md Jahid Hassan** — Senior Python Executive, Softvence Agency.

Three jobs:
1. **Find** roles that match my priority ranking — remote first, Bangladesh government second, on-site Bangladesh third.
2. **Generate** a CV tailored to a specific job description, from a single exhaustive profile.
3. **Record** every job, found and applied, so months later I can answer "which CV did they see?" before an interview.

---

## What I'm looking for — in this order

| Tier | What | Notes |
|---|---|---|
| **1** | **Remote** — company in Bangladesh **or** anywhere globally | Both rank equally. This is the priority. |
| **2** | **Government job in Bangladesh**, same field or expertise | Software / IT / ICT / CS, including semi-government and autonomous bodies. |
| **3** | **On-site in Bangladesh** | The fallback. |

Every job logged here carries its tier. Full rules — including how hybrid is treated and which knockouts each tier raises — are in `CLAUDE.md` § Job-search preferences.

**A number I ask for is a target, not a quota.** "Find five remote jobs" means look for five. Every listing has to be real, still open, a genuine fit against `PROFILE.md`, and not a scam or a harvesting front — anything that fails is not counted and not logged. Four real ones plus "the fifth didn't exist" is the right answer; five where the fifth is padding costs me a wasted day. Near-misses get mentioned separately and labelled, never counted. Full rule: `CLAUDE.md` § A number I give you is a target, not a quota.

---

## Layout

```
.
├── CLAUDE.md                      operating rules — auto-loaded by Claude Code every session
├── PROFILE.md                     ← the source of truth. Everything about me, in one file.
├── jobs/
│   ├── jobs_log.csv               THE log — every job, found and applied, one row each
│   ├── README.md                  folder conventions, CSV columns, status vocabulary
│   ├── Findings/                  jobs found, not yet applied to
│   │   └── YY-MM-DD_company_Role/
│   │       ├── job-description.md the JD, archived verbatim
│   │       └── notes.md           priority tier, deadline, knockouts, timeline
│   └── Applied/                   jobs actually applied to
│       └── YY-MM-DD_company_Role/
│           ├── cv.html            the CV that was actually sent (immutable once applied)
│           ├── ..._CV_<Role>.pdf  the rendered file that got uploaded
│           ├── job-description.md the JD, archived verbatim
│           ├── notes.md           tailoring decisions + status timeline
│           └── preparation/       interview & exam prep, one folder per stage
├── prompts/preparation.md         the interview/exam preparation instruction set
├── .claude/skills/cv-builder/     the /cv-builder procedure
├── tools/html_2_pdf/              HTML CV → PDF exporter (own venv)
├── db.sqlite3                     legacy portfolio DB (already extracted into PROFILE.md §14)
└── my-projects/                   Omnyvora backend + frontend source (analysed in PROFILE.md §8)
```

**A folder moves `Findings/` → `Applied/` when the application is submitted** — moved, never copied, and never in both at once. The folder name never changes; its date is the day the job was found.

---

## Usage

**Log a job I found** — paste the posting and say it's a finding. It goes into `jobs/Findings/` with a `Found` row in `jobs_log.csv` and a `notes.md` naming its priority tier, deadline and knockouts.

**Build a CV for a job:**

```
/cv-builder
```

then paste the job description. It reads `PROFILE.md`, tailors a CV to the JD's vocabulary, writes it into the job's folder, and adds or updates its row in `jobs/jobs_log.csv`.

**Say when I've applied:**

> *"Applied to Acme."*

The folder moves from `Findings/` to `Applied/`, and the CSV row and `notes.md` timeline are updated together.

**Update a status** — just say it in plain language:

> *"Got a screening call from Acme."*
> *"Rejected by Tundra."*

Both `jobs_log.csv` and that job's `notes.md` get updated.

**Prepare for a round:**

```
Read prompts/preparation.md and follow it.
Job:   jobs/Applied/<folder>
Stage: technical interview
Time:  3 days
```

**Before an interview:**

> *"Pull up what I sent Acme."*

---

## Why one big PROFILE.md

It's ~930 lines, which fits in a single file read. Splitting it into topic files would mean guessing which ones to open — and missing one silently drops real evidence from a CV. Split it only past ~2000 lines. Reasoning is at the bottom of `CLAUDE.md`.

## What must never leave this folder

Client source code (NDA), internal client identifiers, and any credential — server IPs, `.pem` keys, IAM access keys, database passwords, API keys. See `PROFILE.md` §13 and §17.3.
