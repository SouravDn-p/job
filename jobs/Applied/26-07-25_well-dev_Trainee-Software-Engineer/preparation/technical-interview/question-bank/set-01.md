# Question bank — set 01

**18 questions** for the technical interview rounds. Built 31 July 2026.

> **No plan exists for this stage yet.** These are parked until you ask for technical-interview
> preparation. All 18 are **reported at WellDev by name** — see [`../../research.md`](../../research.md).

Coding problems (8) · spoken "explain X" answers (10).

---

## Coding problems

> All eight are **reported at WellDev** by name. These are asked live in the technical rounds, so practise saying the approach out loud *before* writing. Solutions in Python; the interviewer cares about the reasoning, not the syntax.

**How to answer a live coding question:** restate the problem → say the naive approach and its complexity → say the better approach and why → then write it. Narrating is half the mark.

---

### Q-COD-001 · arrays · Easy · [Reported]

Move all zeroes in an array to the end, keeping the order of the non-zero elements.
`[0,1,0,3,12]` → `[1,3,12,0,0]`

<details>
<summary>Answer</summary>

**Approach in plain words:** two pointers. One walks the array reading; the other marks where the next non-zero should be written. Then fill the rest with zeroes.

**Complexity:** O(n) time, O(1) space.

```python
def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
```

**They may follow up with:** "Can you do it in one pass?" — yes, swap `nums[read]` and `nums[write]` instead of a second loop.
</details>

---

### Q-COD-002 · hashing · Easy · [Reported]

Two Sum — given an array and a target, return the indices of the two numbers that add to the target.

<details>
<summary>Answer</summary>

**Approach in plain words:** as you walk the array, remember every number you've seen in a dictionary. For each number, check whether `target − number` is already in it.

**Complexity:** O(n) time, O(n) space. The nested-loop version is O(n²) — say that first, then improve it.

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```
</details>

---

### Q-COD-003 · two pointers · Medium · [Reported]

3Sum — find all unique triplets that sum to zero.

<details>
<summary>Answer</summary>

**Approach in plain words:** sort the array. Fix one number, then use two pointers moving inward from both ends of the rest to find pairs that complete the sum. Skip duplicates.

**Complexity:** O(n²) time after an O(n log n) sort.

```python
def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue                      # skip duplicate anchors
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:   lo += 1
            elif total > 0: hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                lo += 1; hi -= 1
    return res
```
</details>

---

### Q-COD-004 · hashing · Easy · [Reported]

Group anagrams — group words that are rearrangements of each other.

<details>
<summary>Answer</summary>

**Approach in plain words:** two words are anagrams if their sorted letters match. Use the sorted string as a dictionary key.

**Complexity:** O(n · k log k) for n words of length k.

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w))].append(w)
    return list(groups.values())
```

**They may follow up with:** "Avoid the sort?" — use a 26-length letter-count tuple as the key instead, giving O(n · k).
</details>

---

### Q-COD-005 · linked lists · Medium · [Reported]

Reverse a singly linked list.

<details>
<summary>Answer</summary>

**Approach in plain words:** three pointers — previous, current and next. Walk the list, and at each node point it backwards at the previous one.

**Complexity:** O(n) time, O(1) space.

```python
def reverse(head):
    prev = None
    while head:
        nxt = head.next    # save it before you overwrite
        head.next = prev   # flip the arrow
        prev = head        # shuffle both pointers forward
        head = nxt
    return prev            # prev is the new head
```

**The trap:** forgetting to save `head.next` before overwriting it loses the rest of the list. Say that line out loud as you write it.
</details>

---

### Q-COD-006 · recursion · Easy · [Reported]

Fibonacci using only two variables.

<details>
<summary>Answer</summary>

**Approach in plain words:** you only ever need the last two numbers, so slide a window forward instead of recursing.

**Complexity:** O(n) time, **O(1) space** — versus O(2ⁿ) for naive recursion.

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**They may follow up with:** "What was wrong with the recursive version?" — each call branches into two, so the call tree doubles: O(2ⁿ). Memoisation fixes it to O(n) time but still O(n) space.
</details>

---

### Q-COD-007 · stack · Hard · [Reported]

Largest rectangle in a histogram — given bar heights, find the biggest rectangle that fits inside.

<details>
<summary>Answer</summary>

**Approach in plain words:** for each bar, ask how far left and right it can stretch before hitting a shorter bar. A stack that keeps bars in increasing height order lets you answer that in one pass — when a shorter bar arrives, every taller bar on the stack has found its right edge.

**Complexity:** O(n) time, O(n) space. The brute force is O(n²) — say that first.

```python
def largest_rectangle(heights):
    stack, best = [], 0
    for i, h in enumerate(heights + [0]):   # sentinel flushes the stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best
```

**Be honest if you're stuck.** This is genuinely hard. Explaining the brute force clearly and then reasoning toward the stack idea scores better than silence. *(Reported at WellDev.)*
</details>

---

### Q-COD-008 · file I/O · Easy · [Reported]

Write code that creates a directory and, inside it, a text file containing "Hello World".

<details>
<summary>Answer</summary>

**Approach in plain words:** make the directory (don't fail if it already exists), then open a file inside it for writing.

```python
import os

os.makedirs("demo", exist_ok=True)
with open(os.path.join("demo", "hello.txt"), "w") as f:
    f.write("Hello World")
```

**Why they ask it:** it is deliberately easy. They want to see you type calmly, use a context manager so the file closes itself, and handle the "directory already exists" case without being told. *(Reported at WellDev.)*
</details>

---

## "Explain X" — spoken answers

> All ten are reported at WellDev. Answers are written **as speech** — say them aloud, don't read them silently. Aim for 20–40 seconds each.

---

### Q-VER-001 · SQL · Easy · [Reported]

Explain the execution order of an SQL query.

<details>
<summary>Answer</summary>

**Short answer (say this):** "SQL doesn't run in the order you write it. It starts with FROM to get the tables, then WHERE to drop rows, then GROUP BY to bundle them, then HAVING to drop whole groups, then SELECT to pick the columns, then ORDER BY, then LIMIT. That's why you can't use a SELECT alias inside WHERE — WHERE has already run by then — but you can use it in ORDER BY."

**They may follow up with:** "So what's the difference between WHERE and HAVING?" — WHERE filters rows before grouping, HAVING filters groups after.
</details>

---

### Q-VER-002 · DBMS · Easy · [Reported]

Explain the ACID properties.

<details>
<summary>Answer</summary>

**Short answer (say this):** "Atomicity means all or nothing — a transfer either takes the money out and puts it in, or neither. Consistency means the database never ends up breaking its own rules. Isolation means concurrent transactions don't see each other's half-finished work. And durability means once it's committed, it survives a crash."

**They may follow up with:** "Which one covers the double-booking problem?" — isolation.
</details>

---

### Q-VER-003 · OOP · Easy · [Reported]

What is polymorphism?

<details>
<summary>Answer</summary>

**Short answer (say this):** "It means the same call does the right thing depending on the object behind it. The practical value is that I can write code against a parent type and it keeps working when I add new subclasses — the calling code doesn't change. In my Django work, every model inherits a BaseModel with soft delete, so `soft_delete()` behaves correctly on any of them without me writing it twice."

**They may follow up with:** "Compile-time or run-time?" — overriding is run-time, overloading is compile-time.
</details>

---

### Q-VER-004 · OOP · Easy · [Reported]

What is encapsulation, and why does it matter?

<details>
<summary>Answer</summary>

**Short answer (say this):** "Encapsulation is keeping internal state private and exposing controlled methods to change it. It matters because it protects invariants — if nobody can set a balance directly, the balance can never go negative behind your back. I apply the same idea at the architecture level: my views never touch the ORM, reads go through selectors and writes go through services."
</details>

---

### Q-VER-005 · data structures · Easy · [Reported]

Compare a linked list and an array in terms of performance.

<details>
<summary>Answer</summary>

**Short answer (say this):** "An array is contiguous memory, so getting element n is constant time, but inserting in the middle shifts everything after it. A linked list stores each value with a pointer to the next, so inserting is constant time once you're at the node — but getting to a position is linear, because you have to walk. So arrays win on lookup, linked lists win on frequent insertion and deletion."

**They may follow up with:** "What's a circular linked list?" — the last node points back to the first instead of to null. Used for round-robin scheduling and buffers.
</details>

---

### Q-VER-006 · algorithms · Medium · [Reported]

What is the two-pointer technique?

<details>
<summary>Answer</summary>

**Short answer (say this):** "You keep two indices moving through the data instead of using nested loops — either from both ends moving inward, or both from the start at different speeds. It turns a lot of order-n-squared problems into order n. Moving zeroes to the end of an array is one pointer reading and one writing; finding a pair that sums to a target in a sorted array is one from each end."
</details>

---

### Q-VER-007 · security · Medium · [Reported]

How would you store passwords so that even an administrator cannot read them?

<details>
<summary>Answer</summary>

**Short answer (say this):** "You never store the password — only a one-way hash of it. To check a login you hash the attempt and compare hashes, so even someone with full database access can't reverse it. Each password gets a unique random salt before hashing, which means two identical passwords produce different hashes and rainbow tables are useless. And you use a deliberately slow algorithm built for this — bcrypt or Argon2 — because a fast hash like plain SHA-256 is exactly what makes brute-forcing cheap."
</details>

---

### Q-VER-008 · concurrency · Medium · [Reported]

Two people try to reserve the same ticket at the same moment. How do you handle it?

<details>
<summary>Answer</summary>

**Short answer (say this):** "That's a race condition — both requests read the seat as free before either writes. I'd wrap it in a transaction and take a row-level lock, so the second request waits for the first to finish. And I'd back that with a unique constraint on event and seat in the database, so even if the application logic has a bug, the second insert simply fails. I've built the same shape for credits — reserve on submit so concurrent jobs can't overspend, then finalise and refund on the callback."
</details>

---

### Q-VER-009 · web · Easy · [Reported]

What happens when you browse to a website?

<details>
<summary>Answer</summary>

**Short answer (say this):** "The browser checks its cache, then DNS turns the domain into an IP address. It opens a TCP connection and negotiates TLS for HTTPS. It sends an HTTP GET, which usually hits a reverse proxy like Nginx before the application server. The server responds with HTML and a status code. The browser parses that into a DOM, discovers it needs CSS, JavaScript and images, and fetches those. Then it renders and runs the JavaScript."
</details>

---

### Q-VER-010 · concurrency · Medium · [Reported]

What is threading, and when would you use it?

<details>
<summary>Answer</summary>

**Short answer (say this):** "Threads run inside one process and share the same memory, so they're cheap to start but you need locks to stop them corrupting shared state. In Python specifically, the global interpreter lock means threads don't help with CPU-heavy work — for that you use multiple processes. Threads still help when you're waiting on input and output, like network calls. In practice for background work I reach for a task queue — Celery with Redis — rather than managing threads by hand."
</details>
