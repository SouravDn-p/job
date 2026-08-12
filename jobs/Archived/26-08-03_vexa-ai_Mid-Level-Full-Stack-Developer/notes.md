# Vexa AI — Mid-Level Full Stack Developer

## 🗄️ ARCHIVED 2026-08-04 — deadline expired

The BDJobs deadline had **already passed** when the listing was checked in a browser on 2026-08-04 —
resolving the unknown posting date recorded below. Never applied. Kept on record so this posting is
not surfaced again; if Vexa AI re-advertises with a fresh date it can be logged as a new job.

**Priority tier:** **1 — Remote, within Bangladesh.** Fully remote, "anywhere in Bangladesh". Tier 1
ranks local remote level with global remote, so this sits alongside the worldwide roles — and it
carries none of their timezone or payment friction.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-03 |
| Applied | — |
| Source | BD Tech Jobs → BDJobs |
| Location / type | Fully remote, Bangladesh · full-time |
| Deadline | Not stated |
| **Posted** | 🔴 **UNKNOWN** — no date on BD Tech Jobs (`/jobs/381`), none on the BDJobs detail page (`1500839`, JavaScript-rendered), none found via search on 2026-08-04. |
| **Admission test** | 🔴 **CANNOT BE RUN → treated as ESCALATED and unverified** (`CLAUDE.md` § Deadline first, rule 6). No deadline is recorded *and* no posting date could be found. **Open `bdjobs.com/h/details/1500839` in a browser and read both the "Application Deadline" and the "Published on" lines.** A live deadline admits it outright; if there is none and it is 31+ days old, this folder gets deleted. |
| Salary | 50,000 – 75,000 BDT |

## The honest assessment

**This is the easiest tier-1 role to actually get, and the weakest one on stack fit.** Both things
are true and both matter.

**What lines up (§8.1, §8.2, §12, §15):** React and Next.js — he built the entire Omnyvora frontend
on Next.js 16 / React 19 / TypeScript. PostgreSQL, Redis, Git, CI/CD, DevOps — all daily work.
**Multi-tenant systems** — CHYR is a multi-tenant B2B SaaS with business scoping and RBAC (§7.1).
**OpenAI and Claude** — OpenAI integrated with per-request cost and token accounting on ProspectLead
(§7.3), Claude Code in daily use (§11).

**What does not (be straight about this):** the backend here is **Node.js / Express / BullMQ**, and
he is a Python engineer. He has professional JavaScript/TypeScript, but his server-side production
work is Django, DRF and FastAPI — not Express. BullMQ is a Node job queue; his equivalent experience
is Celery, which is the same *idea* in a different runtime. Do not claim Node backend experience he
does not have (`CLAUDE.md` hard rule 1). Lead with the transferable architecture — queues, workers,
multi-tenancy, Redis — and be explicit that the Node runtime would be new.

**Pay:** 50,000–75,000 BDT is at or below his likely current level as a Senior Python Executive.
The remote element is the compensation. Worth checking the number against his current package before
spending effort.

## Knockouts

1. **"2+ years" and "mid level"** — he clears this, but the framing is below his title. Expect the
   same "why are you applying down?" question the WellDev application raised, and reuse that answer.
2. **Node.js backend** — if the interview probes Express/BullMQ depth, that is the failure mode.
3. Confirm "fully remote" is permanent, not a trial period.

## CV decisions

**File:** `cv.html` → `Abdullah_Md_Jahid_Hassan_CV_Mid_Level_Full_Stack_Developer.pdf` ·
**verified 2 pages** (page 1 97% full, page 2 80%), selectable text layer confirmed.
Headshot included (`profile-photo.png`, copied from `Assets/Profile Pictures/`) — Bangladesh market.

- **Summary variant used:** §3.4 (Full-Stack / Product Engineer), reordered to put **React / Next.js
  / TypeScript first** and the Python backend second. That inversion is deliberate: the frontend and
  the architecture are where he matches this posting, and the runtime is where he does not.
- **The Node.js problem, handled honestly.** Nothing on the CV claims Node, Express or BullMQ — the
  words do not appear. The summary says plainly that server-side work is Python (DRF, FastAPI) with
  Redis and Celery for queued jobs, and that **the queue and worker architecture is the transferable
  part**. That sentence is the whole pitch; do not let an interview drift past it.
- **Projects featured:** CHYR (**multi-tenant** — the posting names it explicitly) · ProspectLead
  (OpenAI with real cost accounting, plus he designed the UI) · Tundra (three-service estate).
  Omnyvora in Experience, led by the frontend bullet.
- **Keywords targeted:** React · Next.js · REST API · API integration · PostgreSQL · Redis ·
  Git · CI/CD · DevOps · OpenAI · Claude · **multi-tenant systems**.
- **Deliberately omitted:** Node.js, Express, BullMQ (not his). Electronics/IoT/Li-Fi. C#/Java.
- **Knockouts:** "2+ years / mid level" is below his title — expect the "why are you applying down?"
  question and reuse the WellDev answer. **Node.js backend is the failure mode** if the interview
  probes Express or BullMQ depth. Confirm "fully remote" is permanent, not a trial.
- **Weak spots / check first:** 50,000–75,000 BDT may be at or below his current package. Check the
  delta before spending time on this one — the remote element is the only compensation on offer.

## Status timeline
- 2026-08-03 — Found
- 2026-08-04 — Draft (CV built and rendered; not yet submitted)
- 2026-08-04 — **Archived, not applied.** BDJobs listing checked directly: the application deadline
  has expired. Folder moved `Findings/` → `Archived/`. **Do not surface this posting again.**
