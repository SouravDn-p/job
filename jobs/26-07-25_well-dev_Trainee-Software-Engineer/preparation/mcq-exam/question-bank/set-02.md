# Question bank — set 02

**48 questions.** Added 31 July 2026 to fill the ranked coverage gaps in [`INDEX.md`](INDEX.md).

`set-01.md` is untouched. IDs continue from where it ended. **No concept here repeats one in set 01** —
checked question by question.

**What this set closes:** JavaScript 10 → 25 · subnetting 2 → 10 · analytical reasoning 8 → 20 ·
SQL joins 1 → 6 · sorting *traces* 0 → 4 · operating systems 0 → 4. Harder overall: **10 Hard items
here against 2 in set 01.**

Six subjects below. Answers collapsed — commit before you open one.

---

## JavaScript · Q-JS-011 – 025

> Your weakest subject and the one that leads their reported topic list. Set 01 covered equality,
> scope, closures, the event loop, hoisting, `null`/`undefined`, bubbling, `map` and `async`.
> These fifteen go elsewhere.

### Q-JS-011 · this · Hard · [Pattern]

```javascript
const obj = {
  name: "A",
  regular() { return this.name; },
  arrow: () => this.name
};
```
What do `obj.regular()` and `obj.arrow()` return?

A. "A" and "A" · B. "A" and `undefined` · C. `undefined` and "A" · D. Both throw

<details>
<summary>Answer</summary>

**Short answer (say this):** "A" and `undefined`.

**Why:** a regular method gets `this` from **how it is called** — `obj.regular()` means `this` is `obj`. An arrow function has no `this` of its own; it inherits from where it was **defined**, which here is the outer scope, not the object. This is the single most common `this` trap.

**They may follow up with:** "When *should* you use an arrow function?" — callbacks inside a method, where you want to keep the outer `this`.
</details>

---

### Q-JS-012 · loops · Hard · [Pattern]

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```
Output?

A. 0 1 2 · B. 3 3 3 · C. 0 0 0 · D. 2 2 2

<details>
<summary>Answer</summary>

**Short answer (say this):** 3 3 3.

**Why:** `var` is function-scoped, so all three callbacks close over the **same** `i`. By the time the timers fire, the loop has finished and `i` is 3. Change `var` to `let` and you get 0 1 2, because `let` creates a fresh binding per iteration.

**Why it's asked:** it tests scope, closures and the event loop in one question.
</details>

---

### Q-JS-013 · types · Medium · [Pattern]

Which of these is **truthy** in JavaScript?

A. `0` · B. `""` · C. `[]` · D. `NaN`

<details>
<summary>Answer</summary>

**Short answer (say this):** `[]` — an empty array is truthy.

**Why:** the falsy values are exactly six: `false`, `0`, `""`, `null`, `undefined`, `NaN`. Everything else is truthy, including empty arrays and empty objects. That surprises people coming from Python, where `[]` is falsy. **Switch languages in your head.**
</details>

---

### Q-JS-014 · types · Medium · [Pattern]

What does `NaN === NaN` return?

A. `true` · B. `false` · C. `undefined` · D. Throws

<details>
<summary>Answer</summary>

**Short answer (say this):** `false` — `NaN` is the only value not equal to itself.

**Why:** that is why you test for it with `Number.isNaN(x)` rather than `x === NaN`. `typeof NaN` is also `"number"`, which is its own oddity.
</details>

---

### Q-JS-015 · operators · Medium · [Pattern]

What is `typeof []` and `Array.isArray([])`?

A. `"array"` and `true` · B. `"object"` and `true` · C. `"object"` and `false` · D. `"list"` and `true`

<details>
<summary>Answer</summary>

**Short answer (say this):** `"object"` and `true`.

**Why:** `typeof` cannot distinguish an array from an object — both report `"object"`. That is exactly why `Array.isArray()` exists. Same family as `typeof null === "object"`.
</details>

---

### Q-JS-016 · spread · Easy · [Pattern]

What does `[...[1,2], ...[3,4]]` produce?

A. `[[1,2],[3,4]]` · B. `[1,2,3,4]` · C. `[1,2]` · D. Error

<details>
<summary>Answer</summary>

**Short answer (say this):** `[1,2,3,4]`.

**Why:** the spread operator unpacks an iterable into its elements. It also copies: `const b = [...a]` gives a **shallow** copy, so nested objects are still shared. Same idea as `*args` unpacking in Python.
</details>

---

### Q-JS-017 · destructuring · Easy · [Pattern]

```javascript
const { a, b = 5 } = { a: 1 };
```
What are `a` and `b`?

A. 1 and `undefined` · B. 1 and 5 · C. `undefined` and 5 · D. Error

<details>
<summary>Answer</summary>

**Short answer (say this):** 1 and 5.

**Why:** destructuring pulls properties out by name, and a default value is used when the property is **missing or `undefined`**. Note it does *not* apply when the value is `null` — `{ b: null }` leaves `b` as `null`, not 5.
</details>

---

### Q-JS-018 · equality · Medium · [Pattern]

What does `{} === {}` return?

A. `true` · B. `false` · C. `undefined` · D. Throws

<details>
<summary>Answer</summary>

**Short answer (say this):** `false`.

**Why:** objects and arrays are compared **by reference**, not by contents. Two separately created objects are two different references, however identical they look. `const a = {}; const b = a; a === b` would be `true`.
</details>

---

### Q-JS-019 · promises · Hard · [Pattern]

What does `Promise.all([p1, p2, p3])` do if `p2` rejects?

A. Waits for all three, then reports the error
B. Rejects immediately with `p2`'s error, discarding the other results
C. Resolves with two results and one `undefined`
D. Retries `p2`

<details>
<summary>Answer</summary>

**Short answer (say this):** It rejects immediately with that error — all-or-nothing.

**Why:** `Promise.all` is for "I need every one of these to succeed". If you want every result regardless of failures, use `Promise.allSettled`, which resolves with a status for each.
</details>

---

### Q-JS-020 · async · Medium · [Pattern]

How do you catch an error from an `await`ed call?

A. `.catch()` only · B. A `try`/`catch` block around the `await` · C. Errors can't be caught · D. `if (err)`

<details>
<summary>Answer</summary>

**Short answer (say this):** Wrap the `await` in `try`/`catch` — a rejected promise becomes a thrown error.

**Why:** that is the whole ergonomic point of `async`/`await` — asynchronous errors behave like ordinary synchronous ones. Identical to Python's `try`/`except` around an `await`.
</details>

---

### Q-JS-021 · arrays · Medium · [Pattern]

`find` vs `filter` — what's the difference?

A. Identical · B. `find` returns the first matching **element**; `filter` returns an **array** of all matches · C. `find` returns an index · D. `filter` mutates the array

<details>
<summary>Answer</summary>

**Short answer (say this):** `find` gives you the first matching element (or `undefined`); `filter` gives you an array of every match (possibly empty).

**Why:** the related pair is `some` (is at least one true?) and `every` (are all true?), both returning booleans. `findIndex` gives the position instead of the element.
</details>

---

### Q-JS-022 · JSON · Easy · [Pattern]

What does `JSON.stringify({ a: undefined, b: 1 })` produce?

A. `{"a":undefined,"b":1}` · B. `{"a":null,"b":1}` · C. `{"b":1}` · D. Throws

<details>
<summary>Answer</summary>

**Short answer (say this):** `{"b":1}` — keys with `undefined` values are dropped entirely.

**Why:** `undefined`, functions and symbols are omitted from objects during stringification. Inside an *array*, though, `undefined` becomes `null` — because array positions cannot vanish.
</details>

---

### Q-JS-023 · events · Medium · [Pattern]

What is event delegation?

A. Passing an event to another function
B. Putting one listener on a parent to handle events from many children, using bubbling
C. Delegating events to a web worker
D. Preventing the default action

<details>
<summary>Answer</summary>

**Short answer (say this):** B — one listener on the parent, using bubbling to catch events from any child.

**Why:** it means you don't attach a thousand listeners to a thousand rows, and it keeps working for elements added later. Bubbling (set 01, `Q-JS-007`) is the mechanism; delegation is what you *do* with it.
</details>

---

### Q-JS-024 · functions · Medium · [Pattern]

What is the difference between a function declaration and a function expression?

A. None
B. A declaration is fully hoisted and callable before its line; an expression is not
C. An expression is faster
D. Declarations cannot take parameters

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** `function foo() {}` is hoisted whole, so you can call it above where it is written. `const foo = function() {}` only hoists the `const` binding, so calling it early throws. Connects directly to hoisting in set 01.
</details>

---

### Q-JS-025 · strings · Easy · [Pattern]

What does `"5" + 3` evaluate to, and what does `"5" - 3`?

A. 8 and 2 · B. `"53"` and 2 · C. `"53"` and `"53"` · D. 8 and `"53"`

<details>
<summary>Answer</summary>

**Short answer (say this):** `"53"` and `2`.

**Why:** `+` is overloaded — if either side is a string it **concatenates**. `-` has no string meaning, so it coerces both sides to numbers. This inconsistency is a favourite MCQ, and it is pure JavaScript weirdness: Python would raise a TypeError for both.
</details>

---

## Networking & subnetting · Q-NET-013 – 020

> Set 01 covered status codes, /26 and /28, TCP vs UDP, browsing a URL, REST verbs, idempotency,
> health checks and caching. These eight are subnetting drill plus addressing.

### Q-NET-013 · subnetting · Easy · [Pattern]

Usable hosts in a **/27**?

A. 32 · B. 30 · C. 16 · D. 14

<details>
<summary>Answer</summary>

**Short answer (say this):** 30. — 32 − 27 = 5 host bits → 2⁵ = 32 → minus 2 → **30**.
</details>

---

### Q-NET-014 · subnetting · Easy · [Pattern]

Usable hosts in a **/30**, and what is it used for?

A. 4, for small offices · B. 2, for point-to-point links between routers · C. 6, for printers · D. 8

<details>
<summary>Answer</summary>

**Short answer (say this):** 2 — and that is exactly why it's used for router-to-router links, where you only ever need two addresses.
</details>

---

### Q-NET-015 · subnetting · Medium · [Pattern]

What is the subnet mask for a **/26**?

A. 255.255.255.0 · B. 255.255.255.128 · C. 255.255.255.192 · D. 255.255.255.224

<details>
<summary>Answer</summary>

**Short answer (say this):** 255.255.255.192.

**Why:** /26 means 26 network bits. The last octet has 2 network bits set: 128 + 64 = **192**. The ladder for the final octet: /25→128, /26→192, /27→224, /28→240, /29→248, /30→252.
</details>

---

### Q-NET-016 · subnetting · Hard · [Pattern]

For host address **192.168.1.100/26**, what is the network address?

A. 192.168.1.0 · B. 192.168.1.64 · C. 192.168.1.100 · D. 192.168.1.128

<details>
<summary>Answer</summary>

**Short answer (say this):** 192.168.1.64.

**Why:** a /26 gives blocks of 64 addresses: 0–63, 64–127, 128–191, 192–255. 100 falls in the second block, so the network address is **64** and the broadcast is **127**. Usable range 65–126.

**Method:** block size = 256 − mask octet = 256 − 192 = 64. Then count up in 64s until you pass your host.
</details>

---

### Q-NET-017 · subnetting · Hard · [Pattern]

Broadcast address for **10.0.0.20/29**?

A. 10.0.0.23 · B. 10.0.0.24 · C. 10.0.0.31 · D. 10.0.0.255

<details>
<summary>Answer</summary>

**Short answer (say this):** 10.0.0.23.

**Why:** /29 → block size 8 → blocks are 0–7, 8–15, 16–23, 24–31. Address 20 sits in 16–23, so the network is 16, the broadcast is **23**, and usable hosts are 17–22 (six of them).
</details>

---

### Q-NET-018 · addressing · Medium · [Pattern]

Which is a **private** IP range?

A. 11.0.0.0/8 · B. 172.16.0.0/12 · C. 8.8.8.0/24 · D. 200.1.1.0/24

<details>
<summary>Answer</summary>

**Short answer (say this):** 172.16.0.0/12.

**Why:** the three private ranges are **10.0.0.0/8**, **172.16.0.0/12** (that's 172.16 through 172.31) and **192.168.0.0/16**. Not routable on the public internet — they sit behind NAT.
</details>

---

### Q-NET-019 · subnetting · Medium · [Pattern]

How many /26 subnets fit inside a single /24?

A. 2 · B. 4 · C. 8 · D. 16

<details>
<summary>Answer</summary>

**Short answer (say this):** 4.

**Why:** you borrowed 2 bits (24 → 26), and 2² = 4. Each holds 64 addresses; 4 × 64 = 256, the whole /24. **Borrowed bits give you subnets; remaining bits give you hosts.**
</details>

---

### Q-NET-020 · DNS · Easy · [Pattern]

What does DNS actually do?

A. Encrypts traffic · B. Translates a domain name into an IP address · C. Routes packets · D. Assigns IP addresses to new devices

<details>
<summary>Answer</summary>

**Short answer (say this):** Translates a human-readable domain name into an IP address.

**Why:** D is DHCP — a very common distractor. DNS is the first step when you open a URL, because you cannot connect to a name, only to an address.
</details>

---

## Analytical reasoning · Q-APT-009 – 020

> Set 01 covered percentage change, work rate, average speed, number series, ratios, two-eggs,
> river crossing and coin weighing. These twelve are new shapes. **Timer on: 90 seconds each.**

### Q-APT-009 · profit · Medium · [Pattern]

An item bought for 800 is sold for 1,000. What is the profit percentage?

A. 20% · B. 25% · C. 22% · D. straight 200

<details>
<summary>Answer</summary>

**Short answer (say this):** 25%.

**Why:** profit percentage is always calculated on the **cost price**, not the selling price. 200 ÷ 800 = 0.25. Choosing 20% means you divided by 1,000 — that is the trap.
</details>

---

### Q-APT-010 · interest · Easy · [Pattern]

Simple interest on 5,000 at 8% per year for 3 years?

A. 1,200 · B. 1,300 · C. 400 · D. 1,500

<details>
<summary>Answer</summary>

**Short answer (say this):** 1,200.

**Why:** principal × rate × time ÷ 100 = 5000 × 8 × 3 ÷ 100. Simple interest is on the original amount every year; compound interest would earn on the interest too and give slightly more.
</details>

---

### Q-APT-011 · probability · Medium · [Pattern]

Two fair coins are tossed. Probability of getting **exactly one** head?

A. 1/4 · B. 1/2 · C. 3/4 · D. 1/3

<details>
<summary>Answer</summary>

**Short answer (say this):** 1/2.

**Why:** four equally likely outcomes — HH, HT, TH, TT. Two of them have exactly one head, so 2/4. The common error is answering 1/4 by forgetting that HT and TH are different outcomes.
</details>

---

### Q-APT-012 · probability · Medium · [Pattern]

A bag has 3 red and 5 blue balls. One is drawn at random. Probability it is red?

A. 3/5 · B. 3/8 · C. 5/8 · D. 1/3

<details>
<summary>Answer</summary>

**Short answer (say this):** 3/8.

**Why:** favourable ÷ total. Total is 3 + 5 = 8, not 5. Denominator errors are the whole game in these.
</details>

---

### Q-APT-013 · trains · Hard · [Pattern]

A 120 m train travelling at 36 km/h crosses a pole. How long does it take?

A. 6 s · B. 12 s · C. 10 s · D. 20 s

<details>
<summary>Answer</summary>

**Short answer (say this):** 12 seconds.

**Why:** convert first — 36 km/h × (5/18) = 10 m/s. Crossing a **pole** means covering just the train's own length: 120 ÷ 10 = 12 s. If it crossed a 80 m *platform*, the distance would be 120 + 80 = 200 m.

**Memorise:** km/h → m/s is × 5/18. m/s → km/h is × 18/5.
</details>

---

### Q-APT-014 · pipes · Medium · [Pattern]

Pipe A fills a tank in 4 hours, pipe B in 6. Both open together — how long?

A. 5 h · B. 2.4 h · C. 2 h · D. 3 h

<details>
<summary>Answer</summary>

**Short answer (say this):** 2.4 hours.

**Why:** same as work rate. 1/4 + 1/6 = 3/12 + 2/12 = 5/12 per hour, so the time is 12/5 = 2.4. If a pipe were *draining*, you would subtract its rate instead.
</details>

---

### Q-APT-015 · ages · Medium · [Pattern]

A father is 3× his son's age. In 10 years he will be 2× the son's age. How old is the son now?

A. 8 · B. 10 · C. 12 · D. 15

<details>
<summary>Answer</summary>

**Short answer (say this):** 10.

**Why:** let the son be s, father 3s. In ten years: 3s + 10 = 2(s + 10) → 3s + 10 = 2s + 20 → s = 10. Age problems are always one equation — write it rather than guessing.
</details>

---

### Q-APT-016 · averages · Medium · [Pattern]

The average of 5 numbers is 20. One number is removed and the average becomes 22. What was removed?

A. 12 · B. 20 · C. 8 · D. 18

<details>
<summary>Answer</summary>

**Short answer (say this):** 12.

**Why:** work in **totals**, never averages. 5 × 20 = 100. 4 × 22 = 88. The difference is 12. Averages cannot be added or subtracted directly; totals can.
</details>

---

### Q-APT-017 · series · Medium · [Pattern]

Next in the series: 3, 6, 11, 18, 27, __?

A. 36 · B. 38 · C. 40 · D. 34

<details>
<summary>Answer</summary>

**Short answer (say this):** 38.

**Why:** the gaps are 3, 5, 7, 9 — consecutive odd numbers. The next gap is 11, so 27 + 11 = 38.
</details>

---

### Q-APT-018 · letter series · Medium · [Pattern]

Next in the series: A, C, F, J, O, __?

A. S · B. T · C. U · D. R

<details>
<summary>Answer</summary>

**Short answer (say this):** U.

**Why:** convert letters to numbers: 1, 3, 6, 10, 15 — the gaps are 2, 3, 4, 5. The next gap is 6, so 15 + 6 = 21 = **U**. Always convert letters to positions before looking for the rule.
</details>

---

### Q-APT-019 · direction · Medium · [Pattern]

You walk 3 km north, turn right and walk 4 km. How far are you from the start, and in which direction?

A. 7 km north-east · B. 5 km north-east · C. 5 km east · D. 1 km north

<details>
<summary>Answer</summary>

**Short answer (say this):** 5 km, to the north-east.

**Why:** turning right from north faces you east, so it is a 3-4-5 right triangle. Draw it — direction problems are almost always solved by sketching, not by reasoning in your head.
</details>

---

### Q-APT-020 · logic · Hard · [Pattern]

All engineers are graduates. Some graduates are managers. Which **must** be true?

A. Some engineers are managers
B. All managers are graduates
C. Some graduates are engineers
D. No engineer is a manager

<details>
<summary>Answer</summary>

**Short answer (say this):** C.

**Why:** if every engineer is a graduate, then engineers form a subset of graduates, so some graduates are certainly engineers. A *might* be true but is not guaranteed. B reverses the second statement. D is unsupported. **Syllogisms ask what must follow, never what sounds likely.**
</details>

---

## Sorting traces · Q-DSA-023 – 026

> Set 01 tested sorting *recognition* — complexities and stability. These four test *tracing*, which
> is a different skill and is the one that gets careless marks.

### Q-DSA-023 · bubble sort · Medium · [Pattern]

Array `[5, 1, 4, 2]`. What is it after **one complete pass** of bubble sort (ascending)?

A. `[1, 4, 2, 5]` · B. `[1, 2, 4, 5]` · C. `[5, 4, 2, 1]` · D. `[1, 5, 4, 2]`

<details>
<summary>Answer</summary>

**Short answer (say this):** `[1, 4, 2, 5]`.

**Why:** compare and swap each adjacent pair left to right. 5>1 swap → `[1,5,4,2]`. 5>4 swap → `[1,4,5,2]`. 5>2 swap → `[1,4,2,5]`. **After pass one, the largest element is always in its final position** — that is the signature of bubble sort.
</details>

---

### Q-DSA-024 · selection sort · Medium · [Pattern]

Array `[29, 10, 14, 37, 13]`. After **two passes** of selection sort (ascending)?

A. `[10, 13, 14, 37, 29]` · B. `[10, 13, 29, 37, 14]` · C. `[10, 14, 13, 37, 29]` · D. `[13, 10, 14, 37, 29]`

<details>
<summary>Answer</summary>

**Short answer (say this):** `[10, 13, 14, 37, 29]` — option A.

**Why:** trace it one swap at a time.
- **Pass 1** — smallest of the whole array is 10, at index 1. Swap with index 0 → `[10, 29, 14, 37, 13]`.
- **Pass 2** — smallest of what's left (indices 1–4) is 13, at index 4. Swap with index 1 → `[10, 13, 14, 37, 29]`.

**The signature of selection sort:** exactly **one swap per pass**, and after k passes the first k positions are final. Bubble sort by contrast makes many swaps per pass and finalises from the *end*. If a question asks which algorithm produced a given intermediate state, count the swaps.
</details>

---

### Q-DSA-025 · quicksort · Hard · [Pattern]

Array `[7, 2, 9, 4]`, pivot = last element (4). What does the array look like after **one partition**?

A. `[2, 4, 9, 7]` · B. `[2, 4, 7, 9]` · C. `[4, 2, 7, 9]` · D. `[2, 7, 9, 4]`

<details>
<summary>Answer</summary>

**Short answer (say this):** `[2, 4, 9, 7]`.

**Why:** partitioning puts everything smaller than the pivot to its left and everything larger to its right, then places the pivot in between. Only 2 is smaller than 4, so 2 goes first, then the pivot 4, then 9 and 7 in whatever order the swaps left them. **The pivot lands in its final sorted position — that is the guarantee partitioning gives you.**
</details>

---

### Q-DSA-026 · merge sort · Medium · [Pattern]

Merging two sorted halves `[1, 4, 8]` and `[2, 3, 9]` — what is the first comparison, and the result?

A. Compare 1 and 2 → result `[1,2,3,4,8,9]` · B. Compare 8 and 9 → `[1,2,3,4,8,9]` · C. No comparison needed · D. `[1,4,8,2,3,9]`

<details>
<summary>Answer</summary>

**Short answer (say this):** Compare the two **front** elements, 1 and 2, then keep taking the smaller front. Result `[1,2,3,4,8,9]`.

**Why:** merging only ever compares the heads of the two lists, which is why it is O(n) per merge and O(n log n) overall — and why it needs O(n) extra space for the output.
</details>

---

## Operating systems · Q-OS-001 – 004

> Zero coverage in set 01, and "kernel" appears in the reported short-answer list. Four questions —
> enough to not be blank, not enough to cost you time.

### Q-OS-001 · kernel · Easy · [Pattern]

What is the kernel?

A. The command-line shell
B. The core of the operating system that manages memory, processes, devices and system calls
C. The bootloader
D. A CPU instruction set

<details>
<summary>Answer</summary>

**Short answer (say this):** B — the core layer that manages hardware and mediates every request from a program.

**Why:** the shell is what *you* type into; the kernel is what actually talks to hardware. Programs reach it through **system calls**. It runs in privileged **kernel mode**; your code runs in **user mode**.
</details>

---

### Q-OS-002 · process vs thread · Medium · [Pattern]

Difference between a process and a thread?

A. Identical
B. A process has its own memory space; threads live inside a process and share its memory
C. Threads are slower to create
D. A process can only have one thread

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** shared memory makes threads cheap to create and to communicate between, but it is also why they need locks — two threads writing the same variable is a race condition. Processes are isolated, so they are safer but need explicit inter-process communication.

**Your version:** in Python the GIL means threads help with I/O waiting, not CPU-bound work — for that you use processes.
</details>

---

### Q-OS-003 · deadlock · Hard · [Pattern]

Which is **not** one of the four conditions required for deadlock?

A. Mutual exclusion · B. Hold and wait · C. **Preemption** · D. Circular wait

<details>
<summary>Answer</summary>

**Short answer (say this):** Preemption — the condition is actually **no** preemption.

**Why:** all four must hold simultaneously: mutual exclusion, hold and wait, no preemption, and circular wait. Break any one and deadlock is impossible — which is exactly how you prevent it, usually by forcing a consistent lock ordering to break circular wait.
</details>

---

### Q-OS-004 · memory · Medium · [Pattern]

What is virtual memory?

A. RAM soldered to the motherboard
B. An abstraction giving each process its own address space, with pages moved between RAM and disk as needed
C. The CPU cache
D. Memory used only by the kernel

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** each process believes it has a large contiguous memory of its own. The OS maps those virtual pages to real physical frames, and swaps pages to disk when RAM runs short. **Thrashing** is when it spends more time swapping than working.
</details>

---

## SQL joins · Q-DB-015 – 019

> Set 01 had one join question. These five go deeper, since joins are reported by name at WellDev.

### Q-DB-015 · joins · Medium · [Pattern]

A `CROSS JOIN` between a 5-row table and a 4-row table returns how many rows?

A. 9 · B. 5 · C. 20 · D. 0

<details>
<summary>Answer</summary>

**Short answer (say this):** 20 — every row paired with every row.

**Why:** a cross join is the Cartesian product, and it takes no `ON` clause. It is also what you accidentally create when you list two tables in `FROM` and forget the join condition — a classic cause of a query that hangs.
</details>

---

### Q-DB-016 · joins · Hard · [Pattern]

In a `LEFT JOIN`, what is the difference between putting a condition in `ON` versus in `WHERE`?

A. No difference
B. `ON` filters before the join, preserving unmatched left rows; `WHERE` filters after, which silently turns it into an inner join
C. `WHERE` is faster
D. `ON` only works with inner joins

<details>
<summary>Answer</summary>

**Short answer (say this):** B — and this is one of the most common real SQL bugs.

**Why:** a `LEFT JOIN` produces `NULL`s for unmatched right rows. If you then write `WHERE right.status = 'x'`, those `NULL` rows fail the test and disappear — you have lost exactly the rows the left join was there to keep. Put the condition in `ON` instead.
</details>

---

### Q-DB-017 · joins · Medium · [Pattern]

What is a self join, and when do you need one?

A. Joining a table to itself, e.g. employees to their managers in the same table
B. Joining two identical tables
C. A join with no condition
D. Joining a table to a view

<details>
<summary>Answer</summary>

**Short answer (say this):** A — the same table joined to itself under two aliases.

**Why:** it is how you walk a hierarchy stored in one table: `employees e JOIN employees m ON e.manager_id = m.id`. **Aliases are mandatory**, otherwise the database cannot tell which copy you mean.
</details>

---

### Q-DB-018 · joins · Medium · [Pattern]

You want every customer with the number of orders they've placed, **including customers with none**. What do you need?

A. `INNER JOIN` + `COUNT(*)`
B. `LEFT JOIN` + `COUNT(orders.id)`, grouped by customer
C. `CROSS JOIN` + `COUNT(*)`
D. Two separate queries

<details>
<summary>Answer</summary>

**Short answer (say this):** B — left join, and count the **orders column**, not `*`.

**Why:** two traps in one. An inner join drops customers with no orders. And `COUNT(*)` counts the joined row — which exists even when it is all `NULL`s — so zero-order customers would show 1. `COUNT(orders.id)` ignores `NULL`s and correctly returns 0.
</details>

---

### Q-DB-019 · joins · Easy · [Pattern]

`UNION` vs `JOIN`?

A. Identical
B. `JOIN` combines columns side by side; `UNION` stacks rows from two result sets on top of each other
C. `UNION` is faster
D. `UNION` only works on one table

<details>
<summary>Answer</summary>

**Short answer (say this):** B — join widens, union lengthens.

**Why:** `UNION` requires both queries to have the same number of columns with compatible types. `UNION` removes duplicates (and therefore sorts); `UNION ALL` keeps everything and is faster when you know there are no duplicates.
</details>
