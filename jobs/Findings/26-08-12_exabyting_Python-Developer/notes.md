# Exabyting — Python Developer

**Priority tier:** **3 — On-site Bangladesh (Dhaka, Mohakhali DOHS).** Confirmed via Glassdoor/LinkedIn/Crunchbase — Exabyting is a real Dhaka-based software company (~50 staff, founded 2018). The posting itself states no location, but the perk list (dormitory, transport support, mobile allowance for family) is only coherent for an on-site Bangladesh employer, and this is independently corroborated by the company's verified office address and Glassdoor reviews.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-12 |
| Applied | (blank until submitted) |
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

## Interview prep
(filled in later)
