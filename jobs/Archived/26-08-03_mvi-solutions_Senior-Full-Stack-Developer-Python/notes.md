# MVI Solutions — Senior Full Stack Developer (Python)

## 🗄️ ARCHIVED 2026-08-04 — deadline expired

The BDJobs deadline had **already passed** when the listing was checked in a browser on 2026-08-04 —
resolving the unknown posting date recorded below. Never applied. Kept on record so this posting is
not surfaced again; if MVI re-advertises with a fresh date it can be logged as a new job. The stack
fit was the strongest of the tier-3 set, so a repost is worth catching early.

**Priority tier:** **3 — On-site Bangladesh (Dhaka).** The fallback tier, but the best stack fit in it.

## Application

| Field | Value |
|---|---|
| Found | 2026-08-03 |
| Applied | — |
| Source | BD Tech Jobs → BDJobs |
| Location / type | Dhaka · on-site · full-time |
| Deadline | Not stated |
| **Posted** | 🔴 **UNKNOWN** — no date on BD Tech Jobs (`/jobs/291`), none on the BDJobs detail page (`1506018`, JavaScript-rendered), none found via search on 2026-08-04. |
| **Admission test** | 🔴 **CANNOT BE RUN → treated as ESCALATED and unverified** (`CLAUDE.md` § Deadline first, rule 6). No deadline is recorded *and* no posting date could be found, so neither test can be applied. **Open `bdjobs.com/h/details/1506018` in a browser and read both the "Application Deadline" and the "Published on" lines.** A live deadline admits it outright; if there is none and it is 31+ days old, this folder gets deleted. |

## Why this leads tier 3

**Django, Django REST Framework, RESTful APIs, PostgreSQL, AWS, CI/CD pipelines, Redis** — every
one of those is core, evidenced, daily-use experience (§4.1, §7.3, §8.1, §12). There is almost
nothing on this posting he has to reach for, which is unusual.

The salary band tops out at **150,000 BDT**, the second-highest of the on-site set and a plausible
step up rather than sideways.

## Fit detail

| They ask | He has | Verdict |
|---|---|---|
| Python, Django, DRF, RESTful APIs | Eight production backends; DRF on four, FastAPI on four (§4.1) | ✅ Strong |
| SQL, PostgreSQL | Primary database everywhere; schema design, indexing, N+1 elimination (§15) | ✅ Strong |
| AWS | EC2 multi-region, IAM, SES, S3, RDS — provisioned personally (§12) | ✅ Strong |
| CI/CD pipelines | GitHub Actions across 8+ repos, build→push→SSH deploy (§12) | ✅ Strong |
| Redis | Cache, Celery broker, OTP store, channel layer (§12) | ✅ Strong |
| Memcached | Never used | ⚠️ Minor — Redis covers the concept; say so honestly |
| JavaScript, HTML5, CSS3, jQuery, AJAX | Professional JS/TS; jQuery-era libraries (AOS, Isotope, GLightbox, Swiper) listed in §15 | ✅ but dated relative to his Next.js 16 / React 19 work |
| **5+ years** | **~2 years professional** | ❌ **The one real gap** |

## Knockouts

1. **5+ years experience.** Same gap as Search Atlas. Argue scope and trajectory — eight production
   backends in eleven months, junior → senior promotion inside that window — not duration.
2. **On-site Dhaka.** He is currently on-site at Softvence (Mohakhali), so this is a lateral move on
   working conditions with no remote upside. That is the whole reason it is tier 3.
3. The frontend expectation is jQuery/AJAX-era. Worth asking whether the frontend is legacy
   maintenance — it would be a step backwards from the Next.js work.

## CV decisions

**File:** `cv.html` → `Abdullah_Md_Jahid_Hassan_CV_Senior_Full_Stack_Developer_Python.pdf` ·
**verified 2 pages** (page 1 98% full, page 2 79%), selectable text layer confirmed.
Headshot included (`profile-photo.png`) — Bangladesh market.

- **Summary variant used:** §3.2 (Senior / lead-leaning backend) with §3.1's stack vocabulary folded
  in, so the posting's exact terms — Python, Django, Django REST Framework, RESTful APIs, PostgreSQL,
  Redis, AWS, CI/CD pipelines — all appear in the top third.
- **Projects featured:** ProspectLead (DRF + PostgreSQL + Redis + Celery + AWS, lead dev) · Tundra
  (Django REST backend, AWS EC2 + S3 + IAM, N+1 elimination pass) · CHYR (two-region AWS, SES with
  DKIM/DMARC). All three chosen because they let the AWS and CI/CD claims be *shown*, not listed.
- **Keywords targeted (the posting's own wording):** Python · Django · Django REST Framework ·
  **RESTful APIs** · SQL · PostgreSQL · JavaScript · HTML5 · CSS3 · AJAX · AWS · **CI/CD pipelines**
  · Redis.
- **jQuery/AJAX handled honestly:** the frontend skills row names JavaScript ES6, HTML5, CSS3, AJAX
  and the jQuery-era libraries he has actually used (AOS, Isotope, GLightbox, Swiper), then the
  modern React/Next.js work. No claim of jQuery framework depth.
- **Deliberately omitted:** **Memcached** — never used, and Redis is not passed off as it. Also cut:
  electronics/IoT/Li-Fi, C#/Java, and any years-of-experience figure.
- **Knockouts:** 5+ years asked against ~2 years professional — the CV argues scope and trajectory,
  never duration. On-site Dhaka is lateral to his current Mohakhali commute, with no remote upside.
- **Weak spots:** Memcached. Ask whether the jQuery/AJAX frontend is legacy maintenance — if it is,
  the day-to-day would be a step back from the Next.js 16 work, and that matters more than the salary
  band. This is the best stack fit of the tier-3 set; rank it above Codixel if both call.

## Status timeline
- 2026-08-03 — Found
- 2026-08-04 — Draft (CV built and rendered; not yet submitted)
- 2026-08-04 — **Archived, not applied.** BDJobs listing checked directly: the application deadline
  has expired. Folder moved `Findings/` → `Archived/`. **Do not surface this posting again.**
