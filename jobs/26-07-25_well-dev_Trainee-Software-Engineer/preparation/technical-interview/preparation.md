> **No plan exists for this stage yet.** This material is written and parked. When you want it,
> say *"prepare me for the technical interview"* and a `plan.md` will be built around the time you have.
> Questions: [`question-bank/set-01.md`](question-bank/set-01.md).

# Round 2 preview — concurrency, passwords, caching

> **⚠️ Round-2 material — read only after the MCQ.** None of it is in the reported MCQ topic list. It is round-2 interview material, parked here so it isn't lost. If you are short on time today, **skip this file** — it is the correct thing to cut.

## The 60-second version

Round 2 reportedly asks three practical system questions: two people booking the same seat at once, storing passwords so even an admin cannot read them, and caching. You handle all three in production already; this is about saying them cleanly.

---

## 1. The double-booking problem

*Reported question: "two people reserving the same ticket at the same time — how do you handle it?"*

**In plain words:** two requests read "seat is free" at the same moment, and both write "booked". The read and the write were not one indivisible step. That is a **race condition**.

Three fixes, cheapest first:

| Fix | How | When |
|---|---|---|
| **Database constraint** | A unique constraint on (event, seat). The second insert simply fails. | Always. The last line of defence. |
| **Pessimistic lock** | `SELECT ... FOR UPDATE` inside a transaction — lock the row, so the second request waits. | High contention, short transactions |
| **Optimistic lock** | Keep a version number; on write, check it hasn't changed. Retry if it has. | Low contention |

**Your own version of this:** ProspectLead reserves credits when a job is dispatched, so a user cannot overspend on concurrent jobs, then finalises on the callback and refunds the difference. *(`PROFILE.md` §7.3)*

### Say this out loud
"That's a race condition — both requests read the seat as free before either writes. I'd wrap it in a transaction and take a row-level lock so the second request waits, and back that with a unique constraint on event and seat so even if the application logic fails, the database refuses the double booking. I've built the same shape for credits: reserve on submit so concurrent jobs can't overspend, then finalise and refund on the callback."

---

## 2. Storing passwords safely

*Reported question: "how can passwords be secured so no one, even the administrator, can view them?"*

**In plain words: you never store the password.** You store a one-way fingerprint of it. Checking a login means fingerprinting the attempt and comparing fingerprints.

- **Hashing** is one-way. You cannot reverse it.
- **Salting** adds a unique random value per user before hashing, so two people with the same password get different hashes — and a precomputed rainbow table is useless.
- Use a **slow** algorithm built for passwords — **bcrypt**, scrypt or Argon2. Never plain MD5 or SHA-256, which are fast and therefore easy to brute-force.

### Say this out loud
"You never store the password itself, only a one-way hash — so an administrator with full database access still can't read it. Each password gets a unique random salt before hashing, which kills rainbow-table attacks and means identical passwords produce different hashes. And you use a deliberately slow algorithm like bcrypt or Argon2, because a fast hash like plain SHA-256 is exactly what makes brute-forcing cheap."

---

## 3. Caching

*Reported questions: "cache-to-RAM storage solutions", "how do you show a very large dataset?"*

**In plain words:** a cache keeps the answer to an expensive question in fast memory so you don't have to ask again. **Redis** is the standard answer — an in-memory key-value store.

- **Cache-aside:** check the cache; on a miss, read the database and write it back.
- **TTL:** every cached entry expires, so it cannot go stale forever.
- **Invalidation:** clear the entry when the underlying data changes. This is the genuinely hard part.

You use Redis in production as a cache backend, a Celery broker, an OTP store and a Channels layer. *(`PROFILE.md` §12)*

### Say this out loud
"I'd put Redis in front of it — an in-memory key-value store, cache-aside: check Redis, and on a miss read Postgres and write the result back with a TTL. The hard part is invalidation, so I clear the key when the underlying record changes rather than relying on expiry alone. I use Redis in production for caching, as a Celery broker, as an OTP store and as a Channels layer."

---

## Also likely in round 2

- **Threading** — one process, several threads sharing memory; needs locks to stay safe. In Python the GIL means threads help with input/output waiting, not with CPU-bound maths — for that you use processes.
- **Detecting database changes** — triggers, an audit table, `updated_at` timestamps, or change-data-capture.
- **"Write code to create a directory and a text file with Hello World in it."** Practise this in Python once; it is three lines and they want to watch you type calmly.

```python
import os
os.makedirs("demo", exist_ok=True)
with open("demo/hello.txt", "w") as f:
    f.write("Hello World")
```

## Listen instead — search YouTube for

- `Race condition and database locking explained` — about 10 minutes
- `Password hashing and salting explained` — about 8 minutes
