# Exabyting — Python Developer

**Priority tier:** **3 — On-site Bangladesh (Dhaka, Mohakhali DOHS).** Confirmed via Glassdoor/LinkedIn/Crunchbase — Exabyting is a real Dhaka-based software company (~50 staff, founded 2018). The posting itself states no location, but the perk list (dormitory, transport support, mobile allowance for family) is only coherent for an on-site Bangladesh employer, and this is independently corroborated by the company's verified office address and Glassdoor reviews.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-12 |
| Applied | 2026-08-13 (via career-life.exabyting.com/candidate-form) |
| Source | LinkedIn (pasted directly by Abdullah) |
| Location / type | Dhaka, Bangladesh (Mohakhali DOHS) · on-site, inferred from company address + perks, not stated in posting |
| Deadline | Not stated |
| Posted | **UNKNOWN — cannot be established.** Apply link is a JS-rendered form with no date. Per `CLAUDE.md` § Deadline first, rule 6: **treated as escalated and unverified**, not fresh. Apply promptly rather than waiting, since age cannot be bounded. |
| Reference / application ID | — |
| Contact | career-life.exabyting.com/candidate-form |
| Salary discussed | Not stated |

## Fit

| They ask | He has | Verdict |
|---|---|---|
| Django expertise, proven hands-on | Core skill — four production DRF backends at Softvence (§4.1), plus `django_templet` starter | ✅ Strong |
| Backend-focused software development | Sole/lead backend developer on eight Softvence platforms + Omnyvora | ✅ Strong |
| Python or Golang | Python is the primary language throughout; no Golang in profile — the "or" is satisfied by Python | ✅ (Python only) |
| FastAPI, highly preferred | Four production FastAPI backends: OCReels, ArchiCoPro, fitness platform, Outdoorda (§7.2, §7.6, §7.7, §7.8) | ✅ Strong |
| Backend ecosystems & SE best practices | Layered `models→selectors→services→serializers→views`, migration-drift CI gating, testing (Django TestCase, pytest, Vitest), code-quality gates (§11) | ✅ |
| Asynchronous & event-driven architectures | Celery + Celery Beat with isolated queue routing, Django Channels/WebSockets, idempotent webhook processing (Stripe, n8n), async FastAPI with asyncpg/aiomysql | ✅ Strong |
| Practical NoSQL experience | **Redis** — used as cache, Celery broker, OTP store and WebSocket channel layer on every production project. Redis is a genuine NoSQL (key-value) store; honestly claimable. **No document-store (MongoDB) experience** — see gap below | ⚠️ Partial, honestly framed |
| Cloud platform exposure (plus) | AWS: EC2 (multi-region), IAM, SES, RDS, S3 (§12) | ✅ Exceeds |

## Knockouts

1. **"Experience required 2+ years" — the one real gap.** Professional Python/Django experience is
   ~1 year (Softvence, joined 16 Aug 2025). Before that: a PHP/MySQL internship (Feb–Jul 2024, not
   Python) and self-directed Python/Django learning (2024–2025, personal projects, not employment).
   The CV cannot claim "2+ years professional" without inventing — it doesn't. What it does instead is
   lean on the promotion signal (Junior → Senior in 11 months) as evidence of density over duration.
   **Flag this to Abdullah before he applies** — if the application form has a hard "years of
   experience" gate, this may not clear it.
2. **NoSQL is Redis, not a document store.** The JD says "NoSQL databases" generically, not MongoDB by
   name, so Redis is a legitimate, honest answer — but if an interviewer means MongoDB/Cassandra-style
   experience specifically, that's not there. Be straight about it if asked.
3. **Posting age/deadline unverifiable** — apply promptly; do not treat the absence of a deadline as
   safety margin.
4. **On-site, Mohakhali DOHS** — a few minutes from the current Softvence office (Mohakhali C/A), so
   commute is not a practical blocker, but this is a lateral/same-area on-site move, not a step up in
   work arrangement.

## CV decisions

- **Summary variant used:** §3.1 (General Python Backend Developer), adapted to open with Django
  (the JD's literal first and loudest requirement) rather than a generic backend framing, and to
  name FastAPI, async/event-driven architecture, NoSQL (Redis) and AWS in JD order.
- **Projects featured:** **CHYR** (Django REST, multi-tenant SaaS, Celery-driven billing, webhook
  idempotency — strongest Django + event-driven combination) · **OCReels** (FastAPI, fully async
  architecture, Redis, Celery + APScheduler — strongest FastAPI + async + NoSQL combination) ·
  **ArchiCoPro** (FastAPI, RBAC, Celery, Redis — reinforces FastAPI + backend-ecosystem breadth).
  Tail line covers ProspectLead, Tundra, LookUp and `django_templet` for width without diluting focus.
- **Keywords targeted (JD's literal phrasing):** Django, FastAPI, backend-focused software
  development, Python, asynchronous and event-driven architectures, NoSQL, AWS/cloud platform,
  REST API.
- **Deliberately omitted:** Golang (not in profile, not needed — JD's "or" is satisfied by Python) ·
  frontend/React detail (present in the profile but not JD-relevant here, kept to one Omnyvora line) ·
  MongoDB or any document-database claim (never used — would be invention). Internal client folder
  names avoided throughout per the NDA rule.
- **Weak spots:** the 2+ years gate (see Knockouts #1) and NoSQL being Redis rather than a document
  store (Knockouts #2) — prepare to address both directly if asked.

## Status timeline
- 2026-08-12 — Found
- 2026-08-12 — Draft (CV built and rendered)
- 2026-08-13 — **Applied.** Submitted through the Exabyting candidate form
  (`career-life.exabyting.com/candidate-form`). Folder moved `Findings/` → `Applied/`.

## Application form — free-text answers submitted

The candidate form asked open questions beyond the CV. Answers written on 2026-08-13, all traced to
`PROFILE.md`; recorded here because these are what an interviewer will follow up on.

**Q1 — "Why are you considering a change right now?"**

> I have spent the past year at Softvence Agency building client backends, eight of them in eleven
> months, which is how I moved from Junior Python Developer to Senior Python Executive. It has been a
> fast way to learn, but agency work follows a pattern: you design a system, ship it, hand it over,
> and start the next one. I want to stay with a product long enough to see it live in production,
> understand how it behaves under real usage, and keep improving it instead of leaving at handover.
>
> Exabyting stands out because the work described in the posting is what I already do every day:
> Django and FastAPI, asynchronous and event-driven services, Redis, Docker and AWS. I am also
> looking for a team with more backend engineers around me. On most of my projects I have been the
> only backend developer, and I know I grow faster when someone is reviewing my design decisions.
> That combination is what makes this the right time to move.

*Angle taken:* no criticism of Softvence (the handover point is framed as a property of the agency
model, not a complaint); the Junior → Senior promotion is placed early so it lands before anyone does
the date arithmetic against the JD's "2+ years" (Knockout #1).

**Q2 — "Describe one system or feature you personally built recently in 3 lines."**

> I built the credit-billing engine for ProspectLead, an AI lead-generation SaaS on Django REST,
> where I was the lead backend developer.
> Credits are reserved the moment a job is dispatched so concurrent requests cannot overspend, then
> finalised when the n8n automation posts back on an authenticated webhook, with the difference
> refunded automatically if fewer leads are returned than were paid for.
> Every movement is written to an append-only ledger with a running balance, Stripe webhooks are
> processed idempotently against a unique event ID, and a Celery Beat watchdog auto-fails and refunds
> any job that has no callback after six hours.

*Why this project:* the JD makes Django the hard requirement and FastAPI only "preferred", so the
Django answer leads. It also covers their asynchronous/event-driven, Redis and cloud bullets in one
example. Source: `PROFILE.md` §7.3. A FastAPI alternative (OCReels async architecture, §7.2) was
prepared but not used.

## Interview prep

**Follow-ups the submitted answers invite — prepare these first:**

1. **"What if the n8n callback arrives twice?"** — the idempotency key on the webhook event table
   plus the reserved-state check on the `LeadGenerationRequest` state machine. Q2 points an
   interviewer straight here.
2. **"You said 2+ years; you have about one."** — do not pad. ~1 year professional Python/Django at
   Softvence (from 16 Aug 2025), preceded by a PHP/MySQL internship (Feb–Jul 2024) and ~1.5 years of
   self-directed Python work. The promotion in eleven months is the counterweight. See Knockout #1.
3. **"Which NoSQL databases have you used?"** — Redis, genuinely and in production (cache, Celery
   broker, OTP store, Channels layer). No MongoDB or other document store. Say so plainly. See
   Knockout #2.
4. **"Why leave after only a year?"** — consistent with the Q1 answer: wanting to own a product past
   handover, and wanting backend peers to review design decisions. Avoid any framing that reads as
   dissatisfaction with pay or management.
