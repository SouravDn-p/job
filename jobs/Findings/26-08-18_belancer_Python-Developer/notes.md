# Belancer — Python Developer

**Priority tier:** 3 — on-site in Bangladesh (Panthapath, Dhaka). No remote option is offered and it
is not a government post, so it cannot rank higher. It is a genuine stack fit, which is why it is
worth building for at all: the JD's Core Stack (Python · FastAPI · PostgreSQL · REST API · Docker ·
Nginx · AWS · Git/GitHub) is claimable line-for-line from `PROFILE.md`, and the "strong advantage"
list — marketplaces, fintech, payment systems, wallets, high-traffic platforms — hits four separate
production projects.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-18 |
| Applied | *(not yet — status is Draft)* |
| Source | Facebook post, Belancer company page — https://www.facebook.com/share/p/192L5o67NX/ |
| Location / type | Panthapath, Dhaka · Full-time, **on-site** |
| Posted | **Not stated on the shared post — unverified.** Treated as escalated per `CLAUDE.md` rule 6 |
| Deadline | None stated |
| Reference / application ID | — |
| Contact | jobs@belancer.com (apply by email, CV attached) |
| Salary discussed | Advertised BDT 40,000–50,000/month — see knockouts |
| Openings | 3 |

## CV decisions

- **Summary variant used:** §3.1 (General Python Backend Developer), rewritten FastAPI-first and
  re-pointed at this JD's advantage list. The stated "2+ years" figure from §3.1 was **removed** —
  see the years knockout below.
- **Projects featured:**
  1. **Outdoorda** — the single most on-point project in the whole profile. A real two-sided
     marketplace (customers ↔ field installers) with separate `Payment` and `Payout` models,
     service areas, availability windows, ratings and admin-editable commission/payout terms.
     Belancer *is* a freelancing marketplace, so this leads.
  2. **OCReels** — the high-traffic exhibit. FastAPI, CDN-fronted media, immutable cache headers,
     Locust load testing, Sentry, a six-domain CORS estate, plus a creator earnings ledger.
  3. **ProspectLead** — the wallet exhibit. Append-only credit ledger with a running-balance
     snapshot per row, reserve-on-submit / finalise-on-callback, idempotent Stripe webhooks.
  4. **CHYR** — the payment-systems exhibit. Dual payment-provider abstraction across Stripe and
     Tap Payments with a retry/dunning state machine.
  - Tail line carries ArchiCoPro (FastAPI, lead backend developer), Tundra (three-service estate,
    each service independently containerised with its own CI/CD pipeline — plus the client
    server-setup and handover guide he wrote) and LookUp.
- **Keywords targeted (literal JD phrases):** Python · FastAPI · PostgreSQL · REST API · Docker ·
  Nginx · AWS · Git/GitHub · "REST API development and integration" · "database design &
  optimization" · "Authentication, security & backend architecture" · "Docker/Linux production
  environment" · debugging · marketplaces · payment systems · wallets · high-traffic platforms.
  The skills section is deliberately laid out in the JD's own order, and a seventh row —
  *Marketplace, payments & high-traffic platforms* — exists purely to answer the advantage clause.
- **DevOps weighting — revised 2026-08-18 after Abdullah's correction.** The first build carried
  infrastructure as one skills row and one bullet, and cut the closing deployment section for page
  budget. That under-sold him and was the wrong thing to cut for a JD whose Core Stack names Docker,
  Nginx and AWS outright. The CV now states it in the summary (*"there is no separate DevOps
  engineer on my projects — I am it"*), gives it a dedicated experience bullet, adds a second bullet
  for the **cross-team** work (unblocking colleagues' pipelines, Docker builds, AWS and hosting),
  widens the infrastructure skills row to S3 bucket policies and SES/SMTP with DKIM and DMARC, and
  closes with a dedicated **Infrastructure & Deployment** section.
- **Register corrected — second pass, same day.** The DevOps revision above initially overcorrected
  into self-congratulation: the summary read *"There is no separate DevOps engineer on my projects —
  I am it… colleagues bring me their pipelines"*, and bullets used *"all mine"*, *"the person
  colleagues come to"*, *"rather than guesswork"*, *"rather than for a demo"*, *"rather than
  tenure"*. Abdullah called it arrogant and not how professional documents are written; he was
  right. Every one of those was rewritten to state the scope of the work and stop — e.g. *"Own the
  infrastructure alongside the application code on every project — Docker images, GitHub Actions
  CI/CD, Linux server provisioning, database setup and backups, S3 buckets and policies, SES/SMTP
  with DKIM and DMARC records, Nginx or Caddy as reverse proxy"*. The evidence is unchanged and the
  weighting is unchanged; only the voice is. **The lesson generalises and is now recorded** in
  `CLAUDE.md` § Write it in professional register, in `SKILL.md` (content rules + a grep-based
  register check in the gate-3 self-check), and in `PROFILE.md` §12, whose "good CV framing" line
  had itself been written badly and was instructing future builds to repeat the mistake. Room was made by tightening the
  projects section — no evidence was dropped. `PROFILE.md` §12, §4.1, §11 and §16 were updated in
  the same pass, since the cross-team support was not previously recorded anywhere.
- **Deliberately omitted:**
  - **No years total anywhere on the page.** Exact dates are printed (Aug 2025 – Present at
    Softvence, Feb – Jul 2024 internship) so any reader can compute it. §3.1's "2+ years" line was
    cut rather than reproduced, because against a 5+ year gate a stated total is a number to be
    argued about; the dates are the honest version.
  - **No escrow claim.** A freelancing marketplace runs on escrow and Belancer will probe it.
    Escrow is absent from `PROFILE.md`, so it appears nowhere — not even softened.
  - Kubernetes, RabbitMQ, Kafka, SQLAlchemy — all absent from the profile, all absent here.
  - `django_templet` was dropped from the tail line to make room for the infrastructure content;
    it is personal tooling, and the client work carries the same evidence more strongly here.
  - Caddy is named separately from Nginx rather than folded into it. Nginx is claimed on Outdoorda
    (reverse proxy) and OCReels (media cache headers) — both real.
- **Knockouts:**
  - 🔴 **"Experience: 5+ Years" — the largest experience gap in this log to date.** Professional
    experience begins 16 Aug 2025 (~1 year), or ~2.5 years counting the 2024 internship and the
    self-directed Python year. Flyte Solutions asked 3–5 and was already the previous record.
    This is a real filter and may end the application at the CV stage.
  - 🟠 **Salary BDT 40,000–50,000/month.** Bohubrihi's 50,000–70,000 band was recorded as a likely
    pay cut, so this band is almost certainly below current compensation. Confirm before applying.
  - 🟠 **On-site, Panthapath.** Home is Uttara 10 — a long cross-city commute, materially worse
    than the current Mohakhali office.
  - ✅ **NOT a knockout — Docker/Nginx/AWS on the same seat is a strength here, not a risk.**
    The first draft of these notes flagged this as a 🟡 concern by over-applying the Foodi filter.
    That was wrong and has been corrected. Foodi was declined because one seat carried DevOps
    *plus* microservices *plus* backend — a judgement about **role shape**, never about capability.
    Belancer simply lists the stack Abdullah already owns: there is no separate DevOps engineer on
    any of his projects, and he additionally unblocks colleagues' CI/CD, Docker, AWS and hosting
    on *their* projects (`PROFILE.md` §12). This clause is a reason to apply, not a caution.
  - 🟡 **Posting date unverifiable.** A Facebook share carries no visible date, and no deadline is
    stated. Escalated and unverified — apply immediately or re-check before building further.
  - ⚠️ **CGPA 3.59/4.00 is unverified** — one older source says 3.42 (`PROFILE.md` §17.1). It is
    printed on this CV. Verify against the transcript before sending.
- **Weak spots — prepare answers:**
  - "You have one year professional experience and we asked for five." The honest answer is the
    delivery record: eight production backends in eleven months, four on FastAPI, and a promotion
    from Junior Python Developer to Senior Python Executive inside that window.
  - **Escrow and dispute handling.** Never built. Adjacent evidence: reserve-on-submit /
    finalise-on-callback credit semantics on ProspectLead, and the Payment/Payout split on
    Outdoorda. Say what it is — adjacent, not the same thing.
  - **Scale numbers.** OCReels is described with concrete scope (CDN, six domains, Locust) rather
    than user or request figures, because the profile records none. Do not invent one if asked —
    give the architecture instead.
  - **Marketplace domain depth.** Outdoorda was a six-week engagement (Jun 2026), the shortest of
    the four featured projects. Know it well before interviewing.

## Assets used

- Layout: `Assets/CV Templates/cv_temp_1.png` — single column, left-aligned rules, photo top-right.
  Same skeleton as the Exabyting / Flyte / Foodi builds.
- Photo: `Assets/Profile Pictures/Formal profile picture .png`, copied into this folder as
  `profile-photo.png`. Included because this is a local Bangladeshi on-site application, where a
  headshot is expected.

## Build verification

- Rendered by `tools/html_2_pdf` (Chrome headless): **2 pages**, page 1 fill **99.9%**, page 2 fill
  **92.9%** — passes the ≥90% / ≥75% fill test.
- Text layer verified with PyMuPDF: 1,685 words extract as real text; name, title, contact, all six
  section headings and every JD keyword present; no forbidden strings (`amjh.space`,
  `pythonanywhere`, client internal folder names, `3.42`, `escrow`).
- Built HTML-first per the new `SKILL.md` § Step 5a. Three renders total for this job — initial
  build, DevOps rebalance, register correction — each preceded by markup-level review and estimation,
  with no render-inspect-render loop in any of them.
- Register swept programmatically over the rendered text: no `I am`, `all mine`, `myself`,
  `the person`, `comes to me`, `rather than`, `passionate`, `proven track record` or `expert`.
- All dates extract as `Mon YYYY – Mon YYYY`; no numeric dates, no "to" as a joiner.
- Page images inspected — no stranded headings, no bad page breaks. Body copy justified.

## Status timeline

- 2026-08-18 — Found (Facebook post supplied by Abdullah)
- 2026-08-18 — Draft (CV built and rendered; not yet sent)
- 2026-08-18 — CV revised: DevOps and infrastructure ownership given proper weight after Abdullah
  pointed out it was under-represented. `PROFILE.md` updated in the same pass to record the
  cross-team infrastructure support, which it had never captured. Still Draft, still not sent.
- 2026-08-18 — CV revised again: the DevOps wording was boastful and unprofessional. Rewritten in
  plain professional register; evidence and weighting unchanged. Register rule recorded in
  `CLAUDE.md`, `SKILL.md` and `PROFILE.md` §12 so it does not recur. Still Draft, still not sent.

## Interview prep

*(to be filled in after contact)*
