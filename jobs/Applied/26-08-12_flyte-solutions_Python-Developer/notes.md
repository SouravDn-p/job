# Flyte Solutions Ltd — Python Developer

**Priority tier:** **3 — On-site Bangladesh (Dhaka, Banani).** Stated directly in the posting — full-time, on-site at Morning Glory, Banani. No ambiguity here, unlike Exabyting the same day.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-12 |
| Applied | (blank until submitted) |
| Source | Pasted by Abdullah — format matches a LinkedIn or company careers listing |
| Location / type | Banani, Dhaka, Bangladesh · on-site, full-time |
| Deadline | Not stated |
| Posted | **UNKNOWN — cannot be established.** Doesn't match either of Flyte's two indexed SmartRecruiters postings; likely a third, separate requisition. Per `CLAUDE.md` § Deadline first, rule 6: **treated as escalated and unverified**, not fresh. |
| Reference / application ID | — |
| Contact | career@flytesolutions.com — subject "Application – Python Developer" |
| Salary discussed | Not stated by employer. **The application itself requires disclosing current salary, expected salary and notice period** — Abdullah must supply these; not something this workspace can generate. |

## Fit

| They ask | He has | Verdict |
|---|---|---|
| Bachelor's in CS/SE | B.Sc. CSE, IUBAT (§5.1) | ✅ |
| 3–5 years professional Python | **~1 year** (Softvence, Aug 2025–present) | ❌ **The largest gap on any application logged so far** |
| Python + strong OOP | Primary language, expert (§15) | ✅ Strong |
| FastAPI, Django, or Flask | Both Django (4 backends) and FastAPI (4 backends); no Flask, but the "or" is satisfied twice over | ✅ Strong |
| REST APIs & backend development | Core of every Softvence project (§4.1, §11) | ✅ Strong |
| PostgreSQL, MySQL, or SQL Server | PostgreSQL (primary) + MySQL; no SQL Server, but the "or" is satisfied | ✅ |
| Git, collaborative development | Branching strategies, PR workflows, GitHub Actions (§15) | ✅ |
| Redis | Cache, Celery broker, OTP store, channel layer — every project (§12, §15) | ✅ Strong |
| RabbitMQ | **Never used** — Celery is backed by Redis, not RabbitMQ, throughout the profile | ❌ Gap |
| Docker | Multi-stage builds, Compose, every project (§12) | ✅ Strong |
| Kubernetes | **Never used** — Docker Compose only, no orchestration layer | ❌ Gap — listed in both Required *and* Preferred, so this is the JD's second-loudest ask after years of experience |
| CI/CD | GitHub Actions, built on 8+ repos (§12) | ✅ Strong |
| Linux | Server administration, EC2/VPS operation (§12) | ✅ |
| Unit testing | Django `TestCase`, pytest, Vitest, migration-drift CI gating (§11) | ✅ |
| *Preferred:* Azure/AWS/GCP | AWS: EC2, IAM, SES, RDS, S3 (§12) | ✅ Exceeds |
| *Preferred:* AI/ML integration, LLMs | OpenAI (with per-request cost/token accounting), ElevenLabs, google-genai (§7.1, §7.2) | ✅ Genuine, non-ML-engineering integration work |
| *Preferred:* RAG | **Not in profile** — no retrieval-augmented-generation pipeline built | ❌ Not claimed |
| *Preferred:* Celery & background jobs | Celery + Celery Beat, isolated queue routing, on every project (§4.1, §8.1) | ✅ Strong |
| *Preferred:* Elasticsearch | **Not in profile** | ❌ Not claimed |
| *Preferred:* GraphQL | **Not in profile** — REST throughout | ❌ Not claimed |
| *Preferred:* Message queues | Redis-as-broker is the closest evidence; not a dedicated MQ (RabbitMQ/Kafka) | ⚠️ Partial, framed honestly |

## Knockouts

1. **3–5 years professional Python — the headline gap.** This is a harder bar than any BD posting
   logged so far (Bohubrihi asked 12–18 months, Exabyting asked 2+ years; this asks 3–5). Abdullah has
   ~1 year professional (Softvence, joined 16 Aug 2025) plus ~1 year of pre-employment self-directed
   Python/Django work (2024–2025, personal projects). The CV leans on the promotion signal and the
   density of delivery (eight platforms in eleven months) rather than raw tenure — but if their
   screening is a literal years-of-experience filter, **this is the single most likely rejection
   reason**, and Abdullah should know that going in.
2. **Kubernetes — asked twice** (once in the Required Technical Skills list, once again in
   Preferred as "Kubernetes & Container Orchestration"). Genuinely absent from the profile — Docker
   Compose only, no orchestration layer ever operated. Not claimed anywhere on the CV.
3. **RabbitMQ** — the profile's message-broker evidence is entirely Redis-backed Celery, never
   RabbitMQ. Not claimed.
4. **Elasticsearch, GraphQL, RAG** — all absent from the profile, all preferred-only (not required),
   none claimed. These are the least concerning gaps since they're explicitly "preferred," not
   required.
5. **Posting date/deadline unverifiable** — apply promptly regardless.
6. **The application itself requires current salary, expected salary and notice period** — this
   workspace has no record of Abdullah's current compensation and will not fabricate a figure.
   **Abdullah must supply these three values himself before the email can be sent.**

## CV decisions

- **Summary variant used:** §3.1 (General Python Backend Developer), adapted to lead with Python/OOP
  and the Django-or-FastAPI-or-Flask framing the JD itself uses, then REST APIs, then the databases,
  Redis, Docker and CI/CD line-up the JD lists as required Technical Skills, in roughly that order.
- **Projects featured:** **CHYR** (Django, multi-tenant SaaS, Celery, Redis, microservice-shaped
  domain boundaries) · **OCReels** (FastAPI, async, Redis, Celery + APScheduler) · **ProspectLead**
  (Django, OpenAI/LLM integration with cost accounting — direct evidence for the "AI/ML Integration"
  and "LLMs" preferred lines) · **ArchiCoPro** (FastAPI, RBAC, Celery, Redis).
- **Keywords targeted (JD's literal phrasing):** Python, object-oriented programming, FastAPI,
  Django, REST APIs, microservices, PostgreSQL, MySQL, Redis, Docker, Git, CI/CD, Linux, unit testing,
  AWS, AI/LLM integration, Celery.
- **Deliberately omitted — would be invention:** Kubernetes, RabbitMQ, Elasticsearch, GraphQL,
  Retrieval-Augmented Generation (RAG), SQL Server, Flask. None of these appear anywhere on the CV.
- **Weak spots:** the 3–5 years gate (Knockouts #1) and Kubernetes (Knockouts #2) are the two to be
  ready to address directly if he gets a screening call.

## Status timeline
- 2026-08-12 — Found
- 2026-08-12 — Draft (CV built and rendered; **not yet sendable** — the application email still needs
  current salary, expected salary and notice period supplied by Abdullah)
- 2026-08-13 — Application email drafted (`application-email.md`, main + short version). Still not
  sendable: current salary, expected salary and notice period remain `[ ]` placeholders. Per
  Abdullah's instruction the email names **no** gaps — Kubernetes, RabbitMQ, Elasticsearch, GraphQL
  and RAG go unmentioned, and the years-of-experience question is not raised. Nothing false is
  claimed; the gaps are simply not volunteered. Knockouts #1–#4 above still stand for a screening
  call.
- 2026-08-13 — **Applied.** Email sent to career@flytesolutions.com, subject "Application – Python
  Developer", with `Abdullah_Md_Jahid_Hassan_CV_Python_Developer.pdf` attached. Folder moved from
  `jobs/Findings/` to `jobs/Applied/`. Note: the archived `application-email.md` still shows `[ ]`
  for current salary, expected salary and notice period — Abdullah filled those in at send time and
  the figures are not recorded here.

## Interview prep
(filled in later)
