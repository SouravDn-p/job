# Application Log

Master index of every job applied to. **Newest first.** One row per application; full detail lives in each application's folder.

| Total | Draft | Active | Interviews | Offers | Closed |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 0 |

*Active = Applied · Screening · Task/Test · Interview · Final. Closed = Offer · Rejected · No response · Withdrawn. Draft = generated, not yet submitted.*

---

## Applications

| # | Applied | Company | Role | Location / Type | Source | Status | Updated | Folder |
|---|---|---|---|---|---|---|---|---|
| 1 | — | **WellDev** | Trainee Software Engineer | Dhaka, Bangladesh · Full-time permanent, hybrid | `recruitment.welldev.io` portal | `Draft` | 2026-07-25 | [`26-07-25_well-dev_Trainee-Software-Engineer`](26-07-25_well-dev_Trainee-Software-Engineer/) |

---

## Status vocabulary

| Status | Meaning |
|---|---|
| `Draft` | CV generated, not yet submitted |
| `Applied` | Submitted, awaiting response |
| `Screening` | Recruiter/HR screening call scheduled or done |
| `Task/Test` | Take-home assignment or coding test issued |
| `Interview` | Technical or panel interview scheduled or done |
| `Final` | Final-round / founder / culture interview |
| `Offer` | Offer received |
| `Rejected` | Rejected at any stage |
| `No response` | Ghosted — mark after ~4 weeks of silence |
| `Withdrawn` | I withdrew |

---

## Conventions

**Folder naming:** `YY-MM-DD_<company-slug>_<Role-Name>/`, inside `jobs/` — **date first**, so the folder list sorts chronologically and greps cleanly.

**Each application folder contains:**

| File | Purpose |
|---|---|
| `cv.html` | The exact CV sent, in HTML (rendered to PDF by my own HTML→CV builder). **Immutable once status is `Applied`** — if the CV is revised for a re-application, create a new dated folder rather than editing this one. Exactly one CV file per folder. |
| `profile-photo.png` | Copy of the headshot the CV references, kept locally so the folder renders standalone (only when a photo is used). |
| `job-description.md` | The JD archived verbatim. Postings get taken down; this is the only copy that will exist at interview time. |
| `notes.md` | Summary variant used, projects featured, keywords targeted, what was deliberately omitted, contact/portal/reference number, and a dated status timeline. |
| *(raw scrape, optional)* | If the posting was scraped from a JS-rendered page, the original HTML is kept alongside `job-description.md` rather than deleted. |

**Before an interview,** open the folder and read `notes.md` first — it records the story that was told, so the interview matches the CV.

**Keeping this file honest:** whenever a status changes, update the row here *and* the timeline in `notes.md`, and recompute the counts in the header table above.
