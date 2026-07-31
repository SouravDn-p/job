# Question bank — MCQ exam · index

**126 questions across 2 set files.** Built 31 July 2026.

---

## Why this mix

The reported WellDev process puts a **multiple-choice test first**, and that test is the stage most
candidates fail. So every question here is exam-format: four options, one right answer, answerable
in about a minute. The six subjects below are the exact subjects named in the public candidate
reports, weighted by how much of the paper each reportedly occupies.

The bank is deliberately **wide and shallow, because the exam is.** Six subjects at MCQ depth beats
two subjects at interview depth.

Questions for the rounds *after* the MCQ live in the other stage folders —
[`../../technical-interview/question-bank/set-01.md`](../../technical-interview/question-bank/set-01.md) (18)
and [`../../hr-interview/question-bank/set-01.md`](../../hr-interview/question-bank/set-01.md) (24).

---

## Sets

| Set | Subject | Count | ID range | Difficulty E/M/H |
|---|---|---|---|---|
| [set-01.md](set-01.md) | Data structures & algorithms | 22 | `Q-DSA-001` – `022` | 10 / 12 / 0 |
| [set-01.md](set-01.md) | DBMS & SQL | 14 | `Q-DB-001` – `014` | 7 / 7 / 0 |
| [set-01.md](set-01.md) | OOP & software engineering | 12 | `Q-OOP-001` – `012` | 6 / 6 / 0 |
| [set-01.md](set-01.md) | Networking & REST | 12 | `Q-NET-001` – `012` | 5 / 7 / 0 |
| [set-01.md](set-01.md) | JavaScript | 10 | `Q-JS-001` – `010` | 4 / 5 / 1 |
| [set-01.md](set-01.md) | Analytical reasoning | 8 | `Q-APT-001` – `008` | 3 / 4 / 1 |
| | **set-01 total** | **78** | | **35 / 41 / 2** |
| [set-02.md](set-02.md) | JavaScript *(gap fill)* | 15 | `Q-JS-011` – `025` | 3 / 8 / 4 |
| [set-02.md](set-02.md) | Networking & subnetting *(gap fill)* | 8 | `Q-NET-013` – `020` | 3 / 3 / 2 |
| [set-02.md](set-02.md) | Analytical reasoning *(gap fill)* | 12 | `Q-APT-009` – `020` | 1 / 9 / 2 |
| [set-02.md](set-02.md) | Sorting **traces** *(new skill)* | 4 | `Q-DSA-023` – `026` | 0 / 3 / 1 |
| [set-02.md](set-02.md) | Operating systems *(new subject)* | 4 | `Q-OS-001` – `004` | 1 / 2 / 1 |
| [set-02.md](set-02.md) | SQL joins *(gap fill)* | 5 | `Q-DB-015` – `019` | 2 / 2 / 1 |
| | **set-02 total** | **48** | | **10 / 28 / 10** |
| | **BANK TOTAL** | **126** | | **45 / 69 / 12** |

---

## Source tags — read this before you trust a question

| Tag | Count | Meaning |
|---|---|---|
| `[Reported]` | **2** | A real candidate publicly reported this at WellDev. Sources in [`../../research.md`](../../research.md). |
| `[Pattern]` | **76** | **Written by me** to match the reported topics and style. The topic is real; the question and its four options are not from WellDev. |

**Only `Q-DSA-001` is a genuine reported *MCQ*** — its first line appears in a leaked WellDev paper,
though the full paper is paywalled, so even its four options are mine. `Q-APT-006` (two eggs, 100
floors) is reported, but as an *interview* question.

Most of the underlying **topics** are reported — SQL execution order, ACID, DELETE/TRUNCATE/DROP,
stack middle-deletion, the knight's shortest path, and more. But they were reported as interview
questions, and converting one into multiple-choice form makes the question mine. That is why the
`[Pattern]` count is so high.

**There is no leaked answer key here. Do not walk in expecting to recognise the paper.**

---

## Coverage gaps

**Set 02 closed the top six.** ✅ JavaScript 10 → **25** · subnetting 2 → **10** · analytical reasoning
8 → **20** · SQL joins 1 → **6** · sorting traces 0 → **4** · operating systems 0 → **4**.
Hard items 2 → **12**.

What remains, ranked, for any future extension:

1. **DBMS depth** — transactions and isolation levels have one question between them. Worth 6 more if the timeline extends.
2. **OOP code-reading** — one "spot the violation" snippet (`Q-OOP-002`). Snippet-reading is a distinct skill from definition-recall; worth 5 more.
3. **HTTP beyond status codes** — headers, cookies, CORS, HTTPS/TLS. Reported topics say "networking" broadly; only status codes and subnetting are drilled.
4. **Hashing and collision handling** — one question (`Q-DSA-019`). Reported topics don't name it, so this is low priority.
5. **Their actual stack** (Ruby on Rails, ColdFusion, .NET) — still zero, still deliberate. Only worth building if a later round signals a specific placement.

**The bank is now sized well past a single 12-hour day.** 126 questions at roughly a minute each is
over two hours of pure answering, before any review. Further extension is not the constraint —
time is.

---

## Extension history

| Date | Added | Set file | IDs | Duplicate check |
|---|---|---|---|---|
| 2026-07-31 | Initial build — 78 MCQs across 6 subjects | `set-01.md` | all | n/a — first set |
| 2026-07-31 | **+48 filling the six ranked gaps** — JavaScript ×15, subnetting/addressing ×8, analytical reasoning ×12, sorting traces ×4, operating systems ×4, SQL joins ×5. Difficulty deliberately raised: 10 Hard vs 2 in set 01. | `set-02.md` | `Q-JS-011`–`025` · `Q-NET-013`–`020` · `Q-APT-009`–`020` · `Q-DSA-023`–`026` · `Q-OS-001`–`004` · `Q-DB-015`–`019` | ✅ Every question checked against set-01 by **concept**, not wording. Set 01's JavaScript covered equality, scope, closures, event loop, hoisting, `null`/`undefined`, bubbling, `map`, `async`; set 02 deliberately goes elsewhere (`this`, truthiness, `NaN`, spread, destructuring, reference equality, `Promise.all`, JSON, delegation, coercion). Subnetting moved from /26 and /28 to /27, /30, masks, network and broadcast addresses. `set-01.md` was not edited. |

**To extend:** say *"extend the question bank"* and name a subject. New questions go into a **new
file** — `set-02.md` — with IDs continuing from where `set-01.md` ends. `set-01.md` is never edited,
renumbered or reordered, so it stays a clean record of what you have already practised.
