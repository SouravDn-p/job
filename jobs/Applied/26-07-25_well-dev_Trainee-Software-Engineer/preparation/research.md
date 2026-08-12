# Research — WellDev, Trainee Software Engineer

**Researched:** 31 July 2026. Findings only, no teaching. Every claim carries a source and a confidence tag.

**Tags:** `[Verified]` = said by WellDev, or by a named candidate with a URL · `[Likely]` = several sources agree, none official · `[Assumed]` = no source, inferred.

---

## The 60-second version

WellDev runs **four stages**: an **MCQ test**, then a **one-hour technical interview**, then a **second technical interview with an HR half**, then a short **COO round**. The MCQ is the gate that fails most people, and it is **broad, not deep** — DSA, DBMS, OOP, networking, REST, JavaScript and maths reasoning all in one paper. A former WellDev interviewer said publicly that most questions are easy and any fresh graduate should have a basic idea; what they actually screen for is who can handle the **unconventional** ones.

---

## 1. The stages

| # | Stage | Format | Length | Confidence |
|---|---|---|---|---|
| 1 | **MCQ test** | Multiple choice, wide topic spread | Not found | `[Verified]` — JD + two candidate reports |
| 2 | **Technical interview 1** | Live, taken by a junior software engineer | ~1 hour | `[Verified]` |
| 3 | **Technical interview 2** | Two parts — ~20 min HR/behavioural, then technical with **two** engineers | Not found | `[Verified]` |
| 4 | **COO round** | Final conversation with the company COO | Not found | `[Likely]` |

- *"After dropping CV they take a MCQ Round, almost every candidate gets an email for participation in this round."* — `[Verified]`, [Interview BD](https://tamimehsan.github.io/interview-questions-bangladesh/companies/welldev)
- *"The COO round was easy, with the manager asking about the candidate's background and industry experience."* — `[Likely]`, same source.
- One conflicting source ([justcrackinterview.com](https://www.justcrackinterview.com/job-interviews/welldev-bangladesh-ltd/)) describes a 6-stage process with HackerRank/Codility coding tests. **It contradicts the two first-hand reports and reads as auto-generated SEO filler. Do not plan against it.** `[Assumed]` — low trust.

---

## 2. The exam

**It is a multiple-choice test, not a coding test.** No candidate report mentions a take-home or an online coding judge at stage 1. `[Verified]`

**⚠️ It is described as ONSITE in the 2026 posting.** The JD says: *"shortlisted candidates will be informed via email regarding the **Onsite MCQ test**. The Onsite MCQ test is tentatively scheduled for **31 July 2026**."* The 2024 candidate reports describe a **remote** test with screen sharing. **This has changed.** Onsite means travelling to the WellDev Dhaka office and most likely sitting it on their machine or on paper. `[Verified]` that the JD says onsite; `[Assumed]` as to what the room looks like.

---

## 3. The platform

**Quilgo** (candidate blogs spell it "Quillgo"). `[Verified]` — named in both first-hand reports.

What Quilgo is: an online assessment tool with **AI proctoring** — a countdown timer, webcam snapshots and face detection, screen tracking and action tracking. It commonly runs on top of Google Forms. It does **not** use a locked-down browser. Admins set the start time, the duration and a hard submission deadline. `[Verified]` — [quilgo.com](https://quilgo.com/), [Quilgo FAQ](https://quilgo.com/hub/faq)

Reported rules in 2024: **screen share on, camera on for the whole test.** `[Verified]`

> Practical read: a hard timer with auto-submit is the thing to fear, not the proctoring. Pace matters more than perfection.

---

## 4. The rules

| Rule | Finding | Confidence |
|---|---|---|
| Duration | **Not found** | — |
| Number of questions | **Not found** | — |
| Negative marking | **Not found** | — |
| Cut-off score | **Not found** | — |
| Camera / screen | On, both, throughout (2024 remote format) | `[Verified]` |
| Language of the test | English | `[Assumed]` — every reported question is in English |

**Plan for the general case:** a hard-timed paper of mixed-topic MCQs where you cannot go back and re-open it. Practise with a clock.

---

## 5. Question patterns — the most important finding

The MCQ covers, in the reported words of the candidates:

> *"JavaScript fundamentals, OOP, DBMS, SWE principles, Networking, Rest API knowledge, Analytical reasoning, DSA (time complexity, sorting, binary trees, MST, greedy algorithms)"* — `[Verified]`, both sources agree word-for-word.

Networking specifically included **HTTP status codes and subnetting**. `[Verified]`

A real MCQ from a leaked WellDev paper begins: *"Suppose that items A, B, C, D and E are pushed in that order onto an initially empty stack S. S is then popped…"* — `[Verified]` that such a question exists ([Course Hero listing](https://www.coursehero.com/file/74748681/Well-DEV-QUESpdf/); full paper is paywalled and was not read).

**What this tells you:** the spread is wide and the depth is shallow. Nine subjects, MCQ-level. Breadth beats depth here.

**⚠️ JavaScript is on the list and you are a Python engineer.** This is the single biggest gap between the test and your CV. It is treated as a full topic in the plan.

---

## 6-7. Real candidate reports and their shared questions

Two first-hand sources, both naming rounds and questions:

- **Salman Farsi**, Trainee Software Engineer (ColdFusion), Sept 2024 — [blog](https://salman1804102.github.io/posts/2024/09/blog-post-1/) · [LinkedIn post](https://www.linkedin.com/posts/salmanfarsi0_my-interview-experience-with-welldev-for-activity-7237681143557300224-bk6l). Passed MCQ, passed round 1, eliminated after round 2. Published his question list deliberately to help others.
- **Interview BD**, a community archive of Bangladeshi company interviews — [WellDev page](https://tamimehsan.github.io/interview-questions-bangladesh/companies/welldev). Aggregates multiple candidates; question list overlaps Salman's and extends it.

**Reported questions — technical round 1** `[Verified]`

Array base address when you print the array name · array indexing vs linked-list access time · binary search on a sorted linked list · delete the middle element of a stack without another data structure · naming and complexity of a recursive sum function · time complexity of recursive Fibonacci · SQL clause **execution order** (FROM → WHERE → GROUP BY → HAVING → SELECT) · fixing redundant data by normalisation · finding duplicate rows in SQL · spotting an access-modifier violation in Java · OOP fundamentals · ACID properties · build a stack using queues · knight placement on a chessboard (DFS/BFS) · a GRE-style maths question.

**Reported questions — technical round 2** `[Verified]`

Health-check API and what GET does · write code to create a directory and a text file containing "Hello World" · **two people reserving the same ticket at the same time** — how do you handle it · how many APIs does a ticket system need · how do you store passwords so even an admin cannot read them (salting + hashing) · database triggers and cascading · showing a very large dataset (pagination) · what happens when you browse a website · SQL vs NoSQL · caching to RAM · **largest rectangle in a histogram** · **two eggs / 100 floors** · SQL for products sharing the same price · DELETE vs TRUNCATE vs DROP · threading · detecting database changes · **detailed questions straight off your CV** · move zeroes to the end of an array.

**Also listed by Interview BD** `[Verified]`: longest palindrome from a set of letters · Fibonacci with two variables · binary tree post-order traversal · two-sum · 3Sum · group anagrams · swap two variables without a temp · second-highest element · pre/post increment · reverse-iterate a BST · polymorphism · graph representations · two-pointer technique · abstract classes · sorting algorithms · encapsulation · linked list vs array performance · circular linked lists · which structure DFS and BFS use · string-searching structures · ER diagrams · kernel · joins · dependency injection · JavaScript events · improving a UI · stack/queue operations · reversing a linked list.

**Behavioural questions reported** `[Verified]`: why WellDev · your future plan · biggest strengths · five-year goal · commitment to learning new technology · strengths and weaknesses · will you commit full-time · salary expectation · a difficult colleague · tight deadlines · what you expect from a workplace · describe yourself.

---

## 8. The company

| Fact | Detail | Confidence |
|---|---|---|
| What it is | Custom software development — managed applications, staff augmentation, professional services | `[Verified]` — [welldev.io/careers](https://www.welldev.io/careers) |
| Headquarters | Switzerland (Zurich) | `[Likely]` |
| Offices | Bangladesh, Switzerland, Austria, Canada, Mauritius (South Africa also reported) | `[Verified]` — careers page |
| Tech stack | **Ruby on Rails**, React JS, Angular, Vue, **ColdFusion**, .NET, **FastAPI**, Flask, Express, Android, iOS, MySQL, **PostgreSQL**, **Redis** | `[Likely]` — company site + a WellDev engineer's public profile |
| Stated values | "Technology & human development go hand in hand" · inclusive team · hybrid work · learning with "industry-leading mentors" · real client projects | `[Verified]` — careers page |
| Growth story they tell | *"I joined as an intern… and grew into a quality control leader."* | `[Verified]` — careers page testimonial |

**Two things worth using in conversation:**

1. Their stack includes **FastAPI, PostgreSQL and Redis** — three things you use in production daily. Say so.
2. It includes **ColdFusion and Ruby on Rails** — languages you have never written. That is not a problem; it is the *reason* their JD is written around learning velocity. Being placed on an unfamiliar stack is the expected outcome, and your PHP→Django and FastAPI-on-a-deadline stories answer it directly.

---

## 9. The people

- **Philipp Wellstein** — WellDev leadership. Replied publicly to a rejected candidate encouraging them to keep learning and reapply, and invited them to the office. `[Verified]` — LinkedIn thread above.
- **Md Mokhlesur Rahman** — former WellDev interviewer. Said publicly: *"I found most of the questions… were easy and any fresh graduate should have at least a basic idea"*, and that WellDev looks for candidates who can *"handle those unconventional questions."* `[Verified]` — same thread.

**Read this correctly.** The bar is not obscure knowledge. The bar is staying composed on a question you have never seen. That is a rehearsable skill, and it is in the plan.

---

## 10. Knockouts — check these before you sit anything

| Gate | Your position | Action |
|---|---|---|
| Graduation + certificate by **August 2026** | Degree certificate issued 30 May 2024 ✅ | None |
| Age under 30 | Satisfied ✅ | None |
| Start **Sept–Nov 2026** | You are currently employed at Softvence | Know your notice period before they ask |
| **No plans for higher studies abroad** | JD screens this out explicitly | Have a settled answer |
| **Long-term commitment to WellDev** | You founded Omnyvora in June 2026 | Prepare an honest framing — see the behavioural bank |
| English **and** Bangla, both mandatory | Satisfied ✅ | None |
| **Salary** — 50,000 BDT during a 6-month probation | You are a Senior Python Executive taking a trainee req | Decide your number *before* the HR round asks |
| **CGPA** | Recorded 3.59, an older source says 3.42 — unverified | ⚠️ Fresher pipelines check transcripts. Confirm against the IUBAT transcript before any form asks. |

---

## What I could not find

| Gap | What I assumed instead |
|---|---|
| MCQ duration, question count, negative marking, pass mark | A hard-timed mixed paper. Practise at ~60–75 seconds per question. |
| The official recruitment-process PDF linked from the JD | **The Google Drive link requires a login and could not be read.** Open it yourself — it is the most authoritative source available and may state the duration and the round count. |
| Glassdoor's WellDev interview page | Blocked (HTTP 403). Its summary line — difficulty rated **2.8 / 5** by Trainee applicants — came through search results only. `[Likely]` |
| Whether the 2026 MCQ still matches the 2024 pattern | Assumed yes. **Caveat:** this JD was visibly rewritten for the AI era — it now weights AI-output verification and specification skill. The paper may have shifted with it. The 2024 topic list is still the best evidence available. |
| What "onsite" means in practice — their machine, your laptop, or paper | Assumed their office, their machine, closed book. Ask in the confirmation email if you can. |
| Exact MCQ questions | Only one is publicly quoted (the stack push/pop item). Everything in the question bank tagged `[Pattern]` was built by me to match the reported style — **it is not a leaked paper.** |

---

## Sources

- [Salman Farsi — WellDev Trainee Software Engineer interview experience (Sept 2024)](https://salman1804102.github.io/posts/2024/09/blog-post-1/)
- [Salman Farsi — LinkedIn post + comments from WellDev staff](https://www.linkedin.com/posts/salmanfarsi0_my-interview-experience-with-welldev-for-activity-7237681143557300224-bk6l)
- [Interview BD — WellDev Ltd question archive](https://tamimehsan.github.io/interview-questions-bangladesh/companies/welldev)
- [WellDev — Careers](https://www.welldev.io/careers)
- [Quilgo — assessment platform](https://quilgo.com/) · [Quilgo FAQ](https://quilgo.com/hub/faq)
- [Course Hero — "Well DEV QUES.pdf" listing](https://www.coursehero.com/file/74748681/Well-DEV-QUESpdf/) (paywalled, first line only)
- [justcrackinterview — WellDev Bangladesh](https://www.justcrackinterview.com/job-interviews/welldev-bangladesh-ltd/) — low trust, contradicts first-hand reports
- The archived JD in this folder: [job-description.md](../job-description.md)
