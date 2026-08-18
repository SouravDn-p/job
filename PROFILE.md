# MASTER PROFILE — Abdullah Md Jahid Hassan

> **Purpose of this file.** This is the single source of truth about me for AI agents that build tailored CVs/résumés against a specific job description. It is deliberately exhaustive — every job, project, model, service, tool, and architectural decision I have shipped is recorded here so the agent never has to guess or invent.
>
> **Last full rebuild:** 25 July 2026 — compiled by reading the local portfolio database, every office repository in `C:\Users\abdul_m1\Softvence\Projects`, both Omnyvora repositories (backend + frontend, including source code, models, services, docs and git history), and all 27 public repositories on my personal GitHub via the GitHub API.

---

## 0. HOW THE AI AGENT SHOULD USE THIS FILE

You are acting as **a senior HR manager and professional CV writer**. Your job is to produce an ATS-friendly CV for one specific job description.

**Rules of engagement:**

1. **Never invent.** Everything you write must trace to a line in this file. If the JD asks for something not here, leave it out — do not fabricate.
2. **Mirror the JD's vocabulary.** If the JD says "REST APIs", write "REST APIs" (not "RESTful services"). If it says "asynchronous task processing", use that phrase over "background jobs". ATS keyword parsers match literally. The **Keyword Bank (§16)** lists every term I can legitimately claim, grouped so you can pull the ones the JD uses.
3. **Pick, don't dump.** §7–§12 contain far more projects than fit a CV. Select 3–5 that best match the JD, using the "Best for JDs about…" tag on each project. **§9.0 is a dated index of all 27 personal projects** — use it to sort by recency and to supply the start/end dates recruiters expect.
4. **Use the bullet banks.** Each role and project has pre-written, quantified, achievement-oriented bullets in the exact register a recruiter expects. Re-order and re-word them to match the JD; do not weaken them into task lists.
5. **Pick the right summary.** §3 has several pre-written professional summaries targeted at different job families. Adapt the closest one.
6. **Respect confidentiality (§13).** Client work at Softvence is under NDA. Describe *what I built and with what*, never paste client source code, credentials, server IPs, or internal client identifiers. Live product URLs listed as public are safe to cite.
7. **Seniority framing.** I am currently a **Senior Python Executive** (promoted from Junior Python Developer). Frame me as a mid-level backend engineer who owns systems end-to-end — architecture, code, containerisation, CI/CD, deployment — not as a junior who takes tickets.
8. **Verify the flagged items** in §17 before printing them (there is one CGPA discrepancy between two sources).

---

## 1. IDENTITY & CONTACT

| Field | Value |
|---|---|
| **Full name** | Abdullah Md Jahid Hassan |
| **Preferred professional title** | Python Backend Developer / Backend Software Engineer |
| **Current job title** | Senior Python Executive — Softvence Agency |
| **Email** | abdullahmdjahidhassan@gmail.com |
| **Phone** | +880 1756 254873 |
| **Location** | Uttara 10, Dhaka, Bangladesh |
| **Nationality / work base** | Bangladesh (Dhaka) — experienced working with US, EU, Middle East and Australian clients remotely |
| **LinkedIn** | https://www.linkedin.com/in/abdullahmdjahidhassan/ |
| **GitHub (personal)** | https://github.com/abdullah-md-jahid-hassan |
| **GitHub (employer account)** | https://github.com/am-jahid-hassan — mandated by employer security policy; all work there is in private organisation repos |
| **GitHub (own organisation)** | https://github.com/orgs/omnyvora/repositories |
| **Portfolio site** | ~~https://amjh.space~~ — 🔴 **DOMAIN EXPIRED (as of 25 Jul 2026). Do not print on a CV.** A replacement domain is to be purchased; see §17.5 |
| **Legacy portfolio** | https://abdullahmdjahidhassan.pythonanywhere.com — ⚠️ still resolves, but the content is **~1 year stale** (no Softvence client work, no Omnyvora, no FastAPI/AWS/CI-CD). Cite only if a JD demands a live portfolio link, and expect it to undersell me. See §17.5 |
| **Spoken languages** | Bangla (native), English (professional), Hindi (conversational) |
| **Hobbies / interests** | Problem-solving, electronics & robotics, crafting, sketching, public speaking |

**GitHub bio (current):** *"Software Engineer | Python-Django Backend Developer | Fast Learner | Passionate about building scalable backend systems and real-world solutions."*

---

## 2. CAREER FLOW — CHRONOLOGICAL NARRATIVE

This is the story arc. Use it to decide *how* to frame me, not as CV copy.

```
2014 – 2017   SSC (Science) — Ibn Taymiyyah School and College
2017 – 2019   HSC (Science) — Dhaka Udyan Government College
2020 – 2024   B.Sc. in Computer Science & Engineering — IUBAT
              ├─ Thesis: Parallel Data Transmission in Li-Fi using RGB Light (2023)
              ├─ Practicum: ISP Management System (PHP/MySQL) (2024)
              └─ Formal SDLC training: requirement analysis, DFDs, ERDs,
                 activity/swimlane diagrams, cost estimation, feasibility matrices
2024 Feb–Jul  Internship — Cyber Hundred (on-site, Dhaka)
              └─ PHP/MySQL/Bootstrap full-stack web work + project documentation
2024 – 2025   Self-directed transition from PHP to Python/Django.
              Built ~15 personal projects (CLI tools, Django apps, IoT/Arduino,
              a dynamic Django portfolio CMS) to build depth.
              Certified: Python-Django by EDGE (Jul 2025)
2025 Aug 16   Joined Softvence Agency as Junior Python Developer
2025 – 2026   Rapid growth into full ownership of client backends:
              Django REST + FastAPI, Docker, CI/CD, AWS/Hostinger deployment,
              Stripe/Tap payments, Celery, Redis, PostgreSQL, third-party
              integrations (ElevenLabs, Twilio, Cal.com, OpenAI, n8n, Firebase)
2026 Jun      Founded Omnyvora — my own organisation/product company.
              Sole architect, backend dev, frontend dev and UI/UX designer.
2026 Jul      Promoted to Senior Python Executive at Softvence Agency
```

**The one-paragraph version:**
I started as a CSE graduate with a strong software-engineering-process foundation and a PHP/MySQL full-stack internship. Over 2024–2025 I taught myself Python and Django to a production standard, then joined Softvence Agency in August 2025. Inside eleven months there I went from junior to **Senior Python Executive**, owning eight client backends end-to-end — designing the data model, writing the API, containerising it, wiring the GitHub Actions CI/CD pipeline, and deploying and operating it on AWS EC2 / Hostinger VPS myself. In parallel I founded **Omnyvora**, where I am the sole engineer across a Django REST modular monolith, a Next.js 16 / React 19 frontend, and the entire design system — proving I can carry a product from a blank Figma file to a running production stack alone.

---

## 3. PROFESSIONAL SUMMARIES (pick + adapt one)

### 3.1 — General Python Backend Developer
> Python backend developer with 2+ years of hands-on experience building and operating production REST APIs with Django, Django REST Framework and FastAPI. Currently Senior Python Executive at Softvence Agency, where I have delivered eight client backends end-to-end — data modelling, API design, Dockerisation, GitHub Actions CI/CD, and deployment to AWS EC2 and VPS infrastructure. Experienced with PostgreSQL, Redis, Celery, JWT authentication, Stripe payment integration, and third-party API integration (OpenAI, ElevenLabs, Twilio, Cal.com, Firebase, n8n). Committed to clean, production-grade, industry-standard code and to owning a system from architecture through to live operation.

### 3.2 — Senior / Lead-leaning Backend Role
> Backend engineer who owns systems end-to-end. Promoted to Senior Python Executive at Softvence Agency within eleven months for delivering eight client backends, several single-handedly, — from database schema and service-layer architecture through Docker containerisation, GitHub Actions CI/CD, and production deployment on AWS EC2. Designer of a reusable production-grade Django REST template (JWT + OTP + Celery + structured logging + health monitoring) now used as the baseline across multiple company projects. Founder and sole engineer of Omnyvora, a multi-tool SaaS platform spanning a Django modular monolith, a Next.js 16 frontend, and a token-driven design system. Strong software-engineering-process background: requirement analysis, DFDs, ERDs, cost estimation and feasibility assessment delivered as formal client documentation.

### 3.3 — DevOps-leaning / Backend + Infrastructure
> Python backend developer with strong DevOps ownership. Every project I have shipped is containerised with Docker and Docker Compose, gated by a GitHub Actions CI pipeline (dependency install, migration drift check, image build/push, containerised test run) and continuously deployed over SSH to AWS EC2 or Hostinger VPS. Experienced with multi-stage Dockerfiles, Nginx and Caddy reverse proxies, AWS EC2/IAM/SES/RDS/S3, Cloudflare R2, Redis as cache/broker/OTP store, Celery worker and beat topologies with isolated queues, and live health-check dashboards covering database, Redis, SMTP, Celery worker and Celery beat.

### 3.4 — Full-Stack / Product Engineer
> Full-stack product engineer: Python/Django on the backend, Next.js 16 + React 19 + TypeScript on the frontend, and UI/UX design in between. At Omnyvora I built the entire platform alone — a domain-driven Django REST monolith, a feature-sliced Next.js workspace with JWT refresh-rotation, drag-and-drop content management and role-aware admin console, and a token-driven design system where each product re-skins itself by swapping two CSS variables. Day job: Senior Python Executive at Softvence Agency delivering client SaaS backends.

### 3.5 — API / Integrations Specialist
> Backend developer specialising in REST API design and third-party integration. Built and documented versioned REST APIs with a unified response envelope, JWT auth with refresh-token rotation and blacklisting, per-scope rate limiting, cursor/page pagination and strict model-level permissions. Integration experience spans payments (Stripe subscriptions, invoices, webhooks; Tap Payments for the Middle East), AI/voice (OpenAI, ElevenLabs), telephony (Twilio), scheduling (Cal.com, Google Calendar, Calendly, MindBody), automation (n8n webhook contracts), and messaging/storage (Firebase Cloud Messaging, AWS S3, Cloudflare R2).

### 3.6 — Junior-to-Mid (if the JD is explicitly junior/mid)
> Python-Django backend developer and CSE graduate with production experience across eight client projects. Comfortable across the whole stack of a backend service: PostgreSQL schema design, Django REST Framework APIs, Celery background jobs, Redis caching, Docker, and CI/CD with GitHub Actions. Fast, self-directed learner — moved from PHP/MySQL to production Django in under a year and was promoted to Senior Python Executive within eleven months of joining.

---

## 4. EMPLOYMENT HISTORY

### 4.1 — Softvence Agency — *Senior Python Executive* (current)

| | |
|---|---|
| **Company** | Softvence Agency |
| **Location** | Level 3/15, Ambon Complex, 99 Mohakhali C/A, Dhaka-1212, Bangladesh |
| **Type** | Full-time, on-site |
| **Dates** | 16 August 2025 – Present |
| **Progression** | Joined as **Junior Python Developer** → promoted to **Senior Python Executive** (July 2026) |
| **Employer GitHub account** | `am-jahid-hassan` (company policy: separate account, org repos only, all private) |

**What the role actually is:** I am the backend owner for client projects. Clients come through the agency (a significant share via Fiverr, with US, German, Middle Eastern, Brazilian/Portuguese and Australian end-clients). For each project I take the requirement documents, design the data model and API surface, write the backend, containerise it, build the CI/CD pipeline, deploy it to the client's cloud account, and hand over documentation. On several projects I was the *sole* backend developer; on others I led/shared the backend with 1–2 colleagues while frontend was handled by a separate team.

**Bullet bank — pick what matches the JD:**

- Designed, built and deployed **eight production client backends** in eleven months across Django REST Framework (4) and FastAPI (4), covering an AI voice-receptionist SaaS, a casino-affiliate short-video platform, an AI lead-generation SaaS, an AI-enhanced e-commerce platform, a geospatial building-recognition and gamification app, a professional-association member portal, a fitness-tracking platform and a field-service marketplace.
- Promoted from Junior Python Developer to **Senior Python Executive** within eleven months on the strength of end-to-end delivery ownership.
- Authored a **reusable production-grade Django REST starter** (JWT auth, OTP, async email, in-app notifications, structured logging, unified response envelope, soft-delete base model, health dashboard, Docker, CI/CD) that became the baseline for subsequent company projects, cutting new-project setup from days to hours.
- Owned **the full deployment lifecycle personally** on every project: multi-stage Docker images, Docker Compose stacks split into `local` / `prod` / `db` files, GitHub Actions CI/CD (build → push to Docker Hub → SSH deploy with image-pull retry and zero-orphan cleanup), and provisioning on AWS EC2 and Hostinger VPS behind Nginx or Caddy.
- Integrated and productionised **third-party platforms end-to-end**: Stripe (subscriptions, plans, invoices, checkout sessions, webhook event idempotency), Tap Payments (Middle East card billing with retry/dunning state machine), ElevenLabs (multilingual voice synthesis), Twilio (phone provisioning and call forwarding), Cal.com (booking), Google Calendar / Calendly / MindBody (scheduling sync), OpenAI (with per-request cost and token accounting), n8n (secure outbound + callback webhook contract), Firebase Cloud Messaging, AWS S3, AWS SES and Cloudflare R2.
- Built a **credit-based billing engine** with reserve-on-submit / finalise-on-callback semantics, automatic refunds for under-delivery, a full credit-transaction ledger with running balance, and a Celery Beat watchdog that auto-fails and refunds jobs stuck past a six-hour SLA.
- Implemented **structured observability**: a non-blocking `QueueHandler`-based logging pipeline writing to a queryable `SystemLog` model with request-scoped context (`request_id`, actor identity, IP, user agent) carried through `contextvars`, plus JSON formatting for downstream aggregation, and a live HTML health dashboard covering database, Redis, SMTP, Celery worker and Celery Beat.
- Designed **multi-tenant, role-based access control** across projects: organisation/business scoping, invitation flows with expiring tokens, super-admin consoles, and a strict permission class that closes DRF's default gap by enforcing `view_<model>` on safe methods.
- Produced **formal client-facing SDLC documentation** — requirement analysis, functional/non-functional requirement tables, use-case, activity, swimlane and ER diagrams, data-flow diagrams to four levels, function-point estimation, effort distribution, task scheduling, cost estimation (personnel + infrastructure + third-party), feasibility assessment and an RMMM risk plan — delivered as versioned system design documents during client onboarding.
- **Acted as the de-facto DevOps engineer on every project I own** — there is no separate infrastructure engineer, so containerisation, CI/CD, server provisioning, database setup and operation, object storage, mail configuration, reverse proxy and deployment are all mine, on top of writing the backend.
- **Unblock other engineers' infrastructure, not only my own** — regularly debug and fix colleagues' CI/CD pipelines, Docker builds, AWS provisioning and hosting configuration when a deployment problem is holding up their project, making me the person the team comes to when the blocker is infrastructure rather than application code.
- Used **AI coding agents (Claude Code, Cursor) as accelerators** while personally retaining ownership of architecture, system design, data modelling and code quality; every project carries a hand-written `CONTEXT.md`/`CLAUDE.md` that encodes the architectural rules the agent must follow.
- Wrote and maintained **API contract documentation and test collections** (Bruno collections, Postman collections, Swagger/OpenAPI via `drf-yasg`), and maintained per-app developer guides so other engineers could pick projects up.

### 4.2 — Omnyvora — *Founder / Lead Engineer & Designer* (own organisation)

| | |
|---|---|
| **Organisation** | Omnyvora — https://github.com/orgs/omnyvora/repositories |
| **Dates** | June 2026 – Present |
| **Role** | Founder, backend developer, frontend developer, and UI/UX designer — sole contributor |
| **Repos** | `omnyvora-backend` (Django REST), `omnyvora-frontend` (Next.js 16) |

Solely responsible for product definition, system architecture, backend, frontend, design system, containerisation and CI/CD. Full technical detail in **§8**.

**Bullet bank:**
- Founded and solely engineer **Omnyvora**, a multi-tool SaaS platform (CV Builder, Portfolio Builder, Image Enhancer) sharing one identity, profile, notification and billing foundation.
- Architected a **microservice-ready modular monolith** in Django 5.2 / DRF, organised into four bounded domains (`shared`, `user_data`, `portfolio`, `admin`) with a strict `models → selectors → services → serializers → views` layering and no cross-domain foreign keys (soft correlation keys only), so any domain can be extracted into its own service without a rewrite.
- Built the **Next.js 16 / React 19 / TypeScript** frontend with a feature-sliced architecture, TanStack Query for server state, Zustand for client state, React Hook Form + Zod validation, and an Axios interceptor implementing silent JWT refresh with request queueing during in-flight refresh.
- Designed the **Omnyvora design system** from scratch — a four-tier token architecture (primitive → semantic → service → Tailwind `@theme`) where each product re-themes itself by swapping exactly two CSS custom properties, plus a 20-component UI kit, dual light/dark semantics, self-hosted Inter + JetBrains Mono, and an isometric-cube brand mark.

### 4.3 — Cyber Hundred — *Web Development Intern*

| | |
|---|---|
| **Company** | Cyber Hundred |
| **Location** | Adapt F/K Complex, Kuratoli, Khilkhet, Dhaka |
| **Type** | On-site internship |
| **Dates** | 1 February 2024 – 30 July 2024 |
| **Certificate** | Issued 5 June 2024 |

**Bullet bank (as previously written for my résumé — reuse verbatim or tighten):**
- Developed and maintained frontend and backend features using HTML5, CSS, Bootstrap, PHP and MySQL across multiple client web projects.
- Assisted in documenting project workflows and preparing technical reports for multiple projects.
- Collaborated with the team on project planning, product development and execution.
- Used phpMyAdmin for database management, schema changes and query optimisation.
- Applied Git and GitHub for version control and collaborative development.
- Gained practical experience in teamwork, project management and software development methodologies.

---

## 5. EDUCATION

### 5.1 — B.Sc. in Computer Science & Engineering (BCSE)
- **Institution:** IUBAT — International University of Business Agriculture and Technology
- **Department:** Computer Science & Engineering
- **Dates:** 20 May 2020 – 30 June 2024
- **CGPA:** **3.59 / 4.00** ⚠️ *(one older source in my portfolio bio says 3.42 — see §17.1, verify before printing)*
- **Degree certificate issued:** 30 May 2024
- **Thesis:** *"Implementation of Parallel Data Transmission in Li-Fi Technology by Using RGB Light"*
- **Practicum project:** *"Development of Internet Service Provider System"*
- **Relevant coursework:** Data Structures & Algorithms, DBMS, Operating Systems, Software Engineering, Compiler Design, Computer Graphics, Computer Networks, Object-Oriented Programming

### 5.2 — Higher Secondary Certificate (HSC), Science
- **Institution:** Dhaka Udyan Government College
- **Dates:** June 2017 – April 2019 · **GPA:** 3.17 / 5.00

### 5.3 — Secondary School Certificate (SSC), Science
- **Institution:** Ibn Taymiyyah School and College
- **Dates:** January 2014 – April 2017 · **GPA:** 4.68 / 5.00

---

## 6. CERTIFICATIONS

| Certification | Issuing organisation | Date |
|---|---|---|
| **Python-Django** | EDGE — Enhancing Digital Government and Economy (Bangladesh Govt. ICT programme) | 22 July 2025 |
| **Internship Certificate** | Cyber Hundred | 5 June 2024 |
| **B.Sc. in Computer Science & Engineering** | IUBAT | 30 May 2024 |

---

## 7. PROFESSIONAL PROJECTS — SOFTVENCE AGENCY (CLIENT WORK)

> **⚠️ NDA notice for the AI agent:** Source code for all projects in this section is private and cannot be shared. On a CV, describe the *system, my role, the stack and the outcome*. Internal client identifiers/folder names below are for my own reference only — **use the product name, not the internal codename**, and never publish client account details, server IPs, or credentials. Live URLs marked "public" are safe to cite.

---

### 7.1 — CHYR — AI Voice Receptionist & Business Automation Platform
*(internal ref: `ahmadaoosaq123` · product name: **CHYR** · **Best for JDs about:** AI integration, SaaS, multi-tenant, payments, telephony)*

| | |
|---|---|
| **Type** | Multi-tenant B2B SaaS — AI voice agent that answers business phone calls |
| **My role** | Backend developer (shared team of 3; I owned auth, core, emails, logs, payments, OTP and subscription domains) + requirement analysis + design review |
| **Dates** | April 2026 – May 2026 (active development window on my commits) |
| **Stack** | Python 3.11+, Django 5.2, Django REST Framework 3.16, SimpleJWT, PostgreSQL, Redis 7, Celery + Beat, Docker/Compose, Gunicorn, AWS EC2 (two regions: Bahrain + Frankfurt), AWS IAM, AWS SES, boto3 / django-storages (S3), `drf-yasg` (Swagger), `django-filter`, `drf-nested-routers`, `phonenumbers`, Resend |
| **Integrations** | **ElevenLabs** (multilingual voice synthesis), **Twilio-style phone provisioning & call forwarding**, **Cal.com** (demo booking), **Stripe** (subscriptions/invoices/webhooks), **Tap Payments** (Middle East billing), **MindBody**, **Google Calendar**, **Calendly** |

**System shape (13 Django apps):** `authentication`, `business`, `agent`, `phone`, `call`, `booking`, `integration`, `payment`, `subscription`, `otp`, `emails`, `logs`, `core`, `api`.

**What I built:**
- **Multi-tenant business model** — `Business` (one per owner) with typed verticals (restaurant, salon & spa, travel agency, health clinic), US timezone enum, business hours, and normalised service categories with a backend-only `name_normalized` matching key plus a unique constraint so "Hair  Cut " and "hair cut" cannot both exist.
- **Role-based org membership** — `Profile` with role choices scoped to a business, plus `UserInvitation` with expiring unique tokens and an atomic `save_user()` that validates the password, creates the user and provisions the profile in a single transaction.
- **AI agent configuration** — `Agent` (one per business) bound to an ElevenLabs `Voice` registry (provider, `elevenlabs_voice_id`, gender, preview URL, language), multilingual toggle, custom greeting message, and an `AgentVoice` join table with a uniqueness constraint for per-agent voice libraries across English, Spanish, Arabic and Russian.
- **Telephony layer** — `Phone` provisioning (number, friendly name, locality, region, ISO country, JSON capability map) with an answer policy (always / after hours / business hours / when-I-don't-answer) and a `NoAnswerConfig` conditional-call-forwarding model carrying carrier-specific activation/deactivation prefixes (`*921` / `*93`) per phone type (mobile / VoIP / landline) and carrier (AT&T / Verizon / T-Mobile).
- **Dual payment provider abstraction** — `Payment`, `Invoice`, `WebhookEvent` and `TapPaymentMethod` models over a provider enum, with lazily created Stripe and Tap customer records (`get_or_create_stripe_customer()` / `get_or_create_tap_customer()`) so a business is only registered with a PSP on first charge.
- **Subscription & metered-feature engine** — `Feature` (with optional usage limit, overage price, and Stripe product/price sync), `Plan` (feature many-to-many, trial period, billing cycle), `Subscription` (trial state, current period window, cancel-at-period-end, provider subscription ID, **scheduled plan change applied by a Celery renewal task at the next billing cycle**, and Tap-specific retry counters with `tap_next_retry_at` dunning state), `SubscriptionAddOn`, `SubscriptionPayment`, `SubscriptionFeatureUsage` metering and `FreeTrialLog` for trial-abuse prevention.
- **Booking** — Cal.com credential storage per business, admin-published `AvailableSlot` inventory with a `(date, start_time)` uniqueness constraint, and `DemoBooking` capturing guest details, Cal.com booking IDs and the raw provider response as JSONB for reconciliation.
- **Integrations vault** — `IntegrationCredential` with per-provider OAuth token/refresh/expiry columns for MindBody, Google Calendar and Calendly, uniquely constrained per (user, provider).
- **Feature-usage metering utility** (`utils/check_feature_usege.py`) enforcing plan limits at call time, alongside a shared `utils/` package (`response.py`, `general.py`, `validators.py`, `app_model_relate.py`, `debug.py`) mirroring my standard core toolkit.
- Deployed to **AWS EC2 across two regions** with IAM users scoped per environment, AWS SES with DKIM/DMARC/custom MAIL-FROM DNS records configured, and a two-branch **GitHub Actions** pipeline (`dev_ci.yml` for PR gating, `main_ci_cd.yml` for build-push-deploy).

**Beyond the code — analysis and design-review work on this project:**
- Performed **requirement analysis from seven recorded client calls** (March and May 2026) plus a Fiverr inbox thread, working against a client-supplied **Dev Brief** and a formal **Statement of Work (SOW)**.
- Authored a **`Dev_Spec_Subscription_Tiers_and_Safety`** specification defining the plan tiers and the safety/abuse-prevention rules the billing engine had to enforce.
- Wrote a **full visual design critique of the CHYR dashboard** — a written, page-by-page review covering Home, Agent Config, Business, Phone, Integrations and Settings, plus overall visual polish — and a separate **landing-page development notes** document translating design changes into implementable frontend tasks. *(Good evidence for JDs that value design sense or frontend/design collaboration in a backend engineer.)*

---

### 7.2 — OCReels — Casino-Affiliate Short-Video Platform
*(internal ref: `rappio-2` · **live:** ocreels.com / app.ocreels.com / api.ocreel.com — public · **Best for JDs about:** FastAPI, async Python, high-traffic media, i18n, affiliate/fintech)*

| | |
|---|---|
| **Type** | Consumer short-form video (reels) platform monetised through casino affiliate revenue |
| **My role** | Backend developer — FastAPI service (16 of my commits; joint backend team). Frontend was a separate team. |
| **Dates** | June 2026 – July 2026 (my active window; project ongoing) |
| **Backend stack** | **FastAPI 0.119**, **Tortoise ORM 0.25 + Aerich migrations**, PostgreSQL (asyncpg) / MySQL (aiomysql) drivers, Redis, Celery 5.5 + APScheduler, Uvicorn, Pydantic v2 + pydantic-settings, python-jose / PyJWT, passlib + bcrypt, **pyotp (TOTP 2FA)**, `fastapi-mail` / aiosmtplib, aioboto3 + boto3 (S3 / Cloudflare R2), **firebase-admin** (FCM push + Firestore), **OpenAI + google-genai**, ffmpeg-python + imageio-ffmpeg (transcoding), python-socketio, Sentry, Locust (load testing), pytest + pytest-asyncio, Babel (i18n) |
| **Frontend stack (team-owned, for context)** | React 18 + Vite + TypeScript, Redux Toolkit + redux-persist, React Router 7, Tailwind 4, Radix UI, Framer Motion, **hls.js** adaptive video, **i18next** multi-language, TipTap rich text, Recharts, Firebase, PWA |

**What I worked on / the system I contributed to:**
- **Auto-discovering modular FastAPI architecture** — an application factory with an async `lifespan` that initialises the DB, Redis, the scheduler and permission sync, then walks the `applications/` directory and auto-imports each sub-app's `signals.py`; routes are registered dynamically via an `auto_routing` module, so adding a domain requires no wiring changes to `main.py`.
- **Domains:** `user` (UUID PKs, role enum, TOTP secret + `totp_enabled`, ban states with typed durations, per-device `DeviceToken` registry for FCM), `reels`, `casino`, `creator`, `comments`, `site`, `status`.
- **Reel model** with many-to-many categories and viewers, share/click counters, affiliate link, language and JSON tag list, adult-content and legal-disclaimer flags, media/thumbnail/logo asset paths, moderation `content_status` with admin review notes, plus `ReelShare` (per-platform attribution), `ReelsReview` (1–5 validated rating) and `Advertisement` slots.
- **Casino affiliate model** — per-casino tracking parameter, earning model enum (FTD vs revenue-share), FTD amount in USD, revenue-share percentage, geo-restriction via `allowed_countries` JSON, supported languages, bonus/promotional/terms content.
- **Creator programme** — `CreatorProfile` with an application → review → approval state machine (status, application note, rejection reason, agreement acceptance timestamp, reviewer FK), KYC-adjacent profile fields, per-creator tracking codes, **crypto payout configuration** (currency, network, wallet address), `CreatorSocialLink`, hashed `TotpBackupCode` records, and a `CreatorEarning` ledger keyed by casino + reel with FTD counts, commission percentage and USD amounts.
- **Custom RBAC** — hand-rolled `Permission` / `Group` models with a startup `sync_permissions()` routine that reconciles the permission table against code on every boot.
- Custom `MediaStaticFiles` class injecting immutable one-year `Cache-Control` headers on media responses; media served from Cloudflare R2 / S3 and a `cdn.ocreels.com` CDN origin.
- A **second standalone FastAPI service** (`form_server`) deployed alongside the main API with its own Dockerfile, compose file, Firebase config and migration set — handling form intake independently of the main platform.
- Deployed on **AWS EC2 with an Elastic IP, RDS, and IAM users**, with database and server-config backups, plus `dev.yml` / `main.yml` GitHub Actions pipelines and a `dummy_action.yml` no-op workflow for personal branches.
- The product runs across a **multi-domain estate** — `ocreels.com`, `oc-reels.com`, `ocreel.com`, `ocreels.net`, `ocshorts.com`, `onlinecasinoreels.com` (plus `app.` / `api.` / `cdn.` subdomains) — requiring CORS, CSRF-trusted-origin and cookie-domain configuration across all of them.

---

### 7.3 — ProspectLead — AI Lead-Generation SaaS (credit-based)
*(internal ref: `mystore2020` · **live:** prospectlead.ai / api.prospectlead.ai — public · **Best for JDs about:** SaaS billing, automation/n8n, OpenAI cost control, Stripe, Django)*

| | |
|---|---|
| **Type** | Credit-based B2B SaaS that turns a keyword + location + result-count into a downloadable file of AI-qualified business leads |
| **My role** | **Lead backend developer** — the largest share of commits on the repository; owned architecture, billing, leads pipeline, observability. **Also produced the UI/UX design and built the n8n automation workflow.** |
| **Dates** | January 2026 – July 2026 (longest-running project; my first major ownership) |
| **Stack** | Django + Django REST Framework, PostgreSQL, Redis, Celery + Celery Beat, Stripe, Google OAuth 2.0, S3-compatible storage, Docker/Compose (split `local-api` / `local-db` / `production-api` / `production-db`), **Caddy** reverse proxy, GitHub Actions, **Bruno** API collections |
| **Automation** | **n8n** workflow engine — outbound webhook + authenticated inbound callback contract; Google search + AI extraction pipeline runs entirely outside the Django process |

**What I built (11 Django apps: `authentication`, `core`, `credit`, `dashboard`, `emails`, `leads`, `logs`, `notifications`, `openai_usage`, `otp`, `payments`):**
- **The credit economy.** `CreditPackage` (Starter 100/$5, Growth 200/$8, Pro 500/$18 — DB-driven so admins change pricing without a deploy, with Stripe product/price IDs synced), `CreditTransaction` as an append-only ledger storing signed amounts, a typed reason enum, the related payment FK and a **`balance_after` running-balance snapshot** for auditability, and a `UserProfile.credit_balance` seeded with 10 free credits on registration.
- **Reserve-on-submit / finalise-on-callback semantics** — credits are reserved when a job is dispatched so a user cannot over-spend on concurrent jobs, then finalised on the n8n callback with automatic refund of the difference when fewer records are returned, and a full refund when the job fails.
- **`LeadGenerationRequest`** keyed by an external-facing UUID (never the DB PK), with a status state machine, JSON input payload, requested count, credits charged, error message, dispatch/completion/refund timestamps and **per-request OpenAI cost and token accounting**; `LeadResult` rows store extracted lead JSON.
- **OpenAI cost governance** — `OpenAIDailyUsage` (per-day, per-project cost to 12 decimal places, input/output/cached token counts, request counts), `OpenAISyncRun` (audit of each sync attempt with status and error), and `OpenAICreditLedgerEntry` (manual top-ups/adjustments with the recording admin and a note) — giving the business real unit economics per lead.
- **Secure webhook contract** with n8n: bearer-token-authenticated inbound callback, plus a **Celery Beat watchdog** that auto-fails and refunds any request with no callback after six hours.
- **Two-step OTP email registration** plus **Google OAuth** sign-in that skips OTP (email already verified by Google).
- **Stripe** checkout-session flow with `Payment` records, `credits_awarded`, and a `StripeWebhookEvent` table with a unique `stripe_event_id` for **idempotent webhook processing**.
- **Soft-delete `BaseModel`** (`created_at` / `updated_at` / `deleted_at`, `SoftDeleteManager` + `all_objects`) inherited across every domain model, and the structured `SystemLog` observability stack.
- Wrote the platform's **`Context.md` product specification** (problem statement, step-by-step flow, credit rules, page-by-page information architecture, webhook contract, tech stack table) used as the shared source of truth for the whole team, plus per-app developer guides (`Response.md`, `Services.md`, `Utilities.md`) and `docs/`.
- Built the **Bruno API collection** with requests organised into **Admin / Public / User** suites and multiple environments, for repeatable regression testing across environments.
- **Built the n8n automation workflow itself** (`For web - Google Maps Scraper`) — not just the integration contract — covering the Google Maps scrape, AI extraction and structured-output stages, with a maintained backup of the workflow definition.
- **Designed the product's UI/UX**: the **ProspectLead.ai landing page** and the **dashboard + auth screens** ("LeadGen Screens"), built against a shared design-system bundle — the same design-system workflow I use on Omnyvora.
- Produced **screen-recorded demonstrations** for the client (order walkthrough, OTP error reproduction) as part of delivery and QA communication.
- Deployed behind a **Caddy** reverse proxy with automatic HTTPS; authored `CADDY_SETUP.md` and the `Caddyfile`.

---

### 7.4 — Tundra — AI-Enhanced E-Commerce & Custom Product Platform
*(internal ref: `kilian_rohde` · **live:** thundra.de / ai.thundra.de / api.thundra.de — public · **Best for JDs about:** e-commerce, order/fulfilment systems, AI product generation, Django)*

| | |
|---|---|
| **Type** | German-market e-commerce platform with AI-generated custom product designs, wallet, discounts and marketing automation |
| **Architecture** | **Three separate services**: Next.js frontend · Django REST backend · **FastAPI AI image-generation service** — each independently containerised with its own CI/CD pipeline, behind a shared Caddy reverse proxy on one EC2 host (`thundra.de` · `api.thundra.de` · `ai.thundra.de`) |
| **My role** | Backend developer — sole author of all commits on my working copy; owned discounts, payments, wallet, events, automation, AI, documents, communication. **Also authored the complete client handover documentation package for all three services.** |
| **Dates** | April 2026 – May 2026 |
| **Stack** | Django 5.2.9, DRF 3.16, SimpleJWT, PostgreSQL (psycopg2), Redis, Celery 5.6, `django-storages` + boto3 (S3), `drf-yasg`, `django-filter`, `django-extensions`, `django-timezone-field`, `python-crontab` + `cron_descriptor`, Stripe 14.2, Faker, Docker/Compose, AWS EC2 + IAM, GitHub Actions |

**17 Django apps: `authentication`, `product`, `order`, `review`, `contentManagement`, `information`, `discount`, `smtp`, `payments`, `events`, `automation`, `core`, `ai`, `wallet`, `document`, `communication`, `my_test`.**

**What I built:**
- **Product catalogue** — `Category` / `SubCategory` / `Classification` / `Age` taxonomies, `Product` and `ProductImage`, with a documented **product-performance optimisation** pass (query optimisation and N+1 elimination) recorded in `PRODUCT_PERFORMANCE_OPTIMIZATION.md` / `OPTIMIZATION_SUMMARY.md`.
- **Order & fulfilment** — `CartItem`, `Order`, `OrderItem`, `Shipment` with typed shipment methods, and a reusable **`ShipmentAddressBook`** so customers reuse saved addresses; documented as `ORDER_SHIPMENT_FLOW.md` and `ADD_ORDER_ADDRESS_API.md`.
- **Discount engine** — `DiscountCodeSeries` → `DiscountCode` → `DiscountCodeRedemption`, supporting bulk generated code series with per-user redemption tracking (`PROMO_CODE_IMPLEMENTATION.md`).
- **AI custom product pipeline** — `CustomAiProduct`, `CustomAiProductVersion` (version history per generation) and `DesignImages`, letting customers iterate AI-generated designs before ordering.
- **Wallet, events and automation** — a customer `Wallet`, an `EventLog` audit trail, and an `Automation` / `AutomationLog` engine driven by cron expressions (`python-crontab` + `cron_descriptor`) for scheduled marketing and lifecycle jobs.
- **Operational documentation I authored:** `CICD_DOCUMENTATION.md`, `DEPLOYMENT_GUIDE.md`, `S3_SETUP_GUIDE.md`, `S3_BUCKET_POLICY_INSTRUCTIONS.md`, `QUICK_REFERENCE.md`, `ADDRESS_BOOK_VERIFICATION.md` and a bilingual `ORDER_PAYMENT_FLOW_BANGLA.md` for the local team.
- Deployed to **AWS EC2** with scoped IAM users, S3 media with an explicit bucket policy, **Stripe CLI-based local webhook testing**, and dual-branch GitHub Actions CI/CD across all three services.

**The handover package — a standalone deliverable worth citing on its own:**
At project close I authored **`HANDOVER.md`**, a 6-chapter, ~step-by-step operations guide written *in plain language for a non-technical owner*, plus a PDF export, a packaged zip of all three source repositories and server configuration, and the client-facing handover message. It walks the new owner through:

| Chapter | Contents |
|---|---|
| 1 — Common server setup | Create an AWS account · launch an EC2 instance · connect over SSH · install Docker · allow Docker without sudo · install **Caddy** as reverse proxy · generate an SSH deploy key for GitHub Actions · create server project folders · create a Docker Hub account |
| 2 — GitHub setup | Create the account · create three private repositories · upload all three codebases |
| 3 — Frontend (Next.js) | What it does · Docker image naming · environment configuration · files the server needs · GitHub Secrets · how its CI/CD works · trigger the first deploy · verify · ongoing maintenance |
| 4 — Backend (Django) | Same structure, plus **how migrations work** in the pipeline |
| 5 — AI service (FastAPI) | Same structure for the AI image-generation service |
| 6 — **Security cleanup** | Remove the previous developer's access from GitHub, AWS and Docker Hub · **roll the Stripe API keys** |

It closes with a progress checklist. *(This is strong evidence for JDs mentioning documentation, knowledge transfer, client-facing communication, or ownership through to handover — I proactively wrote the client an offboarding security-cleanup chapter that revokes my own access.)*

---

### 7.5 — LookUp (LookUp Architecture) — AI Building-Recognition, Tour & Gamification App
*(internal ref: `benkelly864` · product name: **LookUp** · **Best for JDs about:** geospatial, gamification, mobile backends, AI/vision, Django)*

| | |
|---|---|
| **Type** | Mobile-first app where users photograph buildings, get AI identification, collect them into curated collections, build walking tours and earn XP/badges |
| **My role** | **Sole backend developer** — all 18 commits are mine |
| **Dates** | April 2026 |
| **Stack** | Django + DRF, SimpleJWT + `dj-rest-auth` + `django-allauth` (**Google social login**), `drf-yasg`, `django-extensions`, `django-storages` (AWS S3), CORS headers, PostgreSQL, Docker/Compose, AWS EC2 + IAM, GitHub Actions (`ci-cd.yml` + `dev-ci.yml`) |

**What I built (apps: `user`, `explore`, `tour`, `reward`, `payment`, `health_check`):**
- **Over-normalised geospatial model** — `Country` → `City` with unique constraints, and a `BaseLink` → `Link` split so a URL's origin is stored once and paths reference it, with a computed `full_url` property.
- **`Explore`** — the core building record: lat/long to 7 decimal places, image, many-to-many tags, favourite flag, optional city grouping, user collection, and an **`ai_confidence_level`** score from the recognition pipeline; plus a **custom `CASCADE_IF_CITY_GROUP_NULL` on-delete handler** — a bespoke referential rule that only cascades when the record has no city grouping.
- **Tour engine** — `TourSetUp` (duration, route type, total distance, area-of-interest JSON, start/end coordinates, travel-point JSON) → generated `Tour` with a `tour_mapping_data` JSON payload, plus `FavouriteTour` and `SavedTour` with per-user uniqueness constraints.
- **Gamification system** — `Level` (ordered XP bands with a `get_next_level()` traversal helper and rewards, seeded from `levels.csv`), `UserLevel` (coins, current/completed status, uniqueness constraint per user+level), `Category` → `Buzzword` taxonomy, `RewardBuzzword` (bronze/silver/gold thresholds each with its own XP value), `BadgeBuzzword` unlock tracking, and a `LooksUp` search-history model — plus daily streak tracking (`current_streak` / `longest_streak`) on the customer profile.
- **User settings & privacy** — per-user `Setting` (2FA, biometric, push/email notifications, dark mode, language) and `Privacy` (data consent, save-photo, EXIF metadata stripping) models.
- Google OAuth via allauth social providers, S3 media storage with per-role upload path resolvers, and a dedicated `health_check` app.
- **Operational management scripts** (`scripts/`): `load_levels.py` (seeds the XP level ladder from `levels.csv`), `reward_rule.py`, `streak.py`, `email.py`, `user_check.py` — plus a shared `utilities/` package (`response.py`, `model_helper.py`, `data.py`, `generale.py`, `opt.py`).
- Implemented the gamification economy against client design artefacts — a **LookUp Gamification** specification and a **challenges / XP-tiers / taxonomy / levels** spreadsheet — translating a product-designed reward economy into a normalised, constraint-enforced schema.
- Authored **`Ai_Prompts/ai_rules.md`**, an AI engineering-preferences constitution governing agent-assisted work on the project: production-ready over experimental, performance-first (explicitly mandating `select_related` / `prefetch_related` / batching to minimise DB queries), strict separation of concerns, composition over inheritance, no tight coupling, no placeholders or pseudo-implementations, small focused functions, self-explanatory naming, and domain/feature-based file organisation. *(Concrete evidence that I direct AI tooling to engineering standards rather than accepting its output.)*

---

### 7.6 — ArchiCoPro — Professional Association Member Portal
*(internal ref: `passarinhama` · **live:** archicopro.cloud — public · **Best for JDs about:** FastAPI, RBAC/permissions, content platforms, community/portal systems)*

| | |
|---|---|
| **Type** | Members' portal for a professional (architecture) association — articles, document library, events, forums, trainings, notifications |
| **My role** | **Lead backend developer** — most commits on the repository |
| **Dates** | June 2026 – July 2026 |
| **Stack** | FastAPI + Tortoise ORM + Aerich, PostgreSQL, Redis, Celery, Docker/Compose (four compose files: `local-api`, `local-db`, `production-api`, `production-db`), GitHub Actions (`dev_ci.yml` + `main_ci_cd.yml`), Caddy-based deployment scripting |

**What I built (apps: `user`, `articles`, `documents`, `events`, `forums`, `trainings`, `notifications`, `settings`):**
- **Feature-level RBAC** — a `FEATURES` enum, `Role`, `FeaturePermission` and `UserFeaturePermission` models allowing permissions to be granted at the role level *and* overridden per user, plus per-content-type role permission tables (`ArticleRolePermission`, `ForumRolePermission`, `TrainingRolePermission`, `DocumentFolderPermission`) so visibility is enforced per resource, not just per endpoint.
- **Content domains** — `ArticleCategory`/`Article` with a publication status enum; a hierarchical `DocumentFolder` → `Document` library with typed files; `Event`/`EventRegistration` with event-type enums; `Training`/`TrainingRegistration` with format and status enums.
- **Moderated forums** — `Forum` → `Topic` → `Post` with a `ModerationStatus`/`ModerationAction` state machine and a `ModerationLog` audit trail.
- **Platform settings & operations** — admin-editable `SMTPConfiguration`, and a `BackupConfiguration` / `BackupRecord` system with configurable backup frequency, so the association can self-manage mail and backups.
- **Session & activity auditing** — `UserSession` and `ActivityLog` with a typed `ActivityActionType`, plus a `UserStatus` lifecycle enum.
- Managed server backups (container tarballs, environment variables, nginx config) and a **Caddy auto-deploy script**; migrated a prior `archicopro-backend` codebase into the current architecture.

---

### 7.7 — Fitness & Workout Tracking Platform
*(internal ref: `hawiisaac` · **Best for JDs about:** FastAPI, health/fitness apps, content feeds, Hostinger/VPS deployment)*

| | |
|---|---|
| **Type** | Fitness app backend — workout library, live session logging, social content feed, AI features |
| **My role** | Backend developer (contributing member of a larger team) |
| **Dates** | April 2026 – May 2026 |
| **Stack** | FastAPI + Tortoise ORM, `uv` dependency management (`uv.lock`) + `pyproject.toml`, Docker/Compose, **Firebase**, GitHub Actions (`main.yaml`), **Hostinger VPS** deployment with a dedicated `git_action` deploy user |

**What I built / contributed to (apps: `user`, `content`, `equipments`, `session`, `site`, `ai`):**
- **Training session engine** — `Workout` (typed by `WorkoutType`), `WorkoutSession` with a `SessionStatus` lifecycle, `SessionWorkout` join records, and separate **`SetLog`** (resistance training: sets/reps/weight) and **`CardioLog`** (distance/duration) telemetry models.
- **Equipment & anatomy taxonomy** — `Equipment`, `MuscleGroups` and `Category` models driving workout filtering.
- **Social content feed** — `Content` typed by `ContentFeedType`/`ContentType` with a full engagement stack: `ContentBookmark`, `ContentShare`, `ContentReaction` and `ContentView`.
- **Unit-preference system** — a `Preference` model with `WeightChoice`, `DistanceChoice` and `MeasurementChoice` enums so every number renders in the user's own units (kg/lb, km/mi).
- Custom `Permission` / `Group` RBAC, `Terms` / `Policy` / `CookiesPolicy` / `SiteReview` compliance models.
- An `ai` application module (schema-defined) for the platform's AI features.
- Provisioned and operated the **Hostinger VPS** including root and deploy-user setup (a dedicated `git_action` user) and GitHub Actions deployment scripting.
> *Product name not recorded in my working copy; the Firebase project is `hykx-4b453`. **Ask me for the public product name before putting one on a CV** — describe it as "a fitness and workout-tracking platform" otherwise.*

---

### 7.8 — Outdoorda — Field-Service Installer Marketplace
*(internal ref: `outdoorda` · **Best for JDs about:** marketplace platforms, payments/payouts, scheduling, FastAPI)*

| | |
|---|---|
| **Type** | Two-sided marketplace connecting customers with field installers — job management, availability, service areas, payments and payouts |
| **My role** | Backend developer |
| **Dates** | June 2026 |
| **Stack** | FastAPI + Tortoise ORM, SQLite (WAL mode) for the working environment, Docker + `compose.yml`, **Nginx** reverse proxy, `pyproject.toml`, `start.sh` entrypoint |

**What I built (apps: `user`, `customer`, `installer`, `admin`, `payments`, `communication`, `logs`, `site`):**
- **Two-sided profiles** — `CustomerInfo` and installer-side `ServiceArea` / `InstallerServiceArea` geographic coverage, `AvailabilitySettings` scheduling windows, and `InstallerReview` ratings.
- **Admin-configurable operations** — `JobManagementSettings` and `PaymentSettings` singletons so business rules (job routing, commission, payout terms) change without a deploy.
- **Money movement** — separate `Payment` (customer → platform) and `Payout` (platform → installer) models.
- **Auditing & sync** — `AuditLog` and `SyncLog`, plus a `DeviceToken` registry for push notifications and `Terms`/`Privacy` compliance models.
- **Route modules** covering `admin`, `auth`, `customer`, `installer`, `payment`, `communications`, `site` and `user`, with a `tasks/notify.py` background notification dispatcher.
- Deployed behind **Nginx** on a dedicated VPS.

---

### 7.9 — SafeTag — Emergency Evacuation Status Communication Platform *(system design & documentation)*
*(internal ref: `frogman58` · **Best for JDs about:** system design, technical writing, business analysis, requirement engineering, pre-sales)*

| | |
|---|---|
| **Type** | Real-time emergency evacuation status platform for US wildfire/hurricane/flood/earthquake response |
| **My role** | **System designer & technical author** — produced the complete v1 and v2 System Design Documents |
| **Date** | May 2026 |
| **Commercial context** | Fiverr-sourced US client · **$9,000 USD contract** · 16-week, 4-phase delivery plan |

**This project is my strongest evidence of formal software-engineering-process capability.** I authored a 9-chapter system design document covering:

| Chapter | Contents I produced |
|---|---|
| 1 — Overview | Project overview, objectives, user roles (Resident / Admin / First Responder), technical & operational feasibility assessment |
| 2 — Methodology & Tech Stack | Development methodology; an 18-row tech-stack table with an explicit *rationale* column for every technology selected |
| 3 — Requirement Engineering | Functional requirements per role (numbered, tabulated), non-functional requirements, **use case diagram** |
| 4 — System Planning | System project estimation, **function-oriented metrics**, **function point estimation**, process-based estimation, effort distribution, task scheduling, project schedule chart, and **cost estimation** broken into personnel / infrastructure / third-party service cost |
| 5 — Risk Assessment | Risk management and a full **RMMM plan** (risk identification, analysis, planning, mitigation, monitoring) |
| 6 — Analysis Modeling | **Activity diagram, swimlane diagram, ERD, and data-flow diagrams** |
| 7 — UI Designing | Screen designs |
| 8 — Quality Assurance | QA strategy |
| 9 — Conclusion | |

**Architecture I specified:** Django + DRF backend; **Flutter + GetX** mobile app (iOS/Android) with **Hive** offline storage so residents can set status without connectivity and sync on reconnect; **Next.js + React + Tailwind + Redux/RTK Query** admin & first-responder web portal; **Django Channels + Redis channel layer** over **Daphne** for real-time dashboard updates; **Celery + Beat** for scheduled status-reminder notifications; PostgreSQL with UUID PKs and decimal-precision GPS; **Firebase Cloud Messaging** push; **Twilio** SMS broadcast; **Google Maps Platform** with heatmap layer; **Cloudinary** media; **pyotp** TOTP 2FA for admins; **drf-spectacular** OpenAPI docs; English/Spanish i18n; CSV and PDF report export.

---

### 7.10 — Other client engagements (requirement analysis / scoping)

- **GoPadel** *(internal ref: `singio`)* — Padel-sports platform: reviewed and scoped a detailed development task breakdown, developer project plan, data model (v2.4), an in-store identification & payment system guide (v2.0), a location-intelligence / venue-scouting system, and a QR-code generator specification, including a **Playtomic integration via n8n**.
- **Scope analysis engagement** *(internal ref: `jittarakesh`)* — requirement gathering and scope documentation from client call recordings and Fiverr order activity.
- **PolicyNest** *(archived, internal ref: `fallinlove`)* — insurance policy management: admin / super-admin / website-user requirement documents, AWS EC2 + IAM provisioning, and CRUD-policy IAM user setup.
- **NYXO** *(archived, internal ref: `trilochan`)* — departmental strategic-power and tier-framework analysis documents.
- **Additional deployments** *(internal refs: `karolin`, `Templet`)* — AWS EC2 provisioning and a shared internal project template with codes, docs and requirements scaffolding.

---

## 8. OWN ORGANISATION — OMNYVORA (deep technical detail)

> Two public-organisation repositories, both authored solely by me: architecture, backend, frontend, design system, Docker, CI/CD.

### 8.1 — `omnyvora-backend` — Django REST modular monolith

**Live-facing description:** A production-grade, microservice-ready modular monolith serving a multi-tool SaaS platform (CV Builder, Portfolio Builder, Image Enhancer) on one identity, profile, notification and catalogue foundation.

| Layer | Technology |
|---|---|
| Runtime | Python 3.12 / 3.13 |
| Framework | Django 5.2 + Django REST Framework 3.16.1 |
| Auth | `djangorestframework-simplejwt` 5.5.1 with rotation + blacklisting |
| Database | PostgreSQL 15 (`psycopg` 3.3) |
| Cache / broker / OTP store | Redis 7 (`django-redis` 6.0) |
| Async | Celery 5.6.2 + Celery Beat, isolated queues |
| Media | Pillow 11.2 |
| Config | `python-decouple` with a typed `EnvConfig` loader |
| Validation | `phonenumbers` 9.0 |
| Container | Multi-stage Docker + Docker Compose (`db` / `local-backend` / `prod-backend`) |
| CI/CD | GitHub Actions — `dev_ci.yml` + `main_ci_cd.yml` |

**Domain architecture — four bounded contexts, 20 Django apps:**

```
core/                       shared foundation (no business domain)
  ├── cache/redis_client.py   singleton pooled Redis client
  ├── health/                 database · redis · email · celery worker · celery beat checks
  ├── services/               health_report() aggregator
  ├── utils/                  response · exception_handler · pagination · image · validators
  │                           · generators · decorators · query · file_validators
  │                           · app_model_relate (ModelInspector) · debug · general
  ├── models.py               BaseModel + SoftDeleteManager
  └── permissions.py          IsSuperAdmin · StrictDjangoModelPermissions

shared/       auth · profiles · otp · emails · notifications · logs · activity · catalog
user_data/    taxonomy · skills · projects · experience · education · certifications · social_links
portfolio/    templates · instances
admin/        console
```

**Engineering decisions worth citing on a CV:**

- **`BaseModel` with soft delete** — abstract base providing `created_at` / `updated_at` / `deleted_at`, a `SoftDeleteManager` that filters deleted rows by default plus an `all_objects` escape hatch, and `soft_delete()` / `restore()` / `is_deleted`. Inherited by essentially every model in the system (the graph analysis makes it the single most-connected node: 46 edges).
- **Strict layering per app** — `models.py` → `selectors.py` (read-only, noun-named query functions) → `services.py` (verb-named write operations) → `v1/serializers.py` → `v1/views.py` → `v1/urls.py`. Views never touch the ORM directly.
- **Unified response envelope** — every response, including 404s, 500s and validation failures, returns `{success, message, data, errors}` through `success_response()` / `error_response()` helpers with an error normaliser that flattens DRF, Django and raw exception shapes into a consistent structure — and injects exception class, traceback, path, method and payload into a `debug` key only when `DEBUG` is on.
- **No cross-domain foreign keys.** Domains correlate through soft keys (`SystemLog.request_id` ↔ `UserActivity.request_id`; `PortfolioItemVisibility.item_type` + `item_id` → `user_data`), documented explicitly in code comments and `docs/`. This is what makes the monolith genuinely extractable into services.
- **Two-plane observability**, deliberately separated:
  - **`shared/logs`** (engineering plane) — `SystemLog` with log level, event name, actor type/id/email, model/file/function name, traceback, JSON metadata, service name, request ID and IP; a non-blocking `QueueHandler`/`QueueListener` pipeline with a `DatabaseHandler` that has a **circuit breaker**; `LoggingContextMiddleware` injecting request context via `contextvars`; a JSON formatter for Datadog/ELK/Loki; message truncation at 5,000 chars and metadata capped at 64 KB with graceful degradation; four composite indexes.
  - **`shared/activity`** (product-analytics plane) — `UserSession` (session key, start/end, IP, user agent, device type, active flag, JSON metadata, computed `duration_seconds`) and `UserActivity` (service, action, path, method, status code, duration ms, referrer, device type) with five composite indexes; `ActivityTrackingMiddleware` registered *after* the logging middleware so it can reuse `request.request_id`; `login`/`logout` signal handlers opening and closing sessions; and analytics selectors (`get_active_user_count`, `get_daily_active_user_counts`, `get_platform_service_usage_rows`).
- **Celery queue isolation** — declared `default` and `activity` queues each with an explicit `routing_key` (with an in-code comment explaining that omitting it collapses both queues onto the same binding and fans every task out to both), plus explicit default queue/exchange/routing-key so unrouted tasks don't fall into Celery's undeclared built-in queue. Slow analytics writes can never block business tasks.
- **Redis-backed OTP service** — SHA-256 hashed codes and hashed user identifiers, single-use, configurable length and TTL, a per-user-per-purpose active-OTP cap enforced by an index, eight distinct purposes (registration, password reset/change, login, verification, change email/phone/username), and a `rules.py` policy layer returning per-purpose delivery rules. Email channel live; SMS channel interface ready.
- **JWT hardening** — 15-minute access tokens, refresh-token rotation with `BLACKLIST_AFTER_ROTATION`, `UPDATE_LAST_LOGIN`, HS256, and per-scope DRF throttles for login / register / change-password / change-email / get-OTP, all driven from environment variables.
- **`StrictDjangoModelPermissions`** — a custom permission class that closes a real gap in DRF: `DjangoModelPermissions` deliberately skips the `view_<model>` check on safe methods, meaning any authenticated user can read any model. My subclass enforces `view_<model>` on GET, matching write-method behaviour.
- **`PlatformService` catalogue** — one row per tool on the platform, where `slug` is the **single binding key across the entire stack**: it matches the Next.js route segment, the frontend service-registry key, and the `data-service` CSS theming attribute. Colour columns are named as snake_case mirrors of the frontend camelCase design tokens so the client applies them as CSS custom properties with zero transformation. Also carries role-aware `user_path` / `admin_path` so "Open app" routes admins and users to different destinations.
- **Portfolio template engine** — `Template` → `TemplatePage` (typed pages with a `FileSizeTypeValidator` enforcing max size and allowed extensions on uploaded HTML), `TemplateSection` (ordered, required/optional), `TemplateField` (placeholder keys like `portfolio.github_url`), `TemplateAsset` (uploaded assets mapped to the relative path referenced inside the HTML) — and on the instance side `PortfolioInstance` (unique slug, status, **`setup_step` wizard resume point**, custom domain, published timestamp), `PortfolioSectionState`, `PortfolioService` and `PortfolioItemVisibility`.
- **`user_data` domain** — a normalised CV/portfolio data model: `Technology` taxonomy (with name normalisation so "Java  Script " and "Java Script" collide correctly on the unique constraint), `UserSkill` (0–100 validated proficiency), `Experience` (M2M technologies, null end-date = present), `Education` (GPA + scale, optional certification FK), `Project` (JSON achievements list, separate `technologies` and `skills` M2M, featured flag) with `ProjectImage` (cover-image election, ordered gallery), `Certification` and `SocialLink` — every model carrying a `display_order` with **drag-and-drop reorder endpoints implemented via a single `bulk_update`** and ownership validation that rejects the whole payload if any ID isn't the caller's.
- **Live health dashboard at `GET /`** — HTML report covering database, Redis, SMTP, Celery worker (via inspect) and Celery Beat (via a heartbeat key written by a 60-second Beat task).
- **Fully environment-driven configuration** — a typed `EnvConfig` loader exposing ~39 settings including granular OTP charset control (`OTP_ALLOW_NUMBER` / `_CAPITAL` / `_SMALL` / `_SPECIAL`), `MAX_ACTIVE_OTPS`, `MAX_VERIFY_ATTEMPTS`, per-endpoint throttle rates, token lifetimes, CORS allow-lists plus origin regexes, CSRF trusted origins and allowed methods — so security posture is tuned per environment without a code change.
- **API test assets:** a `my_test` app carrying a **Postman collection** (`Omnyvora_API.postman_collection.json`) with separate **BPS and Localhost environment files**, and a dated manual endpoint test-results report (`current_test_results(26-05-19).md`) recording pass/fail per endpoint.
- **Documentation I wrote for this repo:** root `README.md`, `docs/README.md` (13-section project doc with an ASCII architecture diagram and request-lifecycle walkthrough), `docs/apis.md` (57 KB endpoint-by-endpoint API reference with request/response bodies, a search guide and anchor-linked TOC), `docs/activity-system.md` (26 KB), `docs/logging-system.md` (21 KB), `developer_guide/` (Response, Services, Utilities, FileUploads), and per-app `docs/README.md` files.

### 8.2 — `omnyvora-frontend` — Next.js 16 workspace

| Layer | Technology |
|---|---|
| Framework | **Next.js 16.2** (App Router) + **React 19.2** + **TypeScript 5** |
| Styling | **Tailwind CSS 4** (`@theme`), `class-variance-authority`, `clsx`, `tailwind-merge` |
| Components | **shadcn/ui** on Radix primitives (avatar, dialog, dropdown-menu, label, separator, slot, tooltip) |
| Server state | **TanStack React Query 5** (+ devtools) |
| Client state | **Zustand 5** (persisted sidebar collapse, notifications drawer, per-feature stores) |
| Forms | **React Hook Form 7** + **Zod 4** via `@hookform/resolvers` |
| Interaction | **dnd-kit** (core / sortable / utilities) for drag-and-drop reordering |
| HTTP | **Axios** with request + response interceptors |
| Media | `browser-image-compression` for client-side pre-upload compression |
| UX | `sonner` toasts, `next-themes` light/dark, `lucide-react` icons |
| Testing | **Vitest 4** + Testing Library (react / jest-dom / user-event) + jsdom |
| Tooling | ESLint 9 (`--max-warnings 0`), `tsc --noEmit` type-check script, pnpm workspaces |
| Container | Docker + Nginx config, `docker-compose.local.yml` / `docker-compose.prod.yml` |

**Architecture:**
- **Route groups** — `(public)` wrapped in `GuestGuard` (statically rendered, SEO-friendly: landing, login, register, forgot-password, reset-password) and `(workspace)` wrapped in `AuthGuard` with `force-dynamic` (dashboard, applications, profile, account, cv-builder, portfolio, image-enhancer), plus a separate `/admin` tree behind `SuperAdminGuard` (dashboard, users, services, logs, settings). Every route ships its own `loading.tsx` and, where relevant, `error.tsx`.
- **Feature-sliced source layout** — `src/features/<feature>/{api,hooks,transformers,types,store,utils,components,pages}` for account, activity, admin, auth, catalog, cv-builder, dashboard, image-enhancer, portfolio, profile and user-data; `src/shared/` for auth context + guards, workspace shell (Sidebar, Topbar, AppCard, StatCard, ActivityItem, AdminSidebar), notifications drawer and the UI kit; `src/core/` for the Axios client, response types, service registry, design tokens and hooks.
- **Token-secure Axios layer** — access token held **in JS memory only** (intentionally lost on reload, ~15-minute lifetime), refresh token in `localStorage`; a response interceptor that on 401 performs a **silent refresh, queues all concurrent in-flight requests behind a single refresh, replays them with the new token**, stores the rotated refresh token, and on failure clears both stores and dispatches an `auth:logout` event. Guards against infinite retry loops by only retrying requests that actually carried an `Authorization` header. The security trade-off is documented in-code.
- **Design-token system (`src/core/design/`)** — a four-tier pipeline (primitive hex → semantic light/dark → per-service accent → Tailwind `@theme` → shadcn bridge variables) with a `TOKENS.md` editing contract and two hard rules: *never hardcode a colour, font, radius or shadow in a component; never use `style={{}}` with raw values.* Adding a new product = one new token file + one `[data-service]` block.
- **Drag-and-drop content management** — a `useDragReorder` hook plus manager/panel component pairs for Skills, Projects, Experience, Education, Certifications and Social Links, backed by the backend's bulk reorder endpoints.
- **Admin console** — users list/detail, platform-services CRUD with a form dialog, logs with a filter bar, settings tab panels, and dashboard visualisations (growth chart, service-usage bars, alert cards).

### 8.3 — Omnyvora design system (UI/UX work I did myself)

- A **token-driven design system v1.0** with documented architecture, editing rules and adherence linting (`_adherence.oxlintrc.json`), shipped as a reusable bundle (`_ds_bundle.js`, `_ds_manifest.json`).
- **33 component preview pages** built and documented: buttons (variants / sizes / dark), inputs, textarea, controls, dropdown, modal, card, avatars, badges, sidebar, topbar, stats, toasts, skeleton, empty states, tooltip/divider, elevation, radius, spacing scale, motion, theming, logo light/dark, and the full colour (gray / status / accent) and type (display / body / labels) scales in both semantic light and dark.
- **Four complete workspace designs:** Omnyvora Design System, Auth Design, User Workspace Design, Super Admin Workspace.
- **Brand identity** — an isometric cube-cluster mark, strictly two-colour (`#111111` / `#FFFFFF`), inverting between light and dark modes; light/dark logo lockups and mark variants produced.
- **Typography** — self-hosted Inter (variable, plus 18/24/28pt optical sizes across nine weights with italics) and JetBrains Mono variable, with a defined display/body/label type scale.
- **Content design system** — a documented voice ("precise, calm, engineering-literate"), person/casing rules (sentence-case verb-first buttons, UPPERCASE eyebrow labels as the system's signature accent), length caps for toasts and empty states, and a rule that all numbers, IDs and endpoints set in JetBrains Mono. The voice deliberately mirrors the backend's naming convention — services are verbs (`create_profile`), selectors are nouns (`get_profile_by_user`).
- **Design-direction authoring** — I write structured design briefs, not just code. The Omnyvora landing-page brief (`documentation/landing-page-design-prompt.md`) specifies content, structure, semantic section order and layout **while deliberately containing no colours, fonts, spacing or component styling**, because the design system already owns those — and it explicitly instructs against fabricating testimonials, customer names, review scores or usage statistics, substituting honest unverifiable-claim-free lines instead. *(Useful evidence for JDs valuing design collaboration, content strategy, or ethical product copy.)*
- **Design-system governance** — the token contract is machine-enforced via an adherence lint config (`_adherence.oxlintrc.json`) so the "never hardcode a colour" rule fails CI rather than relying on review.

---

## 9. PERSONAL & OPEN-SOURCE PROJECTS (GitHub: abdullah-md-jahid-hassan — 27 public repos)

**Profile facts:** 27 public repositories · account created 16 Feb 2024 · 0 gists · no GitHub organisation memberships on the personal account (Omnyvora is owned separately). Repo count and dates verified via the GitHub REST API on 25 Jul 2026.

### 9.0 — Dated project index (⭐ = flagged "featured" in my own portfolio)

| # | Project | Start | End | Primary stack | Live |
|---|---|---|---|---|---|
| 1 | Inflation Effect Calculator | 2021-04-05 | 2021-04-05 | C++ | — |
| 2 | Ticket Vending Machine | 2022-06-12 | 2022-06-12 | C++ | — |
| 3 | Flag of Honduras — 2D Animation | 2022-07-17 | 2022-07-30 | C++, OpenGL | — |
| 4 | ⭐ **Thesis on Li-Fi Technology** | 2023-01-05 | 2023-12-29 | C++, Arduino | — |
| 5 | City Night 2D Animation | 2023-05-07 | 2023-05-28 | C++, OpenGL | — |
| 6 | C++ Compiler Simulation | 2023-06-04 | 2023-06-21 | C++ | — |
| 7 | ⭐ **ISP Management System** | 2024-01-07 | 2024-07-17 | PHP, MySQL, Bootstrap 5 | 🔴 ~~isp.amjh.space~~ — dead, expired domain (§17.5) |
| 8 | Resume Template | 2024-07-04 | 2024-07-05 | HTML | — |
| 9 | ⭐ **ESP8266 All-in-One** | 2024-07-10 | 2024-10-09 | C++, ESP8266 | — |
| 10 | Favourite Foods Manager | 2025-01-02 | 2025-01-02 | Python (CLI) | — |
| 11 | Basic Calculator | 2025-01-03 | 2025-01-03 | Python (CLI) | — |
| 12 | Contact Manager | 2025-01-10 | 2025-01-10 | Python, CSV | — |
| 13 | To-Do List | 2025-01-16 | 2025-01-16 | HTML/CSS/JS | — |
| 14 | Library Management System v1 | 2025-02-13 | 2025-02-13 | Python, CSV | — |
| 15 | Hospital Management System | 2025-02-13 | 2025-02-17 | MySQL, SQL, ERD | — |
| 16 | Variable Step-Down Power Supply | 2025-02-13 | 2025-02-15 | Electronics | — |
| 17 | Banking Management System | 2025-02-20 | 2025-02-20 | Python, CSV | — |
| 18 | Product Description Page | 2025-03-06 | 2025-03-06 | HTML/CSS | — |
| 19 | Shopping Cart | 2025-03-12 | 2025-03-13 | HTML/CSS/JS | — |
| 20 | Library Management System v2 | 2025-03-12 | 2025-03-13 | Python, CSV | — |
| 21 | ⭐ **Personal Assets Management** | 2025-04-25 | *ongoing* | Django, MySQL, DRF | — |
| 22 | ⭐ **Dynamic Portfolio Website** | 2025-05-03 | 2025-06-06 | Django, SQLite, Bootstrap 5 | ⚠️ https://abdullahmdjahidhassan.pythonanywhere.com — live but ~1 yr stale (§17.5) |
| 23 | 12 V Li-ion Battery Pack (3S4P) | 2025-05-10 | 2025-05-13 | Electronics | — |
| 24 | ⭐ **Chat Box (Django Channels)** | 2025-08-18 | 2025-08-19 | Django 5, Channels, Redis, Daphne | — |
| 25 | `django_templet` (starter) | 2026-06-30 | *ongoing* | Django, DRF, Celery, Docker | — |
| 26 | `cv_builder_v1` | 2026-07-13 | 2026-07-13 | Python, Jinja2, WeasyPrint | — |
| 27 | `long_range_smartwatch` | 2026-07-17 | *ongoing* | Django, Channels, Flutter, FCM | — |

> **Agent note:** the six ⭐ projects are the ones I self-selected as portfolio highlights. For a CV, prefer #25–27 and #21/#24 (recent, technically substantial) over the 2025 CLI exercises, unless the JD is explicitly junior.

### 9.1 — `django_templet` — Reusable Production-Grade Django REST Starter ⭐
*Created Jun 2026 · Python · **Best for JDs about:** framework design, developer tooling, reusable architecture*

My own reusable Django REST foundation, extracted from repeated production needs and now the baseline I fork for new projects. 176 files across `authentication`, `activity`, `core`, `emails`, `logs`, `notifications`, `otp`, `my_django`.

**Ships with:** JWT auth (register, login, logout, refresh/verify, password change, OTP-gated password reset) · Redis-backed SHA-256 OTP system with configurable TTL/length and per-purpose policy · async Celery email with 3-retry exponential backoff on SMTP failure · in-app notifications (list/paginate/mark-read/unread-count) · the unified `{success, message, data, errors}` response envelope · soft-delete `BaseModel` · aspect-ratio-preserving image resize that never upscales · a live health dashboard (DB · Redis · SMTP · Celery worker · Celery Beat) · non-blocking structured logging with `contextvars` request context · per-scope rate limiting · multi-stage Dockerfile + entrypoint · `docker-compose.local.yml` / `.prod.yml` · CI env dummy · and a `developer_guide/` (Response, Services, Utilities) plus per-app docs.

### 9.2 — `long_range_smartwatch` — Internet-Relayed Smartwatch Platform ⭐
*Created Jul 2026 · Python · 39 commits · **Best for JDs about:** IoT, real-time systems, product architecture, hardware+software*

**The idea:** conventional smartwatches pair over Bluetooth (~10 m). This replaces the radio link with an **internet relay server** — watch and phone both connect to a central Django service, so they stay in sync at any distance. Intended as the technical differentiator for a smartwatch company.

**What I've built and, more importantly, how I sequenced it** — a genuinely senior architectural decision recorded in my `CONTEXT.md`:
> The watch hardware and its protocol (REST vs WebSocket vs MQTT) are undecided, so building an API shaped around reversible assumptions would be throwaway work. Instead: **build the service layer first**, put a human-operated admin panel on top of it as the temporary client, and defer API design until the protocol is known. The admin panel's buttons call the exact same service functions a future watch endpoint will call — making the panel the de-facto integration test harness for every service before any device depends on it.

**Phase 1 scope (current):** Django + DRF service layer · **Django Channels** for low-latency instruction delivery (chosen over polling explicitly to avoid battery drain and lag) · admin panel with fleet dashboard, device registry and per-device action console · **Flutter** companion app using consented runtime permissions (never root) with **Firebase Cloud Messaging** wake-on-instruction to avoid background polling · full admin attribution + timestamped audit trail on every action · permission groups so high-risk actions (remote control) are restricted more tightly than low-risk ones (view notifications). Roadmap phases 2–4: watch API layer → hardware swap-in → multi-tenant fleet management, billing and compliance hardening.

Reuses my full production stack: `activity`, `authentication`, `core` (health, cache, utils), `emails`, structured logging, developer guides, Docker and CI dummy env.

### 9.3 — `cv_builder_v1` — Template-Based CV/Résumé Generator
*Created Jul 2026 · Python + HTML/Jinja2 · **Best for JDs about:** CLI tools, document generation, templating*

A data-driven CV builder: each design lives in its own folder as a Jinja2 HTML template plus a matching JSON data structure, so **content is fully separated from design — you edit JSON, never HTML**. One CLI command renders a print-ready A4 **PDF via WeasyPrint** or a **single self-contained HTML file with images embedded as base64**. Three templates recreated pixel-close from reference images (`modern_navy_cv`, `elegant_gold_cv`, `corporate_blue_cv`, plus an enhanced corporate variant). Features graceful fallbacks (optional fields simply disappear when empty), automatic placeholder silhouette when no photo is set, directory-aware output paths, and a documented "add a new template" contribution path.

### 9.4 — `my_portfolio_v1` — Dynamic Portfolio CMS (Django)
*Django + SQLite + Bootstrap 5 · Live (but ~1 yr stale — see §17.5): abdullahmdjahidhassan.pythonanywhere.com · **Best for JDs about:** full-stack Django, CMS, admin interfaces*

A full dynamic portfolio platform with a custom `AbstractUser`-based user model and a `landing_spot` app whose schema I evolved over 12 migrations. **This is also the data source for §14** — it models `User` (tagline, location + map link, about, socials, banner/profile images, hobbies, languages, meta description, static résumé file), `Experience` (with a separate `resume_des` field holding CV-ready bullets and an on-site/remote type), `Education` (grade + grade standard, `resume_achi` achievements), `Certification`, `Service`, `SkillCategory` → `Skill` (percentage proficiency), `ProjectCategory` → `Project` (tagline, description, image, GitHub + live links, date range, featured flag, slug, `resume_des`), `Contact` (112 submissions received), and a whole **`resume` app** — `Resume` (named variants with a summary, one active), `ResumeProject`, `ResumeCertificate`, `Reference` and `ResumeReference`, each with a `hierarchy` ordering field. Frontend: Bootstrap 5, AOS scroll animations, Isotope filtering, GLightbox, Swiper.
> **Note for the agent:** I had already built a CV-variant system in 2025. Two résumé variants exist in the data — *"General Purpose"* and *"DevOps"* — see §14.4 for their summaries.

### 9.5 — `Chat_box` — Real-Time Chat (Django Channels)
*Aug 2025 · **Best for JDs about:** WebSockets, real-time, async Django*

Multi-room real-time chat over WebSockets. **Django 5 + Django Channels**, **Daphne** ASGI server, **Redis** channel layer for group broadcasting, ASGI-first `ProtocolTypeRouter` with `AuthMiddlewareStack` and `AllowedHostsOriginValidator`. Rooms joined via URL (`ws/<name>/<room_name>/`), named messages, group broadcast to every room member, Bootstrap 5 responsive UI with a live message log. Files: `chatbox/asgi.py`, `chat/routing.py`, `chat/consumers.py` (`WebsocketConsumer` handling connect/receive/group-send), `chat/templates/room.html`.

### 9.6 — `Personal_assets_management` — Islamic-Finance Personal Asset Manager
*Apr 2025 – ongoing · Django + MySQL · **Best for JDs about:** fintech, domain modelling, Django*

Django financial management system with role-based admin/user access. Tracks multiple income sources (salary, business, investment) and asset classes, **automatically calculates zakat against the nisab threshold** and tax obligations, supports document/proof upload against every entity, provides admin and user dashboards with summaries, and issues due-date alerts for tax and zakat payments.

**Apps:** `accounts`, `api`, `assets`, `incomes`, `dashboard`, `verify`.
**Data model — polymorphic asset design:** a base `Asset` (user, name, purchase date, value, uploaded proof document, type) specialised into `LandAsset` (location, area in square feet, **fractional ownership percentage**), `TangibleAsset` (weight in grams, quality, linked to a `TangibleAssetType` carrying a per-gram price so gold holdings revalue centrally), and `ShareAsset` (company name, share count, market price). This is the correct shape for zakat: each class has a different valuation rule.
**Also includes** a **Django REST `api` app** with serializers, and an email-verification subsystem (`api/utility/email.py`, `api/utility/verify.py`, `verify/` app) with HTML email templates and a verification landing page.
**Stack:** Python/Django, MySQL, Django REST Framework, HTML5/CSS3, Bootstrap.

### 9.7 — `Internet-Service-Provider` — ISP Management System (academic practicum, featured)
*Jan 2024 – Jul 2024 · PHP + MySQL + Bootstrap 5 · ~~Live: isp.amjh.space~~ 🔴 **dead — expired domain, do not cite (§17.5)** · **Best for JDs about:** PHP legacy, full-stack, business systems*

Web platform centralising ISP operations. Role-based login for admins, employees and customers; dashboard of critical ISP metrics; customer and employee record management; **payment tracking with invoice generation**; task assignment and service tracking; mobile-friendly responsive UI. My university practicum project, still live.

### 9.8 — Academic & CLI portfolio (Python / C++)

| Project | Stack | Notes |
|---|---|---|
| `Contact_manager` | Python, CSV | CLI CRUD contact manager with persistent CSV storage, modular structure |
| `Library_management_system_v1` | Python, CSV | Add/view books with CSV persistence |
| `Library_management_system_v2` | Python, CSV | Enhanced: full add/view/update/delete, modularised |
| `Banking_management_system` | Python, CSV | Account creation, deposit, withdrawal, balance checks |
| `Basic_calculator` | Python | Arithmetic with error handling for invalid input and division by zero |
| `Favourite_foods_manager` | Python | CLI list manager with text-file persistence |
| `Hospital_management_system` | MySQL/PostgreSQL, SQL, ERD tools | Normalised hospital schema (patients, doctors, appointments, treatments, billing). Ships an actual **`HMS_ERD.png` entity-relationship diagram** plus a runnable `hospital_management_system.sql` schema script — a pure data-modelling artefact, useful evidence for JDs asking for database design |
| `c-_compiler` | C++ | Compiler simulation — lexical analysis, syntax analysis against a customisable grammar file, intermediate code generation |
| `city_night_2d_animation` | C++, graphics lib | 2D animated night cityscape: moving vehicles, twinkling stars, illuminated buildings |
| `flag_of_honduras_2d_animation` | C++, **OpenGL**, Code::Blocks | Flag rendering + animation; modular header/source structure |
| `inflation_effect_calculator` | C++ | CLI tool computing future purchasing power under a given inflation rate |
| `Ticket_vending_machine` | C++ | CLI ticket vending simulation with destination selection, payment and receipt |
| `To-Do-List` | HTML5/CSS3/JS ES6 | Responsive task manager |
| `Shopping-Cart` | HTML5/CSS3/JS ES6 | Responsive cart with add/remove and live total |
| `Product-Description-Page` | HTML5/CSS3 | Responsive product detail page with gallery and specs |
| `Resume_Template` | HTML | Clean responsive résumé template |

### 9.9 — `All-Code` — Consolidated University & Training Code Archive
*~54 MB · 2,950+ files · **Best for JDs about:** breadth of languages, CS fundamentals, C#/.NET, Java*

A single archive of my entire university and training codebase. **This is the evidence behind every "foundational" language claim in §15** — if a JD asks for C#, Java or OpenGL, the proof is here.

| Area | Volume | Contents |
|---|---|---|
| **C# / .NET 6 — "Visual Programming"** | ~2,067 files (222 `.cs`, 74 solutions, 73 projects) | Labs 01–07 plus a Lab Test and a **final assignment** (`Visual_Final_Assignment`), each a full Visual Studio solution targeting .NET 6. **This is my strongest C# evidence — far more substantial than the "60%" self-rating in the old portfolio DB suggests.** |
| **Java** | 421 files (54 `.java`) | NetBeans projects — `Java Lab` coursework and an **Encode-Decode** project |
| **HTML & CSS** | 233 files | `Examples`, `Elements`, and a **static portfolio website** build |
| **Bootstrap** | 88 files | Bootstrap 5 and 5.3.3 working sets |
| **C** | 51 files | CSC 184 lab reports, CSC 437 |
| **C++** | 29 files | CSC 284 final lab reports (11 problems); **CSC 461 Programming Language Structure** — a grammar file plus a `sentance_recognizing.cpp` parser (the compiler-theory work behind `c-_compiler`) |
| **OpenGL** | 13 files | CSC 455 8th- and 10th-semester finals in Code::Blocks, including the `Citynight_2` source behind the City Night animation |
| **Python** | 29 files | **EDGE Python-Django course archive** — 11+ dated class notebooks (Dec 2024 – Jan 2025), 8 mid-term exam solutions, and assignments including a simple calculator, list de-duplication, and a **student-CGPA pie chart generated over a 10,000-row result CSV**; plus a Django portfolio front-end template |
| **PHP** | 6 files | Basic practice (variables, type casting, math operators/functions) and tools |
| **Arduino** | 3 sketches | `Automatic_Counter`, `Temp1` (temperature), **`Turbidity`** (water-turbidity sensor) |
| **ESP8266** | 1 sketch | **`Evil_twine`** — an "evil twin" access-point experiment, i.e. hands-on **wireless network security** work *(mention only where a security or networking JD makes it relevant, and frame it as academic/lab work)* |
| Misc | | `all_books.json`, `database_structure.csv`, `ksp.cpp` |

---

## 10. HARDWARE, IoT & RESEARCH PROJECTS

### 10.1 — B.Sc. Thesis: Parallel Data Transmission in Li-Fi Using RGB Light ⭐
*Jan 2023 – Dec 2023 · **Best for JDs about:** research, embedded systems, R&D, optical communication*

Research + working prototype for **high-speed optical wireless (Li-Fi) communication using RGB colour encoding to transmit three bits in parallel per symbol** rather than serially — a throughput multiplier over conventional single-channel Li-Fi. Included a comparative analysis against traditional wireless methods, a C++ prototype, performance evaluation under varying environmental/ambient-light conditions, and full research documentation.
**Hardware:** Arduino UNO, RGB LED module, RGB colour sensor, LDR, IR LED and photodiode, breadboard/jumper prototyping. **Tools:** C++, Arduino IDE.

### 10.2 — `Esp8266_all_in_one` — IoT Web-Controlled Device Platform
*Jul 2024 – Oct 2024 · C++ · **Best for JDs about:** IoT, embedded, firmware*
Integrated ESP8266 IoT solution exposing a **built-in web interface over Wi-Fi** for real-time remote control and monitoring of connected devices, with live sensor data display and a modular codebase designed for scaling to additional peripherals.

### 10.3 — Variable Step-Down Bench Power Supply (1.3 V – 19.1 V, 5 A)
*Feb 2025* · Designed a variable DC bench supply from a 19 V 3.25 A laptop adapter using an **XL4015 buck converter**, with a **Schottky diode for reverse-polarity protection**, heat-sinking, and validation via multimeter and load tester. Built for powering dev boards and sensors during prototyping.

### 10.4 — 12 V Li-ion Battery Pack (3S4P, 18650)
*May 2025* · Built a 12 V rechargeable pack from twelve 18650 cells in **3S4P** (~12.6 V full / 11.1 V nominal) with a **3S 40 A BMS** for overcharge, over-discharge and short-circuit protection, a push-button digital voltmeter for on-demand monitoring, separate DC input/output jacks, and a hand-built enclosure.

---

## 11. ENGINEERING PRACTICES I CAN CLAIM (evidence-backed)

Use these to answer "what kind of engineer are you?" bullets in a JD.

| Practice | Evidence |
|---|---|
| **Layered / clean architecture** | `models → selectors → services → serializers → views` enforced across 20 apps in Omnyvora; services are verbs, selectors are nouns |
| **Domain-driven modularisation** | Four bounded contexts (`shared` / `user_data` / `portfolio` / `admin`) with no cross-domain FKs; documented soft-correlation pattern |
| **Microservice-ready monolith** | Explicit design goal, documented in `core/docs/README.md`; any domain extractable without rewrite |
| **DRY / reusable foundations** | `BaseModel`, `success_response`/`error_response`, `StandardPagination`, `OrderedIdsSerializer` shared reorder payload, `ModelInspector`, `FileSizeTypeValidator` — the graph analysis identifies these as the codebase's god nodes |
| **API versioning** | `urls_v1.py` split from root `urls.py`; every app has a `v1/` package |
| **Idempotency** | Unique `stripe_event_id` / `event_id` on webhook tables so replays are safe |
| **Atomic transactions** | `transaction.atomic()` around multi-model invitation/user provisioning |
| **Bulk operations over loops** | Reorder endpoints use a single `bulk_update` after ownership validation, not N saves |
| **Explicit `update_fields`** | Writes specify changed fields plus `updated_at` rather than saving whole rows |
| **Defensive validation** | Name normalisation before unique constraints; whole-payload rejection when any ID isn't the caller's; message/metadata size caps with graceful degradation |
| **Security-first defaults** | `StrictDjangoModelPermissions` closing DRF's safe-method gap; SHA-256 hashed OTPs; access token in memory only; refresh rotation + blacklisting; per-scope throttling; documented XSS trade-offs |
| **Observability** | Separate engineering-log and product-analytics planes; non-blocking queue handler with circuit breaker; request-scoped `contextvars`; JSON output for ELK/Datadog/Loki; composite indexes on every query path |
| **Documentation discipline** | 57 KB API reference, 26 KB activity-system doc, 21 KB logging-system doc, per-app READMEs, developer guides, product `Context.md` specs, deployment/CI-CD/S3 guides |
| **Testing** | Django `TestCase` suites for admin console, activity selectors, auth, logs; Vitest + Testing Library on the frontend; Bruno and Postman API collections; Locust load testing on the FastAPI platform; containerised `manage.py test` step inside CI |
| **Code-quality gates in CI** | `makemigrations --check --dry-run` migration-drift gate; ESLint with `--max-warnings 0`; `tsc --noEmit` type-check |
| **AI-assisted, human-owned** | Claude Code / Cursor used as accelerators; each repo carries a hand-written `CONTEXT.md` / `CLAUDE.md` encoding the architectural rules the agent must obey — and on LookUp a formal `ai_rules.md` engineering constitution (performance-first, no placeholders, strict separation of concerns). Architecture, system design and code quality remain mine |
| **Infrastructure ownership without a DevOps team** | No separate DevOps or infra engineer on any project in §7/§8 — Docker, GitHub Actions CI/CD, AWS EC2/IAM/S3/SES/RDS, Nginx/Caddy, database provisioning and server operation are all mine, in addition to the backend itself |
| **Cross-team infrastructure support** | The engineer colleagues come to when a deployment, pipeline, Docker build, AWS setup or hosting problem is blocking *their* project — infrastructure debugging beyond the codebases I wrote (§12) |
| **Client-facing knowledge transfer** | The Tundra `HANDOVER.md` — a 6-chapter guide written for a non-technical owner covering AWS setup through to revoking my own access and rolling the Stripe keys; the ProspectLead `Context.md` product spec; per-app developer guides on every project |
| **Design capability alongside backend** | Omnyvora design system + 4 workspace designs + 33 component specs; ProspectLead landing page and dashboard/auth screens; a written page-by-page visual design critique of the CHYR dashboard; structured design briefs that separate content/structure from styling |
| **Knowledge-graph tooling** | Generated and maintain `graphify-out/` knowledge graphs of both Omnyvora repos (1,304 nodes / 2,511 edges backend; 1,523 nodes / 2,872 edges frontend) to audit coupling, detect import cycles and surface god nodes |

---

## 12. DEVOPS & INFRASTRUCTURE (I do all of this myself — on my projects and on other people's)

> **Agent note — do not under-weight this section.** DevOps is not a sideline next to my backend
> work; it is a co-equal half of what I deliver. On every project listed in §7 and §8 I personally
> did the containerisation, the CI/CD pipeline, the server provisioning, the database setup and
> operation, the object storage, the mail configuration, the reverse proxy and the deployment —
> there is no separate infrastructure engineer on these projects.
>
> **This is context for you, not CV copy.** Give infrastructure real weight in the CV, but write it
> in plain professional register — see the framing rule below.
>
> **And it is not confined to my own projects.** I am the person colleagues at Softvence come to
> when a deployment, a pipeline, a Docker build, an AWS setup or a hosting problem is blocking
> *their* project — I debug and fix other engineers' CI/CD, AWS, Dockerisation and hosting, not
> only my own. Treat this as cross-team infrastructure support, and put it on a CV whenever the JD
> mentions DevOps, deployment, infrastructure, cloud, containers, CI/CD, Linux or mentoring —
> **and also when the JD merely lists Docker, Nginx or AWS in its stack**, because that stack line
> is exactly what this section answers.
>
> *(Recorded 18 Aug 2026, stated directly by me. Scope deliberately kept unquantified — describe it
> as ongoing cross-project support, never with an invented project or colleague count.)*

**Cross-project / cross-team infrastructure support**
- **The person others come to when deployment is the blocker.** I debug and fix **other engineers'
  CI/CD pipelines, AWS setups, Docker builds and hosting** at Softvence, alongside owning my own —
  so the infrastructure knowledge is not confined to the projects I wrote.
- This is unblocking work: a broken pipeline, a container that will not build, a server or hosting
  configuration that will not come up, a cloud account that is not set up right.
- **CV framing — state the work, never the status.** Write it as *"resolve deployment and
  infrastructure issues on colleagues' projects as well as my own — CI/CD pipelines, Docker builds,
  AWS provisioning and hosting configuration"*. **Do not** write "the person everyone comes to",
  "I am the DevOps engineer", "there is no separate infra engineer — I am it", or anything else
  that praises me or reports how colleagues regard me. That reads as arrogance and does not belong
  in a professional document. The facts are strong enough on their own.

**Containerisation**
- Multi-stage Dockerfiles (builder stage compiles wheels into a venv; runtime stage copies only the venv + app code for a lean image), `entrypoint.sh` handling migrations / collectstatic / server launch, `.dockerignore` hygiene.
- Docker Compose stacks deliberately **split by concern** rather than one mega-file: `docker-compose.db.yml`, `docker-compose.local-backend.yml`, `docker-compose.prod-backend.yml` (Omnyvora); `local-api` / `local-db` / `production-api` / `production-db` (ProspectLead, ArchiCoPro, OCReels).
- Production runs Gunicorn (2 workers × 2 threads) or Uvicorn rather than the dev server; pgAdmin bundled in local stacks.

**CI/CD — GitHub Actions (built on 8+ repositories)**
- **CI job:** checkout → `setup-python` → system deps (`build-essential`, `libpq-dev`) → `pip install -r requirements.txt` → prepare CI env from `.env.ci.example` → **`python manage.py makemigrations --check --dry-run`** (fails the build on migration drift) → `docker/setup-buildx-action` → `docker/login-action` → `build-push-action` tagging both `:${{ github.sha }}` and `:latest` → **pull the image back and run `manage.py test` inside the container** so tests execute against the real artefact.
- **CD job:** `appleboy/ssh-action` into the VPS → remove stale images for the repo → **retry loop pulling the new SHA-tagged image** (configurable `MAX_RETRIES` / `RETRY_DELAY` to handle registry propagation) → `docker compose down` → `IMAGE_TAG=<sha> docker compose up -d`.
- **Branch strategy:** `dev_ci.yml` gating the dev branch (build only) and `main_ci_cd.yml` doing full build-push-deploy on `main`; plus a `dummy_action.yml` no-op workflow on personal branches so required-check rules stay satisfied.
- All secrets and environment-specific values injected via **GitHub Secrets and Variables** (SSH key, Docker Hub credentials, image name, Dockerfile path, VPS project directory, compose file, server IP/user/port) — nothing hard-coded.

**Cloud & hosting (hands-on)**
- **AWS:** EC2 (multi-region — Bahrain, Frankfurt, US; Elastic IPs; key-pair management), IAM (per-environment scoped users and access keys), **SES** (DKIM, DMARC and custom MAIL-FROM DNS record configuration), RDS, S3 (with explicit bucket policies), `boto3` / `aioboto3` / `django-storages`.
- **Hostinger VPS** — full provisioning including a dedicated `git_action` deploy user for CI.
- **Cloudflare R2** object storage and CDN origin.
- **PythonAnywhere**, **Render**, **Railway** for earlier personal deployments.
- **Reverse proxies:** Nginx (custom `nginx.conf`, immutable-cache media headers) and **Caddy** (automatic HTTPS; wrote a `deploy_caddy.py` provisioning script and a `CADDY_SETUP.md` guide).
- Server-side backup discipline: container tarballs, database dumps, environment-variable and nginx-config backups kept per project.

**Data & runtime services**
- PostgreSQL (primary), MySQL, SQLite (WAL mode), Redis 7 (cache backend, Celery broker + result backend, OTP store, channel layer), Celery worker + Celery Beat with isolated queues and heartbeat-based liveness checks.

---

## 13. CONFIDENTIALITY & WHAT MAY BE PUBLISHED

| Category | On a CV? |
|---|---|
| Softvence client **source code** | ❌ Never — private org repos under NDA |
| Softvence client **internal folder/account names** (`ahmadaoosaq123`, `benkelly864`, …) | ❌ Never — these are internal references only |
| **What I built + technologies used** on client projects | ✅ Yes — this is the standard, expected way to describe agency work |
| **Public product URLs** (ocreels.com, prospectlead.ai, thundra.de, archicopro.cloud) | ✅ Yes — publicly live products |
| Server IPs, SSH keys, `.pem` files, IAM access keys, database passwords, API keys | ❌ **Never, under any circumstance** |
| Omnyvora repos (own organisation) | ✅ Yes — link freely |
| Personal GitHub repos | ✅ Yes — link freely |
| Client budget figures (e.g. SafeTag $9,000) | ⚠️ Only if the JD is pre-sales/consulting-oriented and the framing is neutral; otherwise omit |

---

## 14. LEGACY PORTFOLIO DATABASE (`db.sqlite3`) — EXTRACTED CONTENT

> **What this file is:** the SQLite database from my Django portfolio site (`my_portfolio_v1` / `landing_spot` + `resume` apps), last updated around September 2025. It captures my profile *as of ~one year ago*. **Everything in §4, §7 and §8 supersedes it.** It remains valuable for: pre-written CV bullet text, my earlier project catalogue, education/certification records, and references.

**Tables and counts (all 26 tables audited):** `landing_spot_user` (2 — one superuser, one me), `landing_spot_experience` (2), `landing_spot_education` (3), `landing_spot_certification` (3), `landing_spot_service` (5), `landing_spot_skillcategory` (10), `landing_spot_skill` (26), `landing_spot_projectcategory` (20), `landing_spot_project` (27, of which 3 are throwaway test rows), `landing_spot_project_categories` (56 tag links), `landing_spot_contact` (**112 real enquiries received through the site's contact form**, with a seen/unseen flag), `resume_resume` (2), `resume_reference` (2), `resume_resumeproject` (8), `resume_resumecertificate` (3), `resume_resumereference` (2), plus Django's `auth_*` (one custom group, "General Users"), `django_admin_log` (109 admin actions between 3 Jun 2025 and 19 Aug 2025 — the site's real operating window), `django_content_type`, `django_migrations` (43 across the `landing_spot` and `resume` apps) and `django_session`.

**Project categories used for tagging (20):** PHP · Python · Python-Django · C++ · JavaScript · HTML/CSS · C# · React · Node · Flutter · JAVA · Electronics · Arduino · Academic · MySQL · Other · Bootstrap · ESP-866 · SQLite · Redis.

### 14.1 — Self-description on file (2025)
> *"Hello! I'm Hassan, a passionate Python-Django Backend Developer with a knack for turning ideas into scalable, efficient systems. My journey in tech blends hardware tinkering with software craftsmanship — whether it's building web APIs or innovating data transmission methods like Li-Fi using RGB light."* — Tagline: *"Web Developer | CSE Graduate"*. Meta description on file: *"Abdullah Md Jahid Hassan – A Python-Django backend developer passionate about scalable web solutions, with experience in software engineering, electronics, and Li-Fi research."*

### 14.2 — Services offered (from the portfolio site)
1. **Backend Development** — custom Django web applications; REST API development & integration; database design & optimisation (MySQL, PostgreSQL); authentication systems (JWT, OAuth).
2. **Full-Stack Solutions** — dynamic Django + HTML/CSS/JS sites; ISP/enterprise management systems; **PHP-to-Django migration** (legacy system upgrades).
3. **IoT & Hardware-Software Integration** — Arduino/Raspberry Pi prototypes; sensor data processing (Li-Fi, RGB light systems); custom electronics-software interfacing.
4. **Technical Consultation** — Li-Fi/optical communication concepts; academic/thesis project guidance; debugging & performance optimisation.
5. **Freelance Support** — small-business web solutions; Python automation scripts; technical documentation.

### 14.3 — Self-rated skill percentages as of 2025 *(historical — treat §15 as current)*
Django 95 · PHP 95 · Bootstrap 95 · Git 95 · Arduino 95 · Li-Fi 95 · VS Code 95 · MS Office 95 · C++ 95 · Cursor AI 95 · MySQL 90 · SQL Queries 90 · GitHub 90 · Sensors 90 · Web Scraping 90 · C 90 · Python 85 · CSS 85 · JavaScript 85 · Parallel Data Transmission 85 · PyCharm 85 · Docker 85 · Django Tenant 85 · REST 80 · C# 60 · Java 60.
*(Skill categories used: Programming Languages · Backend Development · Frontend Development · Database · Version Control · Technologies · Tools · Hardware & Embedded Systems · Networking · Soft Skills.)*

### 14.4 — Pre-written résumé variants already in the database
**Variant A — "General Purpose"** (was the active one):
> *"Motivated and detail-oriented Computer Science Engineering graduate with a strong foundation in software development. Proficient in C, C++, Java, C#, and PHP, with hands-on experience in full-stack development through an ISP system project using HTML, CSS, Bootstrap, PHP, and MySQL. Currently enhancing skills in Python and Django by working on real-world projects. A fast learner with a problem-solving mindset, highly organized, and eager to contribute technical expertise in a dynamic work environment."*
> Featured projects (in order): Portfolio Website → Personal Assets Management → ISP Management System → Li-Fi Thesis.

**Variant B — "DevOps"**:
> *"A Computer Science graduate with hands-on experience in full-stack development and a growing specialization in DevOps practices. Adept at building and deploying web applications using Python (Django), PHP, MySQL, and version control tools like Git. Familiar with CI/CD pipelines, containerization (Docker), Linux environments, and cloud-based deployment (PythonAnywhere, Render, and Railway)…"*

> ⚠️ **Both summaries are now badly out of date and understate me.** Use §3 instead. They are recorded here only to show the CV-variant system already existed and for tone reference.

### 14.5 — References on file
| Name | Designation | Institution | Contact |
|---|---|---|---|
| **Rashedul Islam** | Assistant Professor & Coordinator | IUBAT — International University of Business Agriculture and Technology | rashed@iubat.edu · +880 1776 445218 |
| **Adil Sadman** | Coordinator | Quantanite Bangladesh Ltd. | +880 1837 267804 |
*(Include references only when the JD explicitly requests them; otherwise write "References available on request.")*

---

## 15. CURRENT SKILLS MATRIX (2026 — authoritative)

### Languages
**Python** (primary, expert) · **JavaScript / TypeScript** (professional) · **SQL** (professional) · **PHP** (professional, legacy) · **C / C++** (academic + embedded) · **HTML5 / CSS3** · **C# / .NET 6** (substantial university coursework — 7 labs, lab test and a final assignment as full Visual Studio solutions; see §9.9) · **Java** (university coursework, NetBeans) · Bash / Shell scripting · Dart (Flutter — specified and scoped, not primary)

### Backend frameworks & libraries
**Django 5.2** · **Django REST Framework 3.16** · **FastAPI 0.119** · **Django Channels** (WebSockets) · Daphne / ASGI · Gunicorn / WSGI · Uvicorn · **Celery 5 + Celery Beat** · APScheduler · `djangorestframework-simplejwt` · `django-allauth` / `dj-rest-auth` (social login) · `django-cors-headers` · `django-filter` · `django-storages` · `django-redis` · `drf-yasg` / Swagger / OpenAPI · `drf-spectacular` · `drf-nested-routers` · `django-extensions` · `python-decouple` · Pydantic v2 + pydantic-settings · `phonenumbers` · Pillow · `pyotp` (TOTP) · passlib / bcrypt · python-jose / PyJWT

### ORMs & databases
**PostgreSQL** (primary; psycopg3, asyncpg) · **MySQL** (PyMySQL, aiomysql) · **SQLite** · **Redis 7** · **Django ORM** (select/prefetch related, `bulk_update`, composite indexes, constraints, custom managers, soft delete, custom on-delete handlers) · **Tortoise ORM 0.25 + Aerich migrations** · Database design, normalisation, ERD modelling, query optimisation, N+1 elimination

### Frontend
**Next.js 16** (App Router, route groups, server/client components, loading & error boundaries) · **React 19** · **TypeScript 5** · **Tailwind CSS 4** · **shadcn/ui + Radix UI** · **TanStack React Query 5** · **Zustand 5** · **React Hook Form + Zod** · **dnd-kit** · Axios (interceptors, silent refresh, request queueing) · `next-themes` · `lucide-react` · `sonner` · Vite · Redux Toolkit + redux-persist · React Router · Bootstrap 5 · jQuery-era libraries (AOS, Isotope, GLightbox, Swiper) · i18next · hls.js · Framer Motion · TipTap · Recharts

### DevOps, cloud & tooling
**Docker** (multi-stage builds) · **Docker Compose** · **GitHub Actions** (CI/CD) · **AWS** (EC2, IAM, SES, S3, RDS) · **Hostinger VPS** · **Cloudflare R2** · **Nginx** · **Caddy** · PythonAnywhere / Render / Railway · Linux server administration · SSH key management · `git` / GitHub (branching strategies, PR workflows) · pnpm / npm / `uv` / Poetry · pgAdmin / phpMyAdmin

### Testing & quality
Django `TestCase` · pytest + pytest-asyncio · **Vitest 4** + Testing Library + jsdom · **Bruno** API collections · **Postman** collections · **Locust** load testing · ESLint 9 · `tsc --noEmit` · flake8 · Sentry · migration-drift gating in CI

### Integrations & third-party platforms
**Stripe** (subscriptions, plans, products/prices, checkout sessions, invoices, webhooks, Stripe CLI) · **Tap Payments** · **OpenAI API** (with cost/token accounting) · **google-genai** · **ElevenLabs** · **Twilio** (SMS + telephony) · **Firebase** (Cloud Messaging, Firestore, Admin SDK) · **Cal.com** · **Google Calendar API** · **Calendly** · **MindBody** · **Google OAuth 2.0** · **n8n** (webhook automation contracts) · **Resend** · SMTP / AWS SES / SendGrid · Cloudinary · Google Maps Platform · ffmpeg

### Design & product
UI/UX design · Design systems & design tokens · Component library specification · Light/dark theming · Brand identity & logo design · Typography systems · Content design / UX writing · Design critique & review · Writing structured design briefs · Wireframe-to-implementation translation · Information architecture · Figma-adjacent design-canvas workflows · **n8n workflow building** (Google Maps scraping + AI extraction pipeline) · Product specification authoring

### Architecture & design patterns
Modular monolith · Domain-driven design & bounded contexts · Service layer / selector pattern · Repository-ish separation · Soft correlation keys over cross-domain FKs · REST API design & versioning · Unified response envelope · Multi-tenancy · **Django Tenant** · RBAC & permission groups · JWT auth with rotation/blacklisting · OTP flows · Webhook idempotency · Event-driven & signal-driven design · Background job queues with isolated routing · Caching strategies · Rate limiting / throttling · Soft delete · Audit logging · Feature flags & DB-driven configuration · Design tokens & theming systems

### Software engineering process (formally trained + practised)
Requirement analysis & elicitation · Functional / non-functional requirement specification · **Use case diagrams** · **Activity diagrams** · **Swimlane diagrams** · **Entity-Relationship Diagrams (ERD)** · **Data-Flow Diagrams (DFD) to level 4** · **Function point estimation & function-oriented metrics** · Process-based estimation · Effort distribution & task scheduling · **Cost estimation** (personnel / infrastructure / third-party) · **Feasibility assessment & feasibility matrices** · **Risk assessment & RMMM planning** · SDLC methodologies · Technical writing & API documentation · Client hand-over documentation

### Hardware & embedded
Arduino (UNO, IDE, C++) · **ESP8266 / ESP-01** · Sensor interfacing (RGB colour sensors, LDR, IR LED, photodiode, **turbidity sensors**, temperature sensors, counters) · **Li-Fi / optical wireless communication** · Parallel data transmission · Power electronics (buck converters, BMS, Li-ion pack assembly, reverse-polarity protection, heat dissipation) · Multimeter / load-tester validation · Soldering, enclosure fabrication & prototyping · IoT web interfaces · Wireless network security experimentation (ESP8266 evil-twin lab work)

### AI-assisted development
Claude Code · Cursor · Agent-API-driven workflows · Writing `CONTEXT.md` / `CLAUDE.md` architectural constitutions for agents · Knowledge-graph codebase analysis (graphify) · **Explicit stance: AI accelerates output; architecture, system design and code quality remain human-owned.**

### Professional / soft skills
End-to-end project ownership · Cross-functional collaboration (frontend, design, PM) · Client communication & requirement gathering · Technical documentation & knowledge transfer · Mentoring through documentation · Fast self-directed learning · Problem-solving · Attention to detail & code quality standards · Working to deadlines in an agency environment · Remote collaboration with international clients (US, Germany, Middle East, Brazil, Australia)

---

## 16. ATS KEYWORD BANK

> Pull only the terms the JD actually uses. Every keyword below is legitimately backed by evidence in this file.

**Core:** Python, Django, Django REST Framework, DRF, FastAPI, REST API, RESTful API, API development, backend development, backend engineer, software engineer, web development, full-stack, microservices, modular monolith, SaaS, multi-tenant, API integration, third-party integration

**Data:** PostgreSQL, MySQL, SQLite, Redis, SQL, ORM, Django ORM, Tortoise ORM, database design, schema design, data modelling, normalisation, ERD, query optimisation, indexing, migrations, Aerich, caching

**Async / real-time:** Celery, Celery Beat, background tasks, asynchronous task processing, task queue, message broker, WebSockets, Django Channels, ASGI, Daphne, real-time, async/await, asyncio, APScheduler, cron scheduling

**Auth & security:** JWT, OAuth 2.0, Google OAuth, SimpleJWT, token refresh, token rotation, token blacklisting, OTP, two-factor authentication, TOTP, RBAC, role-based access control, permissions, authentication, authorisation, rate limiting, throttling, bcrypt, password hashing, CORS, CSRF

**DevOps:** Docker, Docker Compose, containerisation, Dockerisation, multi-stage build, CI/CD, GitHub Actions, continuous integration, continuous deployment, pipeline, build pipeline, deployment pipeline, AWS, EC2, IAM, S3, S3 bucket, SES, SMTP, RDS, Cloudflare R2, VPS, Hostinger, Nginx, Caddy, reverse proxy, Gunicorn, Uvicorn, Linux, Linux server administration, server management, SSH, deployment, release management, infrastructure, infrastructure as ownership, cloud infrastructure, provisioning, environment configuration, secrets management, monitoring, health checks, logging, observability, structured logging, backup and recovery, troubleshooting, production support

**Frontend:** Next.js, React, TypeScript, JavaScript, Tailwind CSS, shadcn/ui, Radix UI, TanStack Query, React Query, Zustand, Redux, Redux Toolkit, React Hook Form, Zod, Vite, responsive design, UI/UX, design system, design tokens, accessibility, dark mode, i18n, internationalisation, PWA

**Payments & AI:** Stripe, Stripe subscriptions, Stripe webhooks, payment gateway integration, billing, invoicing, subscription management, credit system, Tap Payments, OpenAI, OpenAI API, LLM integration, AI integration, ElevenLabs, text-to-speech, Twilio, SMS, Firebase, FCM, push notifications, n8n, workflow automation

**Process:** Agile, SDLC, requirement analysis, requirement engineering, system design, software architecture, technical documentation, API documentation, Swagger, OpenAPI, UML, use case diagram, activity diagram, swimlane diagram, data flow diagram, DFD, cost estimation, function point analysis, feasibility study, risk assessment, RMMM, unit testing, integration testing, TDD-adjacent, code review, Git, version control, branching strategy, pull requests, Agile collaboration

**Design & product:** UI/UX, UI/UX design, design system, design tokens, component library, theming, wireframes, information architecture, design review, design critique, UX writing, content design, brand identity, typography, product specification, n8n, workflow automation, no-code automation, web scraping, Google Maps scraping

**Documentation & handover:** technical documentation, technical writing, API documentation, developer guides, onboarding documentation, knowledge transfer, project handover, client handover, runbook, deployment guide, requirement specification, statement of work, SOW, product specification

**Legacy/other:** PHP, Bootstrap, HTML5, CSS3, jQuery, C, C++, Java, C#, .NET, .NET 6, NetBeans, Visual Studio, OpenGL, computer graphics, compiler design, data structures, algorithms, DBMS, operating systems, Arduino, ESP8266, IoT, embedded systems, firmware, sensors, Li-Fi, optical communication, Flutter, Dart, Jupyter, pandas-adjacent data work

---

## 17. DATA HYGIENE — THINGS TO VERIFY OR FIX

### 17.1 — CGPA discrepancy ⚠️
The structured education record in `db.sqlite3` says **3.59 / 4.00**; my older written bio (in the same database and in my GitHub profile README) says **3.42**. **Confirm the correct figure against the official transcript before printing it on a CV.** I have used 3.59 in §5 because it is the structured, more recently edited field.

### 17.2 — Stale sources (do not treat as current)
- `db.sqlite3` — snapshot from ~September 2025; predates all Softvence client work, Omnyvora, FastAPI, AWS, CI/CD.
- GitHub profile README (`abdullah-md-jahid-hassan/README.md`) — written mid-2025, still describes me as an intern-level PHP/Django learner, links to two repository URLs that no longer resolve (`My_portfolio`, `ISP-Management-System`, `li-fi-parallel-rgb`). **Worth updating.**
- `omnyvora-backend/README.md` and `docs/README.md` describe the pre-refactor flat app layout (`authentication/`, `otp/`, `emails/`, `logs/`) — the code has since moved to `shared/<domain>/`. The graph analysis flags this doc-vs-code drift. **Worth updating.**

### 17.3 — Security finding surfaced during this audit 🔴
`Softvence\Projects\hawiisaac\Code\hawiisaac\firebase.json` contains a **live Firebase service-account private key in plaintext** inside a git-tracked repository (project `hykx-4b453`). Several project folders also store `.pem` keys, IAM credential CSVs and plaintext server passwords alongside the code. None of this is in this README and none of it should ever reach a CV — but the Firebase key in particular should be **revoked and rotated**, and the file removed from git history and moved to a secret manager.

### 17.4 — Empty / placeholder items to ignore
`Shortcut-APP` (README only, no code) · three "Temp project" rows in the portfolio project table · the `Templet` and `karolin` project folders (scaffolding/credentials only) · the `Trash/` folder (archived engagements).

### 17.5 — Web presence: dead and stale links 🔴
*Recorded 25 July 2026, stated directly by me. This governs every link an agent prints.*

| Link | Status | May it go on a CV? |
|---|---|---|
| `amjh.space` | 🔴 **Domain expired** | ❌ **Never.** Remove from any CV, cover letter or profile. A dead link on a CV reads as carelessness and is worse than no link. |
| `isp.amjh.space` (ISP Management System demo) | 🔴 **Dead** — subdomain of the expired domain | ❌ No. Describe the project; link the GitHub repo instead. |
| `abdullahmdjahidhassan.pythonanywhere.com` | ⚠️ **Live, but ~1 year stale.** Content reflects ~Sept 2025: no Softvence client work, no Omnyvora, no FastAPI, AWS, Docker or CI/CD. Understates me significantly. | ⚠️ Only if a JD explicitly demands a live portfolio URL and no better option exists. **Tell me before including it.** Prefer GitHub links (personal + Omnyvora org), which are current. |

**Safe, current links to use instead:** GitHub `abdullah-md-jahid-hassan` · Omnyvora org `github.com/orgs/omnyvora/repositories` · LinkedIn · the public client product URLs in §13 (ocreels.com, prospectlead.ai, thundra.de, archicopro.cloud).

**Planned, not yet done (do not reference as if it exists):**
1. Register a **new domain** to replace `amjh.space`.
2. Build a **new portfolio site** from current data — the existing one is a year behind. Stack, audience and visual direction are all still undecided.
3. Optionally refresh `db.sqlite3` (the `my_portfolio_v1` content DB) so the portfolio has current content to serve. **Deferred deliberately** — the portfolio work is not blocked on it and neither is anything else; §14 is already extracted, so per `CLAUDE.md` do not re-parse the DB unless asked.

*Until item 1 and 2 land, treat this profile and my CVs as my web presence, and lean on GitHub for anything that needs to be clickable.*

---

## 18. SOURCE INDEX — WHERE EVERYTHING IN THIS FILE CAME FROM

| Source | What it provided |
|---|---|
| `db.sqlite3` (this folder) | Identity, contact, education, certifications, pre-2025 projects, skills, services, references, résumé variants — §1, §5, §6, §14 |
| `my-projects/omnyvora-backend/` | Full source: 20 apps, models, services, selectors, settings, permissions, Docker, CI/CD workflows, `docs/`, `developer_guide/`, `graphify-out/GRAPH_REPORT.md`, git history — §8.1 |
| `my-projects/omnyvora-frontend/` | Full source: `src/`, `package.json`, `documentation/routes.md`, `core/design/TOKENS.md`, `ui_ux/` design system + 33 component previews, git history — §8.2, §8.3 |
| `C:\Users\abdul_m1\Softvence\Projects\` | All 14 client project folders: source code, models, settings, `requirements.txt`, `.github/workflows/`, docs, `Context.md` specs, git commit authorship — §7 |
| GitHub API — `abdullah-md-jahid-hassan` | 27 repositories with languages, dates and sizes; file trees; raw READMEs and `CONTEXT.md` files — §9 |
| GitHub API — `omnyvora` org, `am-jahid-hassan` | Repository metadata and account confirmation — §1, §8 |
| `frogman58/Doc/System_Design_SafeTag_v2.md` | The 9-chapter system design document — §7.9 |
| `mystore2020/code/.claude/Context.md` | ProspectLead product specification — §7.3 |
| `kilian_rohde/Hand over/HANDOVER.md` + `handover-message.txt` | The 6-chapter client handover guide and three-service architecture — §7.4 |
| `benkelly864/code/.../Ai_Prompts/ai_rules.md` + `benkelly864/Docs/` | AI engineering constitution; LookUp gamification specs — §7.5 |
| `ahmadaoosaq123/source/chyr-*.html`, `Doc/` | CHYR branding, design critique, dev brief, SOW, requirement call recordings — §7.1 |
| `mystore2020/code/ui-ux/`, `mystore2020/n8n/src/` | ProspectLead UI/UX designs and the Google Maps Scraper n8n workflow — §7.3 |
| GitHub API — `All-Code` tree (2,950 files) | C#/.NET, Java, OpenGL, C/C++, PHP, Arduino, ESP8266 and EDGE coursework — §9.9 |
| GitHub API — `Personal_assets_management` tree + `assets/models.py` | Polymorphic asset schema and API/verification apps — §9.6 |

---

*Maintenance note: rebuild this file whenever a project ships, a role changes, or a new technology enters production use. The rebuild procedure is: dump `db.sqlite3` → walk every folder under `Softvence\Projects` reading models/settings/workflows → read both Omnyvora repos including source and git log → query the GitHub API for repo metadata, trees and raw READMEs → regenerate §7–§9 → re-check §17.*
