# Application email — Flyte Solutions Ltd, Python Developer

Written 2026-08-13. Pairs with `cv.html` /
`Abdullah_Md_Jahid_Hassan_CV_Python_Developer.pdf`.
Every claim traces to `PROFILE.md` and appears on the CV. Kubernetes, RabbitMQ, Elasticsearch,
GraphQL and RAG are not claimed anywhere — same as on the CV.

**Send to:** career@flytesolutions.com
**Attach:** `Abdullah_Md_Jahid_Hassan_CV_Python_Developer.pdf`

> ⚠️ **Three values are left as `[ ]` placeholders — I will not invent them.** Fill in current
> salary, expected salary and notice period before sending. The posting asks for all three.

---

## MAIN VERSION — send this

**Subject:** Application – Python Developer

Dear Flyte Solutions Hiring Team,

I would like to apply for the Python Developer role at your Banani office. I am a backend developer
currently working as Senior Python Executive at Softvence Agency, and I build the kind of systems
your posting describes — REST APIs, containerised services, and backends that I take from schema
design all the way to production.

In eleven months at Softvence I have delivered eight production client backends: four on Django and
Django REST Framework, four on FastAPI. On each one I owned the full path — PostgreSQL or MySQL data
modelling, REST API design, Redis for caching and Celery brokering, background jobs with Celery and
Celery Beat, Docker and Docker Compose, GitHub Actions CI/CD, and deployment onto AWS EC2 and VPS
servers behind Nginx or Caddy. I was promoted from Junior Python Developer to Senior Python
Executive inside that period, and I also wrote the reusable Django REST foundation the company now
starts new projects from.

Two pieces of that work line up closely with the sectors you serve. For a multi-tenant SaaS product
I built the subscription and billing layer across two payment providers — Stripe and Tap Payments —
including plans, metered features, invoices, idempotent webhook handling and a retry and dunning
flow for failed cards. For an AI lead-generation platform I was the lead backend developer and built
the credit billing engine: an append-only transaction ledger with a running balance, credits
reserved when a job starts and settled when it finishes, automatic refunds, and per-request OpenAI
cost and token accounting so the business could see its real unit economics. That is my LLM
integration experience — production integration work with cost control, rather than model training.

On architecture, my Django services are built as domain-separated modular monoliths with a strict
models → selectors → services → serializers → views layering and no cross-domain foreign keys, so a
domain can be pulled out into its own service without a rewrite. I work on Linux servers daily, use
Git with branch and pull-request workflows, and cover my code with Django TestCase and pytest tests,
with migration-drift checks gating the CI pipeline.

The details you asked for:

- **Current salary:** [ ]
- **Expected salary:** [ ]
- **Notice period:** [ ]
- **GitHub:** https://github.com/abdullah-md-jahid-hassan
- **LinkedIn:** https://www.linkedin.com/in/abdullahmdjahidhassan/

I hold a B.Sc. in Computer Science & Engineering from IUBAT, I live in Uttara, Dhaka, and I am
available to work on-site in Banani. My CV is attached. I would be glad to talk about the backend
work your team has coming up.

Best regards,
**Abdullah Md Jahid Hassan**
+880 1756 254873 · abdullahmdjahidhassan@gmail.com
Uttara, Dhaka

---

## SHORTER VERSION — if you prefer a tighter email

**Subject:** Application – Python Developer

Dear Flyte Solutions Hiring Team,

I would like to apply for the Python Developer role at your Banani office. I am currently Senior
Python Executive at Softvence Agency, promoted from Junior Python Developer within eleven months.

In that time I have delivered eight production client backends — four on Django and Django REST
Framework, four on FastAPI — owning each from PostgreSQL or MySQL schema design through REST API
development, Redis caching, Celery background jobs, Docker, GitHub Actions CI/CD and deployment on
AWS EC2 and Linux VPS servers. Closest to your sectors: a two-provider subscription and billing
system on Stripe and Tap Payments with idempotent webhooks and card-retry handling, and a
credit-based AI platform where I built the transaction ledger and per-request OpenAI cost and token
accounting.

- **Current salary:** [ ]
- **Expected salary:** [ ]
- **Notice period:** [ ]
- **GitHub:** https://github.com/abdullah-md-jahid-hassan
- **LinkedIn:** https://www.linkedin.com/in/abdullahmdjahidhassan/

B.Sc. in Computer Science & Engineering from IUBAT, based in Uttara, Dhaka, available on-site in
Banani. CV attached.

Best regards,
**Abdullah Md Jahid Hassan**
+880 1756 254873 · abdullahmdjahidhassan@gmail.com

---

## Notes on what this email does and does not do

- **It does not mention years of experience.** The JD asks for 3–5 years and you have about one year
  professional (`notes.md`, Knockout #1). Your CV carries the dates openly, so nothing is hidden —
  but the email leads with delivery volume and the promotion instead of tenure, which is the
  strongest honest framing available. If they raise it on a call, the answer is eight production
  platforms in eleven months plus a year of self-directed Django work before joining.
- **No gaps are named.** Abdullah's decision, 2026-08-13. Kubernetes, RabbitMQ, Elasticsearch,
  GraphQL and RAG are simply not mentioned — the email talks only about what he has actually built.
  Nothing is claimed that isn't true, so this stays inside hard rule 1; it just doesn't volunteer
  what is missing.
- **Be ready for those two on a call.** Kubernetes appears twice in the JD (Required and Preferred)
  and RabbitMQ once in Required. If a screener asks, the honest answer is Docker and Docker Compose
  for containers, Redis-backed Celery for queues and background jobs.
- **Not claimed anywhere:** Kubernetes, RabbitMQ, Elasticsearch, GraphQL, RAG, SQL Server, Flask.
