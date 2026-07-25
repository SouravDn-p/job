# CV & Job Application Workspace

Personal workspace for **Abdullah Md Jahid Hassan** — Senior Python Executive, Softvence Agency.

Two jobs:
1. **Generate** a CV tailored to a specific job description, from a single exhaustive profile.
2. **Record** every application, so months later I can answer "which CV did they see?" before an interview.

---

## Layout

```
.
├── CLAUDE.md                      operating rules — auto-loaded by Claude Code every session
├── PROFILE.md                     ← the source of truth. Everything about me, in one file.
├── jobs/
│   ├── LOG.md                     master index of every application
│   └── YY-MM-DD_company_Role/     one folder per application — date first, so it sorts
│       ├── cv.html                the CV that was actually sent (immutable once applied)
│       ├── job-description.md     the JD, archived verbatim
│       └── notes.md               tailoring decisions + status timeline
├── .claude/skills/cv-builder/     the /cv-builder procedure
├── db.sqlite3                     legacy portfolio DB (already extracted into PROFILE.md §14)
└── my-projects/                   Omnyvora backend + frontend source (analysed in PROFILE.md §8)
```

---

## Usage

**Build a CV for a job:**

```
/cv-builder
```

then paste the job description. It reads `PROFILE.md`, tailors a CV to the JD's vocabulary, writes it to a new dated folder under `jobs/`, and adds a row to `jobs/LOG.md`.

**Update a status** — just say it in plain language:

> *"Got a screening call from Acme."*
> *"Rejected by Tundra."*

Both `LOG.md` and that application's `notes.md` get updated.

**Before an interview:**

> *"Pull up what I sent Acme."*

---

## Why one big PROFILE.md

It's ~930 lines, which fits in a single file read. Splitting it into topic files would mean guessing which ones to open — and missing one silently drops real evidence from a CV. Split it only past ~2000 lines. Reasoning is at the bottom of `CLAUDE.md`.

## What must never leave this folder

Client source code (NDA), internal client identifiers, and any credential — server IPs, `.pem` keys, IAM access keys, database passwords, API keys. See `PROFILE.md` §13 and §17.3.
