# Plan — onsite MCQ exam · one day, about 12 hours

**This plan prepares you for the onsite MCQ test only.** The interview rounds that follow have their
own folders — [`../hr-interview/`](../hr-interview/) and
[`../technical-interview/`](../technical-interview/) — already written and waiting. Ignore them today.

> **Honest warning.** One day is not enough to cover everything this paper spans. Nine subjects
> properly learned is a two-week job. This is a **triage plan**, ordered by how likely each topic is
> to appear multiplied by how fast you can bank it. What is traded away is listed at the bottom.
>
> The good news: an ex-WellDev interviewer said publicly that most of their questions are *easy* and
> any fresh graduate should have a basic idea. **It is a breadth test, not a depth test** — and
> breadth is exactly what one focused day can buy.

---

## The 60-second version

**11 sessions.** Morning is data structures and algorithms — the biggest slice of the paper. Midday
is SQL, databases and OOP, where you are already strong and can move fast. Afternoon is networking,
REST and JavaScript, which holds your one real gap. Evening is aptitude, a **timed mock**, then
repair of whatever the mock exposes. Stop by 21:00 and sleep.

Two things do all the work: [`preparation.md`](preparation.md) to learn from, and the
[`question-bank/`](question-bank/) to practise on — **126 questions** across
[`set-01.md`](question-bank/set-01.md) (78, the core sweep) and
[`set-02.md`](question-bank/set-02.md) (48, filling the weak spots: JavaScript, subnetting,
reasoning, sorting traces, operating systems, joins).

**You will not finish all 126, and you are not meant to.** Each session lists its questions in
priority order — do set 01 first, then set 02 if the session has time left. The two exceptions are
**session 8 (JavaScript)** and **session 9 (reasoning)**, where set 02 *is* the point.

## How each session works

**50 minutes on, 10 off.** Same four steps every time:

| Step | Min | What you do |
|---|---|---|
| **Listen** | 10 | Play the block's script from [`listen/`](listen/). Do nothing else while it plays. |
| **Learn** | 15 | Read the listed sections of [`preparation.md`](preparation.md). They are short on purpose. |
| **Do** | 20 | Attempt the listed questions with the answers collapsed. Commit before you open one. |
| **Recall** | 5 | Close everything. Say the **Say this out loud** line from memory. Do not skip this. |

Clock times assume an **08:00 start** — shift them to whenever you actually begin.

---

## The schedule

### Block A — Data structures & algorithms · 3 sessions
🎧 [`listen/block-a-dsa.txt`](listen/block-a-dsa.txt)

| # | Time | Read | Questions |
|---|---|---|---|
| **1** | 08:00–08:50 | [1. Time complexity](preparation.md#1-reading-time-complexity-big-o) · [2. Sorting](preparation.md#2-sorting-algorithms) | `Q-DSA-002, 003, 008, 009, 010, 018` · **set 02:** `Q-DSA-023` – `026` (sorting traces) |
| **2** | 09:00–09:50 | [3. Arrays & linked lists](preparation.md#3-arrays-and-linked-lists) · [4. Stacks & queues](preparation.md#4-stacks-and-queues) | `Q-DSA-001, 004, 005, 016, 017, 020, 021, 022` |
| — | 09:50–10:10 | **Break. Stand up, leave the screen.** | |
| **3** | 10:10–11:00 | [5. Trees & BST](preparation.md#5-trees-and-binary-search-trees) · [6. Graphs](preparation.md#6-graphs-dfs-bfs-mst-and-greedy) · [7. Recursion](preparation.md#7-recursion) | `Q-DSA-006, 007, 011, 012, 013, 014, 015, 019` |

### Block B — Databases & objects · 3 sessions
🎧 [`listen/block-b-data-and-objects.txt`](listen/block-b-data-and-objects.txt)

| # | Time | Read | Questions |
|---|---|---|---|
| **4** | 11:10–12:00 | [8. SQL queries](preparation.md#8-sql--the-queries-they-actually-ask) | `Q-DB-001, 002, 003, 008, 011, 014` · **set 02:** `Q-DB-015` – `019` (joins) |
| — | 12:00–12:45 | **Lunch. Away from the desk.** | |
| **5** | 12:45–13:35 | [9. DBMS theory](preparation.md#9-dbms-theory--acid-normalisation-indexes-nosql) | `Q-DB-004, 005, 006, 007, 009, 010, 012, 013` |
| **6** | 13:45–14:35 | [10. OOP](preparation.md#10-object-oriented-programming) · [11. SWE principles](preparation.md#11-software-engineering-principles) | `Q-OOP-001` – `012` (all 12) · **set 02:** `Q-OS-001` – `004` (operating systems — no topic section, the answers teach it) |
| — | 14:35–14:55 | **Break.** | |

### Block C — Web, APIs and your one real gap · 2 sessions
🎧 [`listen/block-c-web-and-javascript.txt`](listen/block-c-web-and-javascript.txt)

| # | Time | Read | Questions |
|---|---|---|---|
| **7** | 14:55–15:45 | [12. Networking & HTTP](preparation.md#12-networking--http-status-codes-and-subnetting) · [13. REST APIs](preparation.md#13-rest-apis) | `Q-NET-001` – `012` (all 12) · **set 02:** `Q-NET-013` – `020` (subnetting drill — do these until the ladder is automatic) |
| **8** | 15:55–16:45 | ⚠️ [14. JavaScript](preparation.md#14-javascript-fundamentals--for-a-python-developer) — **your weakest area, and it leads their topic list.** Full 50 minutes. | `Q-JS-001` – `010`, then **set 02:** `Q-JS-011` – `025`. **25 questions — the largest single block of the day, deliberately.** |
| — | 16:45–17:15 | **Proper break. Eat. Do not study.** | |

### Block D — Reasoning, mock, repair · 3 sessions
🎧 [`listen/block-d-exam-craft.txt`](listen/block-d-exam-craft.txt) — play this one **before session 9**

| # | Time | What | Questions |
|---|---|---|---|
| **9** | 17:15–18:05 | [15. Analytical reasoning](preparation.md#15-analytical-and-mathematical-reasoning) — **with a timer, 90 s per question** | `Q-APT-001` – `008` · **set 02:** `Q-APT-009` – `020` (20 total) |
| **10** | 18:15–19:05 | **⏱ TIMED MOCK** — see below | 40 mixed, listed below |
| **11** | 19:15–20:05 | **Repair + speed round** — see below | driven by your mock results |
| — | 20:05–20:30 | Logistics checklist below. Bag packed, alarm set. | |
| — | **21:00** | **Stop. Sleep.** Nothing after this is worth the fatigue. | |

---

## ⏱ Session 10 — the timed mock

The most valuable hour of the day. It trains **pace**, and pace is what a hard auto-submit timer punishes.

**Setup:** 40 questions, 45 minutes — about 65 seconds each. No notes, no searching, phone in another room.

**Use these 40**, drawn from both sets and weighted the way the real paper reportedly is:

| Subject | Questions | Count |
|---|---|---|
| DSA | `Q-DSA-001, 002, 003, 004, 008, 011, 012, 016, 020, 023, 025` | 11 |
| Networking & REST | `Q-NET-002, 004, 007, 008, 013, 016, 018` | 7 |
| JavaScript | `Q-JS-001, 004, 011, 012, 013, 019, 025` | 7 |
| DBMS & SQL | `Q-DB-001, 003, 005, 009, 016, 018` | 6 |
| OOP | `Q-OOP-002, 003, 005, 012` | 4 |
| Analytical | `Q-APT-002, 004, 013, 016` | 4 |
| OS | `Q-OS-002` | 1 |

**The rule that matters:** unresolved at **90 seconds → guess, mark it, move on.** One stubborn
question eating five minutes costs four easy ones. That is how people fail a broad MCQ while knowing
the material.

Score it. Log it in the progress table below, **and note which subject your wrong answers cluster in.**

## Session 11 — repair + speed round

Not new material. Three parts:

1. **Repair · 25 min.** Re-read the `preparation.md` section for whichever subject your errors clustered in. Redo those questions.
2. **The four memorise-tables · 15 min.** Read each aloud, cover it, recite it:
   - The Big-O ladder — [section 1](preparation.md#1-reading-time-complexity-big-o)
   - Status-code families, and 401 vs 403 — [section 12](preparation.md#12-networking--http-status-codes-and-subnetting)
   - The subnet ladder: /24→254, /25→126, /26→62, /27→30, /28→14, /30→2 — [section 12](preparation.md#12-networking--http-status-codes-and-subnetting)
   - Sorting complexities and which are stable — [section 2](preparation.md#2-sorting-algorithms)
3. **Speed round · 10 min.** 20 questions in 10 minutes, answers covered — half your normal time. You are training recall speed, not accuracy. Reuse questions you already got right.

---

## If you fall behind

You will. Sacrifice in this order:

1. **[11. SWE principles](preparation.md#11-software-engineering-principles)** — you do this professionally. Skim the tables only.
2. **[13. REST APIs](preparation.md#13-rest-apis)** — home ground. Read the verb table, skip the rest.
3. **Session 9** — cut to 25 minutes, but never to zero; the timing discipline *is* the lesson.
4. **The speed round** in session 11.

**Never cut:** the JavaScript session, the timed mock, or the repair block. JavaScript is your gap,
the mock is your pacing, and the repair block is the only part of the day that reacts to evidence.

## What is deliberately not covered

- **Operating systems** — "kernel" appears in the reported list. Cut; too little return for one day.
- **Deep dynamic programming** beyond memoised Fibonacci. Cut.
- **Their stack** (Ruby on Rails, ColdFusion, .NET). Cut — you won't be tested on a language nobody asked you to know.
- **Subnetting beyond the formula and the ladder.** If subnetting is heavy on the paper you will lose marks there. Accepted trade.
- **System design.** Not in the MCQ.

---

## Logistics — tonight, not tomorrow

**⚠️ The JD says the test is ONSITE.** That is a change from the remote, screen-shared Quilgo format
candidates described in 2024. Plan to travel.

- [ ] **Re-read the invitation email** — date, time, address, floor, what to bring. The JD's tentative date was **31 July 2026**; if the email says otherwise, **the email wins.**
- [ ] **Open the recruitment-process PDF** linked in the JD — [Google Drive](https://drive.google.com/file/d/1NHE5wISWjLuy84Pqe9si97GeCXAjBedV/view?usp=sharing). It needs a login so I could not read it; it may state the duration and round count.
- [ ] **Route and travel time** to the WellDev Dhaka office, plus 45 minutes of margin for traffic.
- [ ] **Photo ID**, two pens, a printed CV copy.
- [ ] **Ask if you can:** how long, how many questions, **is there negative marking?** That last one decides whether you guess.
- [ ] **Confirm your CGPA** against the IUBAT transcript — recorded as 3.59, an older source says 3.42, and it is unverified. Fresher pipelines check transcripts.
- [ ] **Alarm set. Clothes out. Bag packed.**

## 30 minutes before

**No new material.** Nothing learned in the last half hour survives the stress.

1. Read the Big-O table and the status-code table. Two minutes each — highest density recall on the page.
2. Recite the subnet ladder once.
3. Repeat the pacing rule: **90 seconds, then guess and move on.**
4. Breathe. Their own ex-interviewer said the questions are mostly easy. This is a test of composure across nine subjects, and that is exactly what today built.

---

## Progress

Fill in the last three columns as you go.

| # | Session | Done? | Confidence 1-5 | Revisit? |
|---|---|---|---|---|
| 1 | Complexity + sorting | | | |
| 2 | Arrays, linked lists, stacks, queues | | | |
| 3 | Trees, graphs, recursion | | | |
| 4 | SQL queries | | | |
| 5 | DBMS theory | | | |
| 6 | OOP + SWE principles | | | |
| 7 | Networking + REST | | | |
| 8 | ⚠️ JavaScript | | | |
| 9 | Analytical reasoning (timed) | | | |
| 10 | **Timed mock** — score: ___ / 40 · weakest subject: ________ | | | |
| 11 | Repair + speed round | | | |
