> **No plan exists for this stage yet.** This material is written and parked. When you want it,
> say *"prepare me for the HR interview"* and a `plan.md` will be built around the time you have.
> Questions: [`question-bank/set-01.md`](question-bank/set-01.md).

# Your story — the four questions only you can be asked

## The 60-second version

Four questions are near-certain in the interview rounds, and none of them are technical. Why a trainee role when you are a Senior Python Executive. Whether you will actually stay. A concrete example of learning a stack while building it. And how you verify AI-generated code. Rehearse these four out loud until they are boring.

## Why this matters for this job

The JD asks for a prepared learning example in writing: *"Candidates should be prepared to discuss a concrete example during the interview."* It screens out people planning to study abroad and asks for *"a long-term career with WellDev."* And round 2 reportedly asks **detailed questions straight off your CV**.

---

## 1. "Why are you applying to a trainee role?"

**Do not pretend to be less experienced than you are.** They have your CV; it says Senior Python Executive, eight production backends, promoted in eleven months.

The honest frame: their JD is not a normal fresher req. It asks for AI-output verification, specification skill and learning velocity above coding throughput — and you can evidence all three. Their own line, *"6 Months in Standard Case — can be reduced for extraordinary performers"*, is the lever.

### Say this out loud
"I read your posting closely and it isn't a standard fresher req — it weights verifying AI output, decomposing ambiguous problems into specifications, and learning velocity above raw coding throughput. Those are the three things I can actually evidence. I'd rather join a company whose engineering standards I want to learn, at the level they hire at, than optimise for a title. And your own posting says the probation can be shortened for strong performers — I'd like the chance to earn that."

---

## 2. "Will you stay? What about Omnyvora, or higher studies?"

Two flight-risk flags: the JD screens out people planning to study abroad, and your CV shows you founded your own organisation in June 2026.

Be straight about both. Omnyvora is where you teach yourself things your day job doesn't cover — Next.js 16, React 19, a design system. It is a learning vehicle, not a competing employer.

### Say this out loud
"No plans for higher studies abroad — I want to build a career here. On Omnyvora: it's my own project where I taught myself the frontend and design side, Next.js, React, a token-based design system. It's how I learn, the same way some people do open source. It runs on my own time and it's never conflicted with delivery — I shipped eight client backends in the same period."

---

## 3. "Tell me about learning a stack while building it"

Three true options *(all from `PROFILE.md`)*. **Use the second — highest stakes, real deadline, client-facing.**

| Option | Evidence |
|---|---|
| PHP/MySQL → production Django, self-taught in under a year | §2, §4.3 |
| **FastAPI + Tortoise ORM learned on live client work under deadline** ⭐ | §7.2, §7.6, §7.7 |
| Next.js 16 / React 19 / TypeScript self-taught to build Omnyvora | §8.2 |

### Say this out loud
"My whole backend career started that way — I came out of university on PHP and MySQL, and taught myself Django to production standard in under a year. The sharpest example, though, is FastAPI. I'd only ever worked in Django when I was put on a client project built on FastAPI with Tortoise ORM and Aerich migrations — a different framework, async, a different ORM, and a live deadline. I read the primary docs and the framework source rather than tutorials, shipped it, and then led two more FastAPI projects after it."

---

## 4. "How do you use AI tools, and how do you verify them?"

The JD's headline requirement. Two concrete, verifiable examples — do not answer in generalities.

- **`ai_rules.md` on the LookUp project** — an engineering constitution you wrote governing agent-assisted work: performance-first (mandating `select_related`/`prefetch_related`), strict separation of concerns, no placeholders or pseudo-implementations. *(`PROFILE.md` §7.5)*
- **The DRF permission gap** — Django REST Framework's `DjangoModelPermissions` deliberately skips the `view_<model>` check on safe methods, so any authenticated user can read any model. You found it by **reading the framework source**, and wrote `StrictDjangoModelPermissions` to close it. *(`PROFILE.md` §8.1)*

### Say this out loud
"I use Claude Code and Cursor daily, but I treat them as accelerators, not authors — architecture and data modelling stay mine. Every repo I own carries a hand-written context file that encodes the rules the agent has to follow; on one project I wrote a full engineering constitution — performance-first, no placeholder implementations, strict separation of concerns. The verification habit is the same one that made me read Django REST Framework's source and find that its default permission class skips the view check on safe methods, which means any authenticated user can read any model. I wrote a stricter permission class to close it. I don't accept defaults, from a framework or from a model."

---

## The trap

**Salary.** You currently earn above 50,000 BDT and this role pays that through a six-month probation. If HR asks your expectation and you have not decided your number, you will either overshoot and end the process or undershoot and regret it. **Decide it before the call, not during.**

## Also expect

- Your **five-year plan** · biggest **strengths and weaknesses** · a **difficult colleague** · a **tight deadline** · what you expect from a workplace. All reported at WellDev. See [`question-bank/set-01.md`](question-bank/set-01.md).
- **CV-based drill-down.** Round 2 reportedly goes deep on whatever you wrote. Every line on your CV is fair game — see [`question-bank/set-01.md`](question-bank/set-01.md).

## Listen instead

Read each of the four "Say this out loud" blocks above into your phone's voice recorder, then play them back while walking. Hearing your own answer is what makes it stop sounding rehearsed.
