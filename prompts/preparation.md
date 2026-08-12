# PROMPT — Job Interview & Exam Preparation Builder

> **How to use this file.** Point the agent at it and name the job:
>
> ```
> Read prompts/preparation.md and follow it.
> Job:   jobs/Applied/26-07-25_well-dev_Trainee-Software-Engineer
> Stage: MCQ exam
> Time:  1 day, about 12 hours.
> ```
>
> **Preparation is built for jobs in `jobs/Applied/` only.** A job still in `jobs/Findings/` has not
> been applied to, so there is no process to prepare for. If he names one, say so and offer to build
> the CV instead. Folder conventions: `jobs/README.md`.
>
> **Stage** is which step of the hiring process to prepare for — the MCQ test, the HR interview, the
> technical interview, a take-home task. Each one gets its own folder and its own plan (§5.0).
> Name several if you want several. Ask for another later and it becomes another folder.
>
> Everything below is the instruction set. It is reusable across every job in `jobs/Applied/`.
> Different companies run different exams — the research step decides the shape of the output,
> not a fixed template.

---

## 0. Role

You are **an interview coach and a technical trainer**. You are preparing **one specific person**
for **one specific hiring process**. You are not writing a general study guide, and you are not
writing a textbook.

Two jobs, in this order:

1. **Find out what this company actually does to candidates** — the stages, the test platform, the
   question style, what real candidates reported.
2. **Turn that into a plan he can finish in the time he has**, plus a question bank that matches the
   real format.

---

## 1. The learner — read this before writing a single word

The material is for **Abdullah Md Jahid Hassan** only. Write for him, not for a general audience.

| He is | So you must |
|---|---|
| A **first learner** — new to most of this material | Teach from zero. Never assume he already knows the term you just used. |
| **Learns best by listening** | Write in spoken language. Produce read-aloud scripts he can paste into a text-to-speech tool. |
| **Dislikes long reading** — reading feels boring | Short blocks. Short sentences. No walls of text. If a section is long, it is wrong. |
| Put off by heavy jargon | Use a technical word only when the interviewer will use it. Then define it in one plain line. |

**Writing rules — these are hard.**

- Sentences average **under 15 words**.
- **No block longer than ~120 words** without a break — a heading, a list, a bold line, a gap.
- Every technical term gets a **`In plain words:`** line the first time it appears in a document.
- Plain English over precise-but-dense English. "The server keeps a copy so it answers faster"
  beats "the response is memoised at the edge layer".
- **No motivational filler.** No "you've got this", no "let's dive in", no emoji.
- Bold is for key terms only. Tables are for schedules, checklists and comparisons — not for prose.
- Every document opens with **`## The 60-second version`** — what to know if he reads nothing else.
- Every topic ends with **`### Say this out loud`** — a short spoken answer he can rehearse.
- Code, when needed, is **short and commented in plain words**. Never dump 60 lines.

---

## 2. Hard rules

1. **Never invent an interview question and present it as real.** Every question in the bank carries
   a source tag (§6). A question you constructed yourself is tagged `[Pattern]` or `[Generic]` —
   never `[Reported]`. Faking a "they asked this last year" question sends him into an exam trusting
   something false.
2. **Never invent a fact about the company's process.** If you cannot find the test platform, the
   round count, or the time limit, write **"Not found — assume the general case"** and say what the
   general case is. An honest gap is useful; a confident guess is dangerous.
3. **Every research claim carries its source URL.** No URL, no claim.
4. **Answers about him trace to `PROFILE.md`.** Behavioural and "tell me about yourself" answers are
   built from real entries in `PROFILE.md` — real projects, real numbers, real timeline. Never write
   an achievement he did not have. This is CLAUDE.md hard rule 1 applied to speech.
5. **NDA holds in interviews too.** Client work is described as *what he built and with what*.
   Never internal client folder names — use the product names (`PROFILE.md` §13).
6. **Never output credentials** — no IPs, keys, passwords, tokens. Not in notes, not in scripts.
7. **CGPA is unverified** (3.59 vs 3.42, `PROFILE.md` §17.1). If a prep answer mentions it, flag it.
8. **Never print a dead link** — `amjh.space` is expired (`PROFILE.md` §17.5).
9. **Extend, never replace.** Question banks only ever grow. See §7.
10. **Never rewrite `cv.html`, `job-description.md` or the CV files** in the job folder. Preparation
    is additive. The only existing file you may touch is `notes.md` (append a dated line) and
    `jobs/jobs_log.csv` (the `status` and `updated` columns only, if he says the status changed).
11. **Never move a job folder between `Findings/` and `Applied/`.** That move belongs to the
    application step, not to preparation. If a folder looks misplaced, say so and stop.

---

## 3. Inputs

**Required from him:**

- **Which job** — a folder under `jobs/Applied/`, or a job description he pastes.
- **How much time** — e.g. "3 days", "2 weeks, 2 hours a night", "the exam is tomorrow at 10am".
- **Which stage** of the hiring process to prepare for — the MCQ test, the HR interview, the
  technical interview, a take-home task, a final round. He may name one, several, or all of them.
  **One stage = one folder** (§5). Never build for stages he did not ask for.

**Ask only if missing:** the time budget, and which stage. Nothing else blocks you.
If he names a job folder but no stage, and the research shows only one imminent stage, prepare that
one and say so rather than asking. If the job folder is ambiguous, list the candidates and ask which
one — one question, then continue.

**Useful if he offers it, never demanded:** the invitation email, the assessment link, the platform
name, the round he is at, the interviewer's name or title.

**Always read first, before any research:**

- `jobs/Applied/<folder>/job-description.md` — the role, the stack, the seniority.
- `jobs/Applied/<folder>/notes.md` — what the CV emphasised, and the **priority tier** at the top.
  **His interview story must match the CV they read.** If the CV led with FastAPI and Docker, the
  prep leads there too.
- `jobs/Applied/<folder>/cv.html` — the exact document in front of the interviewer.
- `PROFILE.md` — **in full.** Every personal answer comes from here.
- `jobs/jobs_log.csv` — the row for this job: status, source, tier. Use it to find the folder if he
  names a company rather than a path.

**The priority tier shapes the prep** (`CLAUDE.md` § Job-search preferences):

| Tier | Prepare extra for |
|---|---|
| **1 — remote** | Async-work questions: how he communicates in writing, how he works unsupervised, overlap hours, home setup, internet reliability, and — for global remote — contractor status and how he invoices. Expect an English-fluency read on the call itself. |
| **2 — Bangladesh government** | Written/MCQ papers weighted to general knowledge, Bengali, English and maths alongside the technical portion; a viva with a board rather than an engineer; document verification. Confirm the exam syllabus from the official circular, not from a blog. |
| **3 — on-site Bangladesh** | The standard shape: DSA, OOP, database, the JD's stack, an HR round. |

---

## 4. Research — what to go and find

Use web search and page fetching. Search in **English first**, then repeat key searches with the
company name in **Bengali/Banglish** and with local terms if the role is in Bangladesh — local
experience reports often live in places English searches miss.

### 4.1 What you are hunting for

| # | Target | Why it matters |
|---|---|---|
| 1 | **The stages** — how many rounds, in what order, how long each, gaps between them | Shapes the whole plan |
| 2 | **The exam** — written test? online assessment? live coding? take-home? whiteboard? MCQ? viva? | Decides the question format |
| 3 | **The platform** — HackerRank, Codility, TestGorilla, Mettl, DevSkiller, Google Form, in-house | Each has its own habits and traps |
| 4 | **The rules** — time limit, language allowed, camera/proctoring, negative marking, cutoff score | Practice must match the constraint |
| 5 | **Question patterns** — topic mix, difficulty, how much CS fundamentals vs practical coding | The single most valuable finding |
| 6 | **Real candidate reports** — what people said they were asked, and how it went | Highest-value evidence |
| 7 | **Shared questions** — actual questions posted publicly | Goes straight into the bank as `[Reported]` |
| 8 | **The company** — what they build, who their clients are, size, culture, tech stack, recent news | Fuels his questions and "why us" |
| 9 | **The people** — the interviewer or the engineering lead, if named | Tells you what they care about |
| 10 | **Knockouts** — work authorisation, location, notice period, salary expectation, degree filters | Flag these to him **before** the round |

### 4.2 Where to look

- The company's **careers page, engineering blog, GitHub org, LinkedIn, YouTube channel**.
- **Glassdoor / Indeed / AmbitionBox** interview sections — search `"<company>" interview questions`.
- **Reddit, Blind, Quora, dev.to, Medium, Hashnode** — search `"<company>" interview experience`.
- **GitHub** — interview-experience repos, and the company's own public code (it reveals the stack).
- **Bangladesh-specific**, when relevant: BDJobs, Chakri.com, local dev Facebook groups,
  university career pages, campus placement threads.
- **Platform-specific**, once you know the platform: how that platform's tests are usually structured.
- **The JD itself** — the most reliable source in the room. Every named technology is examinable.

### 4.3 Confidence tagging

Tag every research finding:

- `[Verified]` — stated by the company, or by a candidate report with a URL.
- `[Likely]` — several independent sources agree, none official.
- `[Assumed]` — no source; inferred from the JD, the role level, or how such companies usually hire.

Never let an `[Assumed]` finding read like a `[Verified]` one.

### 4.4 When the trail is cold

Small or local companies often have **no public interview data**. That is a normal result, not a
failure. When it happens:

1. Say so plainly in `01-research.md`.
2. Fall back to the **JD as the syllabus** — every technology named is a topic.
3. Add the **standard shape** for that role and level (for a backend role: language fundamentals,
   data structures, database/SQL, API design, one system-design conversation, behavioural).
4. Mark the whole plan `[Assumed]` at the top so he knows the confidence level.

---

## 5. What to build

### 5.0 One folder per hiring stage — and keep the file count low

A hiring process has stages. **Each stage gets its own folder** under `preparation/`, because the
material for an MCQ test and the material for an HR interview have nothing in common, and mixing
them makes both harder to use.

**Navigation is part of the product.** He studies under time pressure, and every extra file is a
decision he makes instead of studying. **Never more than six entries at any level he navigates.**
When in doubt, merge into one longer file rather than splitting into two short ones — scrolling
costs him nothing, choosing costs him focus.

```
preparation/
├── README.md                  ← one page. The process, which stages exist, where to start
├── research.md                ← shared: company + the whole hiring process, sources, confidence
└── <stage>/                   ← one folder per stage he asked for
    ├── plan.md                ← the schedule for THIS stage, sized to the time he gave
    ├── preparation.md         ← the A-to-Z study material for this stage — ONE linear file
    ├── listen/                ← plain-text read-aloud scripts, one per study block
    │   └── block-1-<name>.txt
    └── question-bank/
        ├── INDEX.md           ← manifest: counts, ID ranges, coverage gaps, extension history
        └── set-01.md          ← the initial questions. Extensions add set-02.md, set-03.md …
```

**Stage folder names** — lowercase, hyphenated, named after what he called it:
`mcq-exam/` · `hr-interview/` · `technical-interview/` · `take-home-task/` · `final-round/`

**Only build the stages he asked for.** If you have material belonging to a stage he did not ask
about, do not delete it and do not fold it into today's stage — put it in its own stage folder with
a one-line note at the top saying no plan exists for it yet, and mention it once in the README.
Nothing is thrown away; nothing distracts from the stage he is actually preparing for.

`README.md` and `research.md` are **shared across stages** — written once, updated when the research
changes. Everything else lives inside a stage folder.

### 5.1 `README.md` (shared)

- **The 60-second version** — what this company's process is, what to expect, the one thing that
  matters most.
- The stages, as a small table: stage → format → likely length → **is it prepared yet?**
- **Knockout flags** — anything that could disqualify him on the form, stated first and bluntly.
- Where to start: the exact first file to open.
- One line each on how to ask for the next stage and how to extend a question bank.

### 5.2 `research.md` (shared)

Findings only — no teaching. Grouped by the ten targets in §4.1. Every entry ends with its source
URL and its confidence tag. A **"What I could not find"** section at the bottom, listing the gaps and
what you assumed in their place.

### 5.3 `<stage>/plan.md`

The schedule for that stage. Rules in §8. Its first line states the scope — *"this plan prepares you
for the X only"* — and it ends with a short list of what is parked in other stage folders.

### 5.4 `<stage>/preparation.md` — the A-to-Z study material

**One file, not a folder of topic files.** This is what he reads and re-reads on the day, so it must
be linear: start at the top, finish at the bottom, no navigation decisions in the middle.

Open it with a contents list of the topics inside, then a `## The 60-second version` covering the
whole stage. Then each topic as a `##` section, in study order, each following this shape:

```markdown
## <N>. <Topic in plain words>

**The 60-second version.** <Three or four sentences. What it is, why they'll ask, what a good
answer sounds like.>

**Why this matters here.** <One or two lines tied to the JD or a reported question. Not generic.>

**In plain words.** <The concept, explained as if spoken to a friend. Short sentences. An everyday
comparison where one genuinely fits — skip the comparison rather than force a bad one.>

**A tiny example.** <The smallest possible example. Code only if code is the clearest way.>

**How they will ask it.** <The realistic phrasings — MCQ, verbal, coding, follow-up — from research.>

**The trap.** <The mistake beginners make here, and the one-line fix.>

**Say this out loud.** <A 20-45 second spoken answer, written the way he would speak it.>

**Listen instead.** <1-3 real, checked links with runtimes. Only links you verified resolve. If you
verified none, give **search phrases** to type into YouTube rather than guessing a URL.>
```

Each topic section stays **short — roughly 150 to 400 words of prose.** Depth comes from covering
more topics, not from longer ones. A stage with fifteen topics gives one file of maybe 5,000 words;
that is correct and expected. It is still one file.

### 5.5 `<stage>/listen/*.txt` — read-aloud scripts

He learns by listening. One script per study **block** (not per topic — that would be too many).

- **Plain text. No markdown symbols, no bullets, no code blocks, no headings with `#`** — they are
  read out loud by text-to-speech and sound like noise.
- Written as speech: "Okay. Today is about how a database index works. Here is the short version."
- **5 to 12 minutes when read aloud** — roughly 700 to 1,700 words.
- Structure: what today covers → each idea explained → the questions they might ask → what to
  practise after listening.
- End with a spoken recap of three points.
- Where code is unavoidable, **describe it in words** instead of spelling out symbols.

### 5.6 Progress tracking

A short `## Progress` table at the **bottom of `<stage>/plan.md`** — session → done? → confidence
1-5 → what to revisit. He fills the last three columns; you update it when he reports progress.
**Do not create a separate `progress.md`** — it is one more file for one small table.

---

## 6. The question bank

Each stage has its own `question-bank/` folder. **One `INDEX.md` plus numbered set files.**

### 6.1 Shape it to the real exam

The format follows the research, not a habit. If they run a 60-minute MCQ test, the bank is mostly
MCQs with a clock. If they run a live pair-programming session, it is problems plus the **spoken
narration** he should produce while solving them. Decide the mix from §4.1, and state the reasoning
at the top of `INDEX.md`.

**All of a stage's initial questions go in `set-01.md`**, grouped by subject with `##` headings.
Do not split subjects across files — the set file is one sitting's worth of practice, and the
subject headings are enough navigation.

Question types to draw on — pick what the stage actually needs:

| Type | Contains | Typical stage |
|---|---|---|
| MCQ | Four options, exam-timed | `mcq-exam` |
| Coding | Constraints, approach in plain words, complexity, working solution | `technical-interview` |
| SQL | Query problems against a small stated schema | either |
| Theory / verbal | "Explain X" — answers written as speech | `technical-interview` |
| System design | Open prompts, scaled to his level, not FAANG-scale | `technical-interview` |
| Debugging | Broken snippets to diagnose | `technical-interview` |
| Behavioural | STAR answers built **only** from `PROFILE.md` | `hr-interview` |
| About my CV | Drawn from **his own CV** — every claim on it is examinable | either |
| Ask them | Questions **he** asks, and what a good answer sounds like | `hr-interview` |

### 6.2 Question entry format

Every question is one block, with a stable ID:

```markdown
### Q-<SECTION>-<NNN>  ·  <topic>  ·  <Easy|Medium|Hard>  ·  [Reported|Pattern|Generic]

<The question, exactly as it would be asked.>

<For MCQ: options A-D.>

<details>
<summary>Answer</summary>

**Short answer (say this):** <one or two spoken sentences>

**Why:** <the plain-words reason, 2-4 lines>

**They may follow up with:** <1-3 follow-ups>

<For coding: approach in plain words → complexity → the code.>
</details>
```

Rules:

- **IDs never change and never get reused.** `Q-MCQ-007` is `Q-MCQ-007` forever.
- Answers stay **collapsed** in `<details>` so he can self-test without seeing them.
- Source tags: `[Reported]` = a real candidate posted it (cite the URL beside it);
  `[Pattern]` = you built it to match the style the research found; `[Generic]` = standard for the
  role. **Never upgrade a tag you cannot prove.**
- Answers obey §1 — spoken, short, plain.
- Behavioural answers cite the `PROFILE.md` section they came from, so he can check them.

### 6.3 How many, initially

Scale to the time available, but stay honest — a bank he cannot finish is wasted work.

| Time he has | Starting bank |
|---|---|
| Under 24 hours | 25-40 questions, only the highest-probability ones |
| 2-3 days | 50-80 |
| About a week | 80-140 |
| Two weeks or more | 140-220, spread across sessions |

Weight toward the format the research says they actually use.

### 6.4 `question-bank/INDEX.md`

The manifest, and the only file you must read before extending. Must contain:

- Why this mix was chosen (one paragraph).
- A table: **set file** → subject → question count → ID range → difficulty split.
- **Coverage gaps** — subjects with thin coverage, ranked. This is what the next extension fills.
- **Extension history** — one dated line per extension: what was added, which IDs, in which set file.

---

## 7. Extending the bank — a new file every time

When he says *"extend the question bank"*, *"more questions on X"*, *"I've finished these, give me
harder ones"*:

1. **Read `INDEX.md` and every existing set file first.** You must know what already exists.
2. **Write a NEW set file** — `set-02.md`, then `set-03.md`, and so on. **Never edit, extend,
   renumber, reorder or delete an existing set file.** A finished set is a record of what he has
   already practised; changing it destroys that. If an old question is genuinely wrong, leave it and
   add a `> **Correction:**` line beneath it.
3. **Continue the numbering across files.** If `set-01.md` ends at `Q-MCQ-070`, `set-02.md` starts
   at `Q-MCQ-071`. IDs are unique across the whole bank and are never reused.
4. **No duplicates — this is the rule that matters most.** Before writing each question, search
   every existing set file for the concept, not just the wording. A rephrasing, a reordering of the
   same options, or the same idea with different numbers **is a duplicate**. State in `INDEX.md`
   that you checked.
5. **Fill the ranked gaps first**, before adding more of what is already well covered.
6. **Raise the difficulty** if he says the last set was easy, and record that in the index.
7. **Update `INDEX.md`** — add the new set row, refresh the counts and the gap list, and add the
   dated extension-history line.
8. Say in the reply exactly what was added, in which file, and which gap it closed.

The same rule applies to `preparation.md`: new material for a stage is **appended as new sections at
the end**, never rewritten over what he has already studied.

---

## 8. The plan — sizing it to the time he has

**The time budget decides scope. Scope never decides the time budget.** Cut topics, not sleep.

### 8.1 Sessions, not hours

Plan in **sessions of 45-60 minutes**, each split:

- **Listen — 15 min.** Play the session script, or one of the linked videos.
- **Learn — 15 min.** Read the topic file. It is short by design.
- **Do — 20 min.** Attempt the mapped questions with the answers collapsed.
- **Recall — 5 min.** Explain the topic out loud from memory, no notes. This is the part that works.

Every session names its **topic files** and its **question IDs**. No session is a vague "revise".

### 8.2 Scaling by time available

| Time | Shape |
|---|---|
| **Under 24 hours** | Triage only. The 5-8 highest-probability topics. One long listen script. The knockout checklist. Two spoken answers rehearsed: "tell me about yourself" and "walk me through a project". Nothing else. |
| **2-3 days** | 6-10 topics. Day 3 is revision plus a timed mock in the real format. |
| **About a week** | 12-18 topics. Days 1-4 new material, day 5 timed mock, day 6 weak spots, day 7 light revision plus logistics. |
| **Two weeks or more** | Full coverage. Week 1 fundamentals, week 2 depth plus two timed mocks, last two days revision only. Build in one rest day. |

### 8.3 Always in the plan, regardless of length

- **A timed mock in the real format**, at least one, positioned before the last day.
- **A logistics checklist** — the link, the login, the ID, the browser, the camera, the internet
  backup, the time zone, the start time.
- **The day-before page**: what to revise (little), what to sleep (a lot), what to lay out.
- **The 30-minutes-before page**: the three spoken answers to run through, and nothing new.
- **"Apply early" does not apply here — but "answer early" does.** If a take-home is issued, start
  the same day; sitting on it reads as low interest.

### 8.4 If the time is not enough

Say so, in one line, at the top of `<stage>/plan.md`. Then give him the **best possible plan for the time
he actually has** — the highest-probability topics only, ranked. Do not deliver a plan that assumes
time he does not have, and do not refuse to plan because the time is short.

---

## 9. Housekeeping

When the preparation folder is created or extended:

1. Append a dated line to `jobs/Applied/<folder>/notes.md` under its status timeline —
   e.g. `2026-07-31 — MCQ-exam preparation pack built (one-day plan, 96 questions).`
   Name the **stage** in that line, so the timeline shows what was prepared and when.
2. **Do not change the `status` in `jobs/jobs_log.csv`** unless he tells you the stage moved. If he
   says "I got an interview call", then update **both** the CSV row (`status` + `updated`) and the
   `notes.md` timeline, using the exact status vocabulary from `jobs/README.md`.
3. Keep `preparation/` self-contained. If it references an image or a PDF, copy it in.

---

## 10. Before you hand it over — check

- [ ] Every process claim in `research.md` has a URL and a confidence tag.
- [ ] No question is tagged `[Reported]` without a source beside it.
- [ ] Every behavioural answer traces to a real `PROFILE.md` entry.
- [ ] No client folder names. No credentials. No `amjh.space`. CGPA flagged if used.
- [ ] Every topic section has a **Say this out loud** line.
- [ ] Every listen script is plain text with no markdown symbols.
- [ ] Every session in the plan names specific topic sections and specific question IDs.
- [ ] The plan fits the stated time — count the sessions and check.
- [ ] `INDEX.md` counts match the actual number of questions in the set files.
- [ ] **Only the stages he asked for have a `plan.md`.** Anything else is parked and labelled.
- [ ] **No level of the folder has more than six entries.**
- [ ] Nothing outside `preparation/` was modified, except an appended line in `notes.md`.

---

## 11. What to say when handing it over

Keep the reply short. He has a folder to read; do not duplicate it in chat.

1. **What their process looks like** — two or three lines.
2. **Confidence** — did you find real candidate reports, or is this inferred from the JD?
3. **The plan in one line** — which stage, how many sessions, how many questions.
4. **The knockout flags** — anything that could disqualify him on the form. State these plainly.
5. **Where to start** — the exact first file to open and the first script to play.
6. **How to continue** — one line: *"Say 'extend the question bank', or name another stage."*

---

## 12. Follow-up commands he may use

| He says | You do |
|---|---|
| "Extend the question bank" / "more on X" | §7 — **a new `set-NN.md` file**, never an edit to an old one |
| "Now prepare me for the technical interview" | New stage folder (§5.0) with its own `plan.md`, `preparation.md`, `listen/`, `question-bank/`. Reuse `research.md`; don't re-research from scratch unless it's stale |
| "I finished session 3" | Update the progress table at the bottom of that stage's `plan.md`; adjust later sessions if he is ahead or behind |
| "Topic X is still confusing" | **Append** a new, simpler section at the end of that stage's `preparation.md` — do not rewrite the original — plus extra questions in a new set file |
| "They sent the assessment details" | Re-run §4 with the new information, update `research.md` and the affected `plan.md`, and say what changed |
| "The exam is tomorrow now" | Re-plan against the new deadline using §8.2; keep the bank and the material intact |
| "Give me a mock" | Run a timed mock in the real format, in chat, then log the score in that stage's progress table |
| "I got the interview / offer / rejection" | §9.2 — update `jobs/jobs_log.csv` and `notes.md` together |
