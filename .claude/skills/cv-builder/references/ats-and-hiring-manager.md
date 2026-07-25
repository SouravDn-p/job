# How CVs Actually Get Read — ATS and Hiring Managers

Research compiled **25 July 2026**. This is the evidence base behind `SKILL.md`.
Read this when you need the *why* behind a rule, or when a decision isn't covered
by the procedure.

Sources are listed at the bottom. Where the evidence is weak or contested, it says so.

---

## The three gates

A CV is not read once. It passes three gates, in order, and each one wants
something different. Optimising for one at the expense of another is the most
common way a CV fails.

| Gate | Who/what | Time spent | What it wants | Failure mode |
|---|---|---|---|---|
| **1. Parser** | ATS extracts text → database fields | milliseconds | Machine-readable structure | Data lands in the wrong field, or vanishes |
| **2. Ranking / recruiter skim** | Keyword search, AI match score, human 7-second scan | ~7.4 seconds | Obvious, literal relevance in the top third | Ranked below the batch the recruiter has time for |
| **3. Hiring manager read** | The person who owns the role | 30 seconds → 2–4 minutes | Evidence of impact, scope, trajectory | Reads as a task list; nothing to evaluate |

Gate 1 is a formatting problem. Gate 2 is a vocabulary problem. Gate 3 is a
**content** problem — and it's the one that actually gets an interview. Most CV
advice online is 90% gate 1, which is why so many "ATS-optimised" CVs get
parsed perfectly and then rejected by a human.

---

## Gate 1 — The parser

### What ATS actually does (and what it doesn't)

**It does not auto-reject you for formatting.** This is the single most
over-stated claim in CV advice. In a 2025 survey of 25 working recruiters,
**23 of 25 (92%) said their ATS does not automatically reject resumes** for
content or formatting. The 2 that used content-based auto-rejection applied it
to match thresholds or required-skill counts, not layout. **No recruiter in the
study reported an ATS rejecting a CV for fonts, layout, or formatting errors.**

The famous "**75% of resumes are auto-rejected by ATS**" figure is **not real**.
It traces to a 2012 marketing claim by a small resume company that shut down the
following year, with no published methodology. Do not repeat it, and do not let
it drive design decisions.

**What ATS does do:**

1. **Parse** — extract name, contact, employers, titles, dates, education,
   skills into structured fields.
2. **Knockout-question filtering** — **100% of surveyed recruiters** use yes/no
   eligibility gates (work authorisation, location, certifications, degree).
   These *do* auto-reject, and they are answered in the application form, not
   the CV. Answer them carefully; they are the only real automatic rejection.
3. **Rank** — keyword search and, increasingly, AI match scoring, to decide
   review order. **99.7% of recruiters use keyword filters inside the ATS** to
   sort and prioritise. This is why keywords matter — not rejection, *ranking*.

**The real enemy is volume, not the algorithm.** Recruiters in the study
described 400–500 applications for one data-analyst role in a week, and 2,000
for a software engineering role. One said that once they find strong candidates
in the first batch, *"we'll probably start interviewing before we even look at
the rest."* **52% said applying early materially improves your chances**,
because review happens in order received. Applications per job rose **111%
between 2022 and 2025** (115 → 244 on average).

> **Implication:** a perfectly-optimised CV submitted on day 9 loses to a good
> one submitted on day 1. When handing over a CV, say so.

### Parsing rules that are worth following

These are cheap to obey and occasionally save you, so obey them — but hold them
as hygiene, not as the point of the exercise.

**Layout**
- **Single column.** Multi-column is the one layout choice with real evidence
  against it: Workday's parser in particular struggles with columns and
  embedded tables. Two-column CVs risk interleaving text across columns.
- **No tables for layout.** Parsers skip or scramble table content.
- **No text boxes** — content inside is commonly skipped entirely.
- **Nothing in headers/footers.** Many parsers ignore that region. Never put
  contact details there.
- **No text baked into images**, no logos, no skill-rating bars, no icons
  carrying meaning. If a graphic conveys information, that information is lost.
- **Contact details as plain text at the top of page 1**, pipe- or
  bullet-separated.

**Type**
- Standard fonts: Arial, Calibri, Helvetica, Georgia, Garamond, Times New Roman,
  Verdana. Body **10–12pt**, name **14–16pt**, section headings **11–13pt**.
- Bullets: `•` or `-` only. Not stars, arrows, checkmarks, or emoji.

**Section headings — use the boring names.** Parsers match on literal strings:
  - `Professional Summary` / `Summary` / `Profile`
  - `Work Experience` / `Professional Experience` / `Employment History`
  - `Skills` / `Technical Skills`
  - `Projects` / `Selected Projects`
  - `Education`
  - `Certifications`

  Never `My Journey`, `What I Bring`, `Toolbox`, or similar.

**Dates — this one genuinely breaks parsers.** Use **`Mon YYYY – Mon YYYY`**
(e.g. `Aug 2025 – Present`). Evidence indicates `Jan 2023 – Mar 2025` parses
cleanly across the major systems while `January 2023 to March 2025` often fails
to extract. Avoid numeric (`08/2025`), apostrophes (`Aug '25`), seasons, and
quarters. Use an en-dash or hyphen as the separator, never the word "to".

**File**
- Text-based PDF or DOCX. Both parse reliably in Workday, Greenhouse and Lever.
- **Test:** open the PDF and try to select the text. If you can't highlight and
  copy it, no parser can read it. A CV exported as an image is invisible.
- **Filename:** `Firstname_Lastname_Role.pdf`. Never `cv_final_v3.pdf`.

**Parser strictness, roughly ranked** (Workday/Greenhouse/Lever/Ashby/iCIMS
cover ~78% of the market):
- **Workday** — strictest. Struggles with columns and tables; wants tight date
  formatting. Design for Workday and you're safe everywhere.
- **Greenhouse** — moderate. Handles single-column with sub-bullets fine.
- **Lever** — most forgiving; tolerates some tables.

### What changed by 2026: LLM screening

Screening has shifted from literal token matching to **semantic matching**. The
CV and the job description are embedded into the same vector space and compared
for closeness, so a CV saying "statistical modelling with Python" now aligns
with a JD asking for "machine learning with scikit-learn". An LLM may read the
parsed text, write a short fit summary, and hand the recruiter a score with a
rationale. **87% of organisations now use AI somewhere in hiring.**

Recruiter-facing scores are visible in the product: **Oracle** rates 0–5 at
submission, **Workday** grades A–D, **Greenhouse** ranks by criteria match
without auto-rejecting. A low rank can mean no human ever opens the file, even
though nothing "rejected" you.

But recruiters don't trust the scores much: **44%** of systems surface a match
score, **36%** manually verify it before acting, and only **8%** use it as a
hard filter. One recruiter: *"The fit score… we're not really trusting it. It's
hit and miss."*

**Two consequences for how we write:**

1. **Exact-string paranoia matters less than it did.** Semantic matching means
   "RESTful services" will usually match "REST APIs". Mirroring the JD's literal
   vocabulary is still the right default — it costs nothing, it survives the
   older keyword-search path that 99.7% of recruiters still use, and it reads as
   deliberate to a human — but do not mangle a sentence to force a literal
   string in.
2. **Context beats density.** An LLM reading for fit rewards a keyword sitting
   inside a real accomplishment ("built Celery task queues handling X") over the
   same keyword in a comma-list. Skills sections still matter for search; the
   *evidence* has to live in the bullets.

### Things that backfire — do not do these

- **Hidden keywords in white text or 1pt font.** Recruiters do find them: paste
  a CV into a notes field or an ATS text preview and the hidden block appears in
  plain black. The reaction is described as a fast, emotional "no", and it can
  follow you across companies in a recruiter's network. Some platforms flag text
  whose colour matches the background automatically.
- **Prompt-injection text aimed at LLM screeners.** Same category, worse.
- **Keyword stuffing.** **76% of recruiters** value *natural* keyword usage;
  stuffing reads as copying to both the AI and the human. Rule of thumb: any
  given keyword **2–3 times maximum**, in different sections, each time inside a
  genuine readable sentence.
- **Mass-applying with an untailored CV.** One recruiter called it evidence of
  *"lack of attention to detail"* and a rejection trigger. Another noted
  recognising identical ChatGPT formatting patterns across submissions — *"give
  it that human eye."*

---

## Gate 2 — The 7-second skim

Ladders' eye-tracking study (30 professional recruiters, 10 weeks, tracked
gaze on hundreds of CVs) found an average initial screen of **7.4 seconds**, up
from 6 seconds in 2012.

**They read in an F-pattern:** thorough scan of the **top third of page 1**,
then a fast skim down the **left edge**, glancing right only occasionally.

What top-performing CVs had in common:
- Simple layout, clearly marked section headings, one clear font
- **Bold job titles** anchoring the left edge, each followed by bulleted
  accomplishments
- A **summary or overview at the top of page 1**

**Design consequences:**

1. **The top third of page 1 is the most valuable real estate on the document.**
   Name, target-role-aligned summary, and the top skills go there. If the
   recruiter has to reach page 2 to learn you're a backend engineer, the CV has
   failed.
2. **Front-load every bullet.** The left edge gets read; the right does not.
   Put the outcome and the technology at the start of the line, qualifiers at
   the end. `Cut API p95 latency 40% by adding Redis caching…` beats
   `By adding Redis caching to the product endpoints, latency was cut by 40%`.
3. **Job titles must be scannable and bold.** Title, company, dates on one line,
   consistently placed.
4. **20% of recruiters flagged heavily-designed, graphic-laden CVs as harder to
   scan.** Visual flourish costs you at gate 2 even when it survives gate 1.
5. **92% emphasised clear skimmable structure; 72% preferred short bullets over
   paragraphs.** No paragraph blocks in the experience section.

---

## Gate 3 — The hiring manager

This is the gate that decides the interview, and it's where content quality
finally matters more than formatting.

Hiring managers typically decide within about **30 seconds** whether you're
worth a phone screen, then spend a few minutes confirming. Recruiters given
two-page CVs spent **over 4 minutes**; one-page CVs got **under 2.5 minutes**.

### The four things they're evaluating

**1. Relevance to *this* role.** The candidates who get callbacks are not the
ones with the most experience — they're the ones whose CV is the closest match
in vocabulary and demonstrated impact to the specific posting. Recent work
(last 1–3 years) weighs most, because the technology moves.

**2. Impact, not duties.** They need evidence of what *happened because you did
it*. Did response time drop, did coverage rise, did the service scale, did
delivery get faster? A bullet with no outcome gives them nothing to evaluate.

**3. Scope and trajectory.** Are you taking on bigger things over time — bug
fixes → features → owning a service → architecting → mentoring? Progression
matters and doesn't require a promotion to demonstrate. (A promotion is a strong
signal and should be stated explicitly when there is one.)

**4. Credibility.** They are actively sceptical of numbers that don't fit the
described scope. *"Reduced cloud costs by 60%"* reads as suspicious if the work
described was turning off unused instances. **A metric that outruns its scope
damages you more than no metric does** — it makes them distrust the whole
document, and it will be probed in the interview.

### Documented red flags

- Short stints and unexplained gaps (an employment-continuity filter of >6
  months is also one of the commonest ATS knockouts, per the HBS/Accenture study)
- **Jargon-rattling instead of describing the work** — hiring managers read this
  specifically as an attempt to satisfy a keyword filter
- Vague or disproportionate metrics
- Reverse-chronological violations — listing oldest first was explicitly
  criticised
- 7–8 page CVs — called an instant red flag

### The bullet formula

The most durable structure is Laszlo Bock's (ex-SVP People Ops, Google):

> **"Accomplished [X], as measured by [Y], by doing [Z]."**

- **X** — the outcome you created, not the task you were assigned
- **Y** — the number that proves it: %, time, volume, money, users, requests
- **Z** — the specific mechanism, technology, or decision that got you there

Z is where the JD's technology keywords belong — which is exactly what the LLM
screener at gate 2 rewards and what the hiring manager at gate 3 believes.

**52% of recruiters** specifically named achievements with measurable results as
what they value.

**When there is no honest number**, do not invent one. Substitute concrete
scope: what you built, what it handled, who used it, what it replaced, what it
integrated with. `Built the Stripe subscription flow covering three plan tiers
and webhook-driven state reconciliation` has no metric and is still evaluable.
This matters here — see the hard rule against invention in `CLAUDE.md`.

---

## Length

### What the evidence says

The old "one page, always" rule is not supported. ResumeGo (2018, 482
recruiters, hiring managers, HR professionals and C-suite executives, blind
hiring simulation) found recruiters were:

| Role level | Preference for two pages over one |
|---|---|
| Entry-level | **1.4×** |
| Mid-level | **2.6×** |
| Managerial | **2.9×** |

Two-page CVs scored **21% higher** on "summarises the candidate's work
experience and overall credentials", and got **4+ minutes** of attention versus
**under 2.5 minutes** for one-pagers.

Against that: **64% of the 25 surveyed recruiters preferred one to two pages
maximum**, and ATS does not penalise length either way.

### The rule to apply

**Content decides page count; page count never decides content.** Every line
must earn its place — but do not amputate genuinely strong material to hit an
arbitrary page target, and do not pad to fill one.

| Situation | Target |
|---|---|
| < 2 years, thin project inventory | 1 page |
| 1–5 years with substantial, JD-relevant material to show | **2 pages** — the default for this profile |
| 10+ years | 2 pages |
| Executive, academic CV, or federal/government application | 3+ pages, by convention |
| Any case | **Never 3 pages for a non-executive engineering role** |

**The fill test, applied to the rendered PDF, not to an estimate:**
- Every page before the last must be **≥ 90% full**.
- The last page must be **≥ 75% full**. A page 2 that is 40% full reads as
  padding and is worse than a tight single page — cut to one page.
- If it overflows, **cut copy before shrinking type**. 8.8pt is the floor.

**Regardless of length, the first third of page 1 has to work standalone.** The
7.4-second scan happens there. Page 2 is for the hiring manager at gate 3, never
for the recruiter at gate 2 — so nothing decision-critical goes on it.

---

## Quick reference — the rules that actually matter, ranked

1. Tailor to the specific posting. Untailored is the top rejection trigger.
2. Apply early. Volume beats optimisation.
3. Answer knockout questions correctly — the only true auto-reject.
4. Top third of page 1 carries the pitch.
5. Every bullet = outcome + number/scope + mechanism.
6. Mirror the JD's vocabulary naturally, 2–3 uses max per keyword.
7. Single column, standard headings, `Mon YYYY – Mon YYYY`, selectable-text PDF.
8. No metric that outruns its scope. Ever.
9. Nothing in headers/footers, no layout tables, no meaningful graphics.
10. Never hide text. Never stuff.

---

## Sources

Compiled 25 July 2026.

- [Does the ATS Reject Your Resume? 25 Recruiters Explain What Really Happens — Enhancv](https://enhancv.com/blog/does-ats-reject-resumes/) — the strongest primary source here; direct survey of working recruiters
- [Ladders eye-tracking study, 2018 update (7.4-second scan, F-pattern)](https://www.prnewswire.com/news-releases/ladders-updates-popular-recruiter-eye-tracking-study-with-new-key-insights-on-how-job-seekers-can-improve-their-resumes-300744217.html) · [HR Dive coverage](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/)
- [ResumeGo — Settling the Debate: One or Two Page Resumes](https://www.resumego.net/research/one-or-two-page-resumes/) · [CNBC coverage](https://www.cnbc.com/2018/12/19/resumego-hiring-managers-prefer-candidates-with-two-page-resumes.html)
- [Hidden Workers: Untapped Talent — Harvard Business School / Accenture (Fuller & Raman)](https://www.hbs.edu/managing-the-future-of-work/research/Pages/hidden-workers-untapped-talent.aspx) — 8,000+ workers, 2,250+ executives; 88% of employers admit qualified candidates are screened out by rigid filters; ~27M affected in the US
- [How AI Resume Screening Works in 2026 — Jobscan](https://www.jobscan.co/blog/blog-ai-resume-screening/) — semantic matching, vendor scoring behaviour, 111% application-volume rise
- [Are You Guilty of Resume Keyword Stuffing? — Jobscan](https://www.jobscan.co/blog/resume-keyword-stuffing/)
- [The "75% auto-rejected" myth, traced to its source — Uncharted Career](https://unchartedcareer.com/blog/the-75-of-resumes-are-auto-rejected-myth-traced-to-its-source)
- [How Workday, Greenhouse & Taleo Read Your Resume (2026)](https://www.shashiworks.com/ats-workday-greenhouse-taleo.html) · [ATS-Friendly Resume Formatting: Complete Parsing Rules for 2026](https://cv4me.pro/blog/ats-friendly-resume-formatting-2026) — parser-specific formatting; SEO-commercial sources, treat the specifics as plausible convention rather than measured fact
- [Red Flags in Technical Resumes — Exodata](https://exodata.io/red-flags-in-technical-resumes-what-hiring-managers-miss/) · [Software Engineer Resume — Austen McDonald / System Design newsletter](https://newsletter.systemdesign.one/p/software-engineer-resume) — engineering hiring-manager perspective
- [XYZ formula — Laszlo Bock / Google](https://resume.io/blog/xyz-resume-format)

**Reliability note.** The recruiter survey, the eye-tracking study, the ResumeGo
simulation and the HBS report are real studies with stated methodology. The
parser-specific formatting claims (which ATS mangles which layout, exact date
strings) come mostly from CV-tool vendors with an incentive to sound
authoritative and no published testing. They're followed here because the cost
of compliance is near zero, not because they're proven.
