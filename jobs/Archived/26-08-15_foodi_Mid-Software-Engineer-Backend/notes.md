# Foodi — Mid Software Engineer, Backend (Python / FastAPI)

> # 🔴 ARCHIVED — DECIDED AGAINST. NEVER APPLIED.
>
> **Archived 2026-08-15, the same day it was found.** Abdullah decided against it:
> **the role expects too broad a skill span — DevOps, microservices and similar —
> stacked on top of the backend work.** No application was ever submitted.
>
> **This did not die of expiry.** No deadline was stated, the posting was still live,
> and a finished two-page CV was already built and sitting in this folder. The CV
> remains here as a record of what would have been sent.
>
> **Do not surface this posting again.** If Foodi reposts with a fresh posting date
> that is a *new* job — new folder, new row, new `id` — but the reason below still
> applies and should be checked against the new posting before anything is built.
>
> **The generalisable filter.** The stack match was the strongest in the whole log,
> and it still was not enough, because fit is not only about the stack — it is about
> how many *different* jobs a single role is asking one person to do. **From now on,
> at the finding stage, flag any backend posting that also loads DevOps, infrastructure
> ownership, microservice architecture or similar breadth onto the same seat, and say
> so out loud when it rules something out.** Note the tension to watch for: Abdullah's
> profile *evidences* deep DevOps and architecture work, so postings like this will
> keep scoring as excellent matches on paper. Matching the evidence is not the same as
> wanting the job.

**Priority tier:** 3 — on-site, Bangladesh. The posting does not state work type, and
per Abdullah's standing instruction a Bangladeshi circular that says nothing defaults
to on-site. Foodi's office is Baridhara J Block, Dhaka. **If it turns out to be remote
this is a tier 1 and should be treated as such** — worth asking on the form or at
screening.

**This is the best stack match logged to date.** Every hard requirement except
SQLAlchemy and the years-of-experience band is directly evidenced in `PROFILE.md`,
and the FastAPI half of the profile — which most postings in this log ignored — is
exactly what this JD leads with.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-15 |
| Applied | *(blank — not yet submitted)* |
| Source | LinkedIn |
| Location / type | Dhaka (Baridhara) — assumed on-site; not stated in the posting |
| Posted | **Unknown — could not be established** |
| Deadline | **Not stated** |
| Freshness verdict | **Escalated + unverified** (`CLAUDE.md` rule 6) — apply early |
| Apply method | Google Form (link in `job-description.md`) |
| Reference / application ID | — |
| Contact | — |
| Salary discussed | Not stated in the posting |

**Company verification (2026-08-15).** Foodi is real and established: Bangladeshi
food/grocery delivery platform, HQ Baridhara J Block Dhaka, 201–500 employees, founded
2021, a concern of US-Bangla. Its LinkedIn page confirms it has been advertising "Mid
and Senior Backend Software Engineers (.NET Core and Python/FastAPI)", which
corroborates the pasted JD. Legitimacy gate: **pass**.

**Why an HRIS at a food-delivery company is plausible** — Foodi runs a large rider and
merchant workforce, so an internal HRIS handling attendance, leave and employee records
is a real internal-platform need, not a red flag. Worth saying at interview that this
was understood.

## CV decisions

- **Summary variant used:** §3.1 (General Python Backend Developer), rewritten
  FastAPI-first. §3.1 was the closest base, but its Django-led ordering was inverted —
  this JD leads with FastAPI, so the CV does too. The promotion signal was pulled in
  from §3.2/§3.6 because the years-of-experience gap needs a counterweight.
- **Projects featured (4), FastAPI-first:**
  - **OCReels** (§7.2) — the strongest pure FastAPI/async/Pydantic evidence. Its
    creator application → review → approval state machine was framed as the same
    review-and-approve shape an HR workflow runs on. Honest framing, not a domain claim.
  - **ArchiCoPro** (§7.6) — FastAPI + feature-level RBAC with per-role grants and
    per-user overrides. **This is the closest thing in the profile to an HRIS
    permission model** (who may see whose records), and it is said so explicitly.
  - **CHYR** (§7.1) — multi-tenant SaaS with organisation/role-scoped member profiles
    and an atomic invitation flow. The employee-onboarding analogue.
  - **ProspectLead** (§7.3) — background jobs done properly: Celery Beat watchdog,
    authenticated callback contract, append-only ledger.
- **Keywords targeted (literal phrases lifted from the JD):** "backend services and
  REST APIs using FastAPI and Python", "own well-defined modules end to end",
  "efficient database queries", "data model design in PostgreSQL", "code reviews,
  testing, and debugging", "collaborate with frontend, QA and product", "API
  integrations and background jobs", "Pydantic", "async", "REST API design",
  "JWT/OAuth2", "Docker, Git, pytest", "Redis / Celery", "SaaS".
- **Assets used:** layout from `Assets/CV Templates/cv_temp_1.png` (single column,
  left-aligned rules, photo top-right) — the same skeleton as the Exabyting and Flyte
  builds. Headshot from `Assets/Profile Pictures/` included; a photo is normal for the
  Bangladesh market. Copied into the folder as `profile-photo.png`.
- **Formatting:** body copy justified per the house rule added to `CLAUDE.md`
  § Justify the body copy on 2026-08-15. Line-height taken to 1.21 and section spacing
  to 8px to hold two pages — **type size was not reduced**, it stayed at 9pt.

### Deliberately omitted — and why

- **SQLAlchemy.** The JD asks for "working knowledge of SQLAlchemy". Abdullah has none.
  His async ORM is **Tortoise ORM 0.25 + Aerich**, which is named plainly on the CV
  instead. No substitution and no vague "ORM experience" phrasing that would imply it.
  **This is the single most likely screening question.**
- **gRPC / Protocol Buffers.** Nice-to-have in the JD, absent from the profile.
  Appears nowhere on the CV, not even softened.
- **HR / Payroll domain.** No experience. SaaS and multi-tenant org/role/invitation
  modelling are offered as the honest adjacency and described as exactly that.
- **Years of experience.** The JD asks 2–4 years professional; Abdullah has ~1 year
  (Softvence from Aug 2025) plus a 6-month internship in 2024. **No total is stated
  anywhere on the CV** — the dates are printed exactly and the reader does the maths.
  The counterweight offered is real: eight production backends and a promotion inside
  eleven months.
- Cut for space (all present in earlier drafts): the reusable `django_templet` starter
  bullet, OpenAI cost accounting, the dual payment-provider abstraction, self-service
  SMTP/backup ops, and the OCReels RBAC/Locust/Sentry bullet.

### Knockouts

| Gate | Status |
|---|---|
| Work authorisation | Fine — Bangladeshi national applying in Bangladesh |
| Location | Assumed on-site Dhaka; Uttara 10 → Baridhara is a normal commute |
| Degree | B.Sc. CSE, IUBAT — clears anything likely to be asked |
| Named certification | None demanded |
| **Years of experience** | **~1 yr professional vs 2–4 asked. The real gate.** |
| NOC | Not applicable — private sector |

**The Google Form could not be read in advance** (HTTP 401 — it needs a signed-in
Google account). So its questions are unknown. Expect the usual: years of experience,
current and expected salary, notice period, and a CV upload. **Have those three
figures decided before opening the form** — the same gap that held up the Flyte
application.

### Weak spots — prepare answers for these

1. **"Have you used SQLAlchemy?"** The honest answer is no, with the strong follow-up:
   four production services on Tortoise ORM — an async ORM with the same
   session/model/migration concepts — plus Django ORM depth, and Aerich migrations
   which map onto Alembic. Worth doing a small SQLAlchemy + Alembic exercise before any
   interview so the answer is "not in production, but I've built with it".
2. **"You have about a year, we asked for two to four."** Answer with delivery volume
   and the promotion, not with a stretched date.
3. **"Any HR or payroll domain experience?"** No. Pivot to the permission and
   record-privacy modelling on ArchiCoPro, and the org/role/invitation modelling on
   CHYR, which is the machinery an HRIS is built out of.
4. **gRPC** — no exposure. Say so plainly; it is a nice-to-have, not a requirement.
5. **Attendance and leave** specifically — no prior module. Closest genuine analogues
   are state machines with audit trails (moderation, creator review, subscription
   lifecycle), which is what leave-approval is.

## Status timeline

- 2026-08-15 — Found. Logged from a LinkedIn posting Abdullah had already closed;
  company verified by web search, posting date unverifiable, no deadline stated →
  escalated.
- 2026-08-15 — Draft. CV built and rendered: 2 pages, page 1 97.8% full, page 2 89.0%,
  text layer verified, no forbidden strings. Not yet submitted.
- 2026-08-15 — **Archived. Decided against; never applied.** Reason: the role expects
  too broad a skill span — DevOps, microservices and similar — on top of the backend
  work. The deadline was not a factor; no deadline was stated and the posting was
  still live. Folder moved `Findings/` → `Archived/`, CSV row 15 updated to `Archived`.

## Interview prep

*Not applicable — no application was ever submitted.*
