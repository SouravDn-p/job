# jobs/ — how this folder works

Three folders and one log. Nothing else lives at this level.

```
jobs/
├── jobs_log.csv                            ← THE log. Every job, found or applied. One row each.
├── Findings/                               jobs found, not yet applied to
│   └── YY-MM-DD_<company-slug>_<Role-Name>/
├── Applied/                                jobs actually applied to
│   └── YY-MM-DD_<company-slug>_<Role-Name>/
└── Archived/                               dead ends — kept so they are never surfaced again
    └── YY-MM-DD_<company-slug>_<Role-Name>/
```

**One job = one folder.** Never two jobs in a folder, never one job split across two.

**A folder moves, it is never copied.** `Findings/` → `Applied/` on the day the application is
submitted, or `Findings/` → `Archived/` when the job dies before an application goes out. The folder
name does not change when it moves — the date in the name is the date the job was found, and that
stays true. Update `folder_local_location` and `status` in the CSV in the same edit. **A job must
never exist in two of these folders at once.**

---

## `Archived/` — the do-not-surface list

A job goes here when it is **dead before an application was ever sent**: the deadline expired while
it sat in `Findings/`, a knockout turned out to be genuinely blocking, or he decided against it.
Status `Archived`. It never moves to `Applied/`.

**Its whole purpose is negative memory.** These rows exist so the same posting is not found,
researched and pitched all over again next month. So:

- **When searching for jobs, read `Archived/` first** and skip anything already there. An archived
  job re-surfaced as a new find is a wasted day and the failure this folder exists to prevent.
- **The `notes.md` must say *why* it died**, in a banner at the top and a dated timeline entry.
  "Expired" and "blocked by an NOC requirement" lead to different future behaviour — the first means
  *catch the repost*, the second means *never pitch this class of job again*.
- **A repost is a new job.** If the employer re-advertises with a fresh posting date, that is a new
  folder and a new row with a new `id`. Do not resurrect the archived one.
- **Never delete an archived folder** to tidy up. An empty `Archived/` is a workspace that has
  forgotten what it already ruled out.

Distinguish this from the postings that **never get a row at all** (see below): those were rejected
at the *finding* stage, before a folder existed. `Archived/` is for jobs that were logged, researched
and often had a CV built — real sunk effort worth keeping.

---

## Folder naming

`YY-MM-DD_<company-slug>_<Role-Name>/` — **date first**, so the folder list sorts chronologically
and greps cleanly. Company slug lowercase-hyphenated (`well-dev`), role in `Title-Case-Hyphens`
(`Trainee-Software-Engineer`).

The date is **the day the job was found and logged**, in both folders.

---

## What goes in a `Findings/` folder

The job exists; nothing has been sent. Minimum:

| File | Purpose |
|---|---|
| `job-description.md` | The JD archived verbatim, with the standard header (source, **posted date**, archived date, deadline, URL). Postings get taken down; this is the only copy that will exist later. **`**Posted:** YYYY-MM-DD` is mandatory** — the freshness gate cannot be re-applied without it. |
| `notes.md` | Why this job is worth applying to: which **priority tier** it hits (see `CLAUDE.md` § Job-search preferences), the **posting date and age in days**, the knockouts spotted, the deadline, and a dated timeline starting at `Found`. |
| *(raw scrape, optional)* | If the posting was scraped from a JS-rendered page, keep the original HTML alongside `job-description.md`. |
| `cv.html` + PDF *(optional)* | Only if a CV was built ahead of applying — status `Draft`. |

## What goes in an `Applied/` folder

Everything above, plus the documents that were actually sent:

| File | Purpose |
|---|---|
| `cv.html` | The exact CV sent, in HTML (rendered to PDF by `tools/html_2_pdf`). **Immutable once status is `Applied`** — a revised CV for a re-application means a new dated folder, not an edit. **Exactly one CV file per folder** — never a `cv.md` beside a `cv.html`. |
| `Abdullah_Md_Jahid_Hassan_CV_<Role>.pdf` | The rendered, recruiter-facing PDF. This is the file that gets uploaded. Immutable once `Applied`, same rule. |
| `profile-photo.png` | Copy of the headshot the CV references, so the folder renders standalone (only when a photo is used). |
| `job-description.md` | As above, carried over from `Findings/`. |
| `notes.md` | Summary variant used, projects featured, keywords targeted, what was deliberately omitted, contact / portal / reference number, and the dated status timeline. |
| `preparation/` | Interview and exam prep, built by `prompts/preparation.md`. One subfolder per hiring stage. |

**Before an interview, read `notes.md` first** — it records the story that was told, so the
interview matches the CV they read.

---

## The log — `jobs_log.csv`

One row per job, in **both** folders. Newest row appended at the bottom; `id` increments and is
never reused.

**What never gets a row:** a posting whose **stated deadline has passed**; a posting with **no stated
deadline that is more than 30 days old**; one that can't be verified as real; or one that isn't a
genuine fit against `PROFILE.md`. Stale, expired and near-miss listings are worth *mentioning* in the
reply — they show the market exists — but they never become a `Found` row and never count toward a
requested number. See `CLAUDE.md` § A number I give you is a target, not a quota, and § Deadline
first, then the 30-day window.

**Deadline outranks age.** Check the deadline first. If one is stated and still in the future, the
job is in — a live deadline admits a 60-day-old posting. **The 30-day age filter only applies when no
deadline is stated.** Record both dates in the `job-description.md` header and the `notes.md`
Application table, because neither test can be re-run later without them.

**Ageing out.** For undated postings, age is measured from the posting date to **today**, not to the
day it was found — so a row can pass when logged and fail a fortnight later while still sitting in
`Findings/`. Re-check before building a CV for anything that has been waiting. When asked to audit
the folder, **move what has closed or aged out to `Archived/`** rather than deleting it — a job that
was logged and researched is worth keeping as negative memory. (A posting rejected at the *finding*
stage, before a folder ever existed, still gets no row at all.) Undated postings between **day 11 and
day 30 are escalated**: still valid, but applied to ahead of fresher roles of the same tier.

| Column | Meaning |
|---|---|
| `id` | Sequential integer, never reused. |
| `date` | `YYYY-MM-DD`. Date **found** for `Findings/` rows; date **applied** for `Applied/` rows. |
| `title` | The role title exactly as posted. |
| `type` | `Remote` · `Hybrid` · `On-site` · `Government` — see priority tiers below. |
| `location` | City/country, or `Global` / `Bangladesh` for remote roles. |
| `priority_tier` | `1`, `2` or `3` — from `CLAUDE.md` § Job-search preferences. Filled on every row. |
| `short_description` | One or two sentences: what the role is, and the one thing that decides whether it is worth applying to. |
| `company` | Company name as it should be spoken. |
| `role` | Normalised role (`Backend Engineer`, `Python Developer`) — this is what gets grepped, where `title` is what was posted. |
| `source` | Where it was found: LinkedIn · BDJobs · company site · referral · recruiter · portal URL. |
| `status` | From the vocabulary below. Exact strings only. |
| `updated` | `YYYY-MM-DD` of the last status change. |
| `folder_local_location` | Repo-relative path, forward slashes: `jobs/Findings/…` or `jobs/Applied/…`. |

**CSV rules:** any field containing a comma is wrapped in double quotes. No trailing blank
columns. Dates are always `YYYY-MM-DD` — never `26/07/24`, which is unreadable months later.

### Status vocabulary — use these exact strings

| Status | Meaning | Folder |
|---|---|---|
| `Found` | Logged, nothing built yet | `Findings/` |
| `Draft` | CV generated, not yet submitted | `Findings/` |
| `Applied` | Submitted, awaiting response | `Applied/` |
| `Screening` | Recruiter/HR screening call scheduled or done | `Applied/` |
| `Task/Test` | Take-home assignment, MCQ or coding test issued or sat | `Applied/` |
| `Interview` | Technical or panel interview scheduled or done | `Applied/` |
| `Final` | Final-round / founder / culture interview | `Applied/` |
| `Offer` | Offer received | `Applied/` |
| `Rejected` | Rejected at any stage | `Applied/` |
| `No response` | Ghosted — mark after ~4 weeks of silence | `Applied/` |
| `Withdrawn` | Withdrew after applying | `Applied/` |
| `Archived` | **Died before any application was sent** — deadline expired while it sat in `Findings/`, a knockout proved blocking, or he decided against it. Kept as negative memory: never surface this posting again. | `Archived/` |

**Keeping this honest:** whenever a status changes, update the CSV row (`status` **and** `updated`)
*and* the timeline in that folder's `notes.md`, in the same edit. The CSV is the index; the notes
are the record. If they disagree, the notes win and the CSV gets corrected.
