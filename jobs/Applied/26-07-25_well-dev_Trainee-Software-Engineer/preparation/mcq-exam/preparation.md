# MCQ exam — everything you need to learn

**Read this top to bottom.** Fifteen topics in study order, matching the eleven sessions in
[`plan.md`](plan.md). Each one takes 10–20 minutes. Nothing here needs to be read twice before the
questions — do the questions instead.

## The 60-second version

WellDev's first stage is a **broad, shallow multiple-choice paper**. Nine subjects, MCQ depth: data
structures and algorithms, sorting, OOP, DBMS and SQL, software-engineering principles, networking,
REST, JavaScript and analytical reasoning. A former WellDev interviewer said publicly that most of
the questions are easy and any fresh graduate should have a basic idea — **what they screen for is
composure across all nine, not depth in one.**

So the goal today is coverage, not mastery. Get to "I recognise this and I know the one-line answer"
on every topic below. That is enough to pass a paper like this.

**Three things to carry into the room:**

1. **Trace, don't guess.** Stack and tree questions are traceable on paper in eight seconds.
2. **90 seconds, then move on.** One stubborn question costs you four easy ones.
3. **Read the word before you answer.** *Time* or *space*? *Best* case or *worst*? That's where the marks leak.

## What's inside

| # | Topic | Session |
|---|---|---|
| 1 | Reading time complexity (Big O) | 1 |
| 2 | Sorting algorithms | 1 |
| 3 | Arrays and linked lists | 2 |
| 4 | Stacks and queues | 2 |
| 5 | Trees and binary search trees | 3 |
| 6 | Graphs, DFS, BFS, MST and greedy | 3 |
| 7 | Recursion | 3 |
| 8 | SQL — the queries they actually ask | 4 |
| 9 | DBMS theory — ACID, normalisation, indexes, NoSQL | 5 |
| 10 | Object-oriented programming | 6 |
| 11 | Software engineering principles | 6 |
| 12 | Networking — HTTP, status codes and subnetting | 7 |
| 13 | REST APIs | 7 |
| 14 | ⚠️ JavaScript fundamentals — **your weakest area** | 8 |
| 15 | Analytical and mathematical reasoning | 9 |

**Not here, on purpose:** operating systems, deep dynamic programming, system design, and their
actual stack (Ruby on Rails, ColdFusion, .NET). Reasoning in [`plan.md`](plan.md).

---

## 1. Reading time complexity (Big O)

### The 60-second version

Big O is a way of saying **how much slower a program gets when the data gets bigger**. You do not calculate it with maths. You count loops. One loop over the data is O(n). A loop inside a loop is O(n²). Cutting the data in half each step is O(log n). That covers almost every MCQ they will ask.

### Why this matters for this job

*"Time complexity"* is named explicitly in the reported MCQ topic list, and round 1 asked for the complexity of recursive Fibonacci. It is the single most-asked idea in the whole test.

### In plain words

**In plain words:** Big O ignores the small stuff and keeps only the part that grows fastest. If a program does `3n + 50` steps, we call it O(n). The 3 and the 50 stop mattering once n is a million.

Read it as a promise about growth, not about seconds.

| Notation | Name | What it looks like in code |
|---|---|---|
| **O(1)** | constant | No loop. Direct access — `arr[5]`, a dictionary lookup |
| **O(log n)** | logarithmic | Halving each step — binary search |
| **O(n)** | linear | One loop over the data |
| **O(n log n)** | linearithmic | Good sorting — merge sort, heap sort |
| **O(n²)** | quadratic | A loop inside a loop — bubble sort |
| **O(2ⁿ)** | exponential | Recursion that branches twice — naive Fibonacci |

### A tiny example

```python
def has_duplicate(items):
    for a in items:            # loop 1
        for b in items:        # loop 2 inside loop 1
            ...
# Two nested loops over the same data → O(n²)
```

Put those two loops **side by side** instead of nested and it becomes O(n) + O(n) = **O(n)**. Nesting multiplies; sequencing adds.

### How they will ask it

- *"What is the time complexity of this code?"* with a snippet.
- *"What is the time complexity of recursive Fibonacci?"* — **O(2ⁿ)**, because each call makes two more calls.
- *"Accessing element 500 of an array vs. the 500th node of a linked list?"* — **O(1) vs O(n)**.
- *"Which sort is O(n log n) in the worst case?"* — merge sort or heap sort (**not** quicksort, whose worst case is O(n²)).

### The trap

Space complexity is a different question. It asks **how much extra memory** you use, not time. A loop that stores nothing extra is O(1) space even if it is O(n) time. Round 1 asked about space complexity specifically — read the word before you answer.

#### Say this out loud

"Big O describes how the running time grows as the input grows. One pass over the data is linear, order n. A nested loop is quadratic, n squared. Halving the problem each step is logarithmic. Naive recursive Fibonacci is order two-to-the-n because every call spawns two more, which is why you memoise it and bring it down to order n."

### Listen instead — search YouTube for

- `Big O notation in 100 seconds` — about 2 minutes, the fastest possible intro
- `Big O notation full course beginners` — about 15 minutes, watch once while doing nothing else

---

## 2. Sorting algorithms

### The 60-second version

You do not need to write these. You need to recognise them by name, state their speed, and say which one is stable. There are three slow ones you should know exist (bubble, selection, insertion) and three fast ones you should know properly (merge, quick, heap).

### Why this matters for this job

"Sorting" appears in the reported MCQ topic list and again in the short-answer list. It is pure recall — the cheapest marks on the paper.

### In plain words

**In plain words:** the slow sorts compare neighbours over and over, O(n²). The fast sorts split the problem in half repeatedly, O(n log n).

| Algorithm | Average | Worst | Stable? | The one-line idea |
|---|---|---|---|---|
| **Bubble** | O(n²) | O(n²) | Yes | Swap neighbours, biggest bubbles to the end |
| **Selection** | O(n²) | O(n²) | No | Find the smallest, put it first, repeat |
| **Insertion** | O(n²) | O(n²) | Yes | Like sorting playing cards in your hand |
| **Merge** | O(n log n) | **O(n log n)** | Yes | Split in half, sort each, merge them |
| **Quick** | O(n log n) | **O(n²)** | No | Pick a pivot, put smaller left and bigger right |
| **Heap** | O(n log n) | **O(n log n)** | No | Build a heap, keep pulling the max off |

**Stable** means two equal items keep their original order relative to each other. It matters when you sort by one field and want the previous sort preserved.

### A tiny example

Quicksort's worst case is the interesting one:

```
Already sorted: [1, 2, 3, 4, 5]
Pivot = first element every time
→ each partition peels off exactly one item
→ n levels instead of log n → O(n²)
```

Fixed by choosing a random pivot or a median-of-three. That fix is a great thing to say aloud.

### How they will ask it

- *"Which sorting algorithm has O(n log n) in the worst case?"* — **merge sort** or **heap sort**. Not quicksort.
- *"Why is quicksort used in practice if merge sort has a better worst case?"* — quicksort sorts **in place** (O(log n) extra memory), merge sort needs O(n) extra space, and quicksort has smaller constant factors so it is faster in reality.
- *"Which sorts are stable?"* — merge, insertion, bubble.
- *"Best case of insertion sort?"* — **O(n)**, on already-sorted data. It is the one slow sort with a good best case.

### The trap

Do not say "quicksort is the fastest." Say **"quicksort is fastest in practice, but its worst case is O(n²) — merge and heap sort guarantee n log n."** The caveat is the mark.

#### Say this out loud

"Merge sort and heap sort are order n log n even in the worst case. Quicksort averages n log n but degrades to n squared on a bad pivot — sorted input with a first-element pivot, for instance — so you randomise the pivot. Quicksort still wins in practice because it sorts in place, while merge sort needs order n extra memory. Merge and insertion sort are stable; quicksort and heap sort are not."

### Listen instead — search YouTube for

- `Sorting algorithms explained comparison` — about 12 minutes
- `Quick sort vs merge sort explained` — about 10 minutes

---

## 3. Arrays and linked lists

### The 60-second version

An **array** is one solid block of memory. You can jump straight to any position, but inserting in the middle means shifting everything. A **linked list** is scattered boxes, each holding a value and the address of the next box. Inserting is cheap, but finding item 500 means walking through 499 boxes first. That trade-off is the whole topic.

### Why this matters for this job

Round 1 reportedly asked three things from this topic: what an array name prints, array indexing vs linked-list access time, and whether binary search works on a sorted linked list. All three are the same idea asked three ways.

### In plain words

**In plain words:** an array is a row of lockers, numbered and side by side. A linked list is a treasure hunt — each clue tells you where the next one is.

| Operation | Array | Linked list |
|---|---|---|
| Get item at position i | **O(1)** — jump straight there | **O(n)** — walk from the start |
| Insert / delete at the front | O(n) — shift everything | **O(1)** — repoint one link |
| Insert / delete in the middle | O(n) | O(1) *once you are already there* |
| Memory | One contiguous block | Scattered, plus extra space per node for the pointer |

### A tiny example

```c
int arr[5] = {10, 20, 30, 40, 50};
printf("%p", arr);   // prints an ADDRESS, not the values
```

In C, **the array name is the address of its first element.** `arr` and `&arr[0]` are the same thing. That is the "base address" question, and the answer is: it prints the memory address where the array starts.

### How they will ask it

- *"Given an array, what will be the base address if we print the array name only?"* — the address of element 0.
- *"Can you do binary search on a sorted linked list?"* — **Technically yes, practically no.** Binary search needs to jump to the middle in O(1). A linked list cannot jump; reaching the middle costs O(n), so you lose the whole benefit.
- *"When would you choose a linked list over an array?"* — when you insert and delete constantly at known positions and rarely look things up by index.
- *"Reverse a linked list"* — three pointers: previous, current, next.

### The trap

Python's `list` is **not** a linked list. It is a dynamic array. So a Python answer of "lists are fast to insert" is wrong for an MCQ written in C or Java terms. Answer in the general computer-science sense, not the Python sense.

#### Say this out loud

"An array is contiguous memory, so indexing is constant time, but inserting in the middle shifts every element after it. A linked list stores each element with a pointer to the next, so inserting is constant time once you're at the node, but reaching a position is linear. And binary search doesn't really work on a linked list, because you can't jump to the middle in constant time."

### Listen instead — search YouTube for

- `Arrays vs linked lists explained simply` — about 8 minutes
- `Linked list data structure full explanation` — about 15 minutes

---

## 4. Stacks and queues

### The 60-second version

A **stack** is last in, first out — like a pile of plates. A **queue** is first in, first out — like a line at a shop. That is genuinely all they are. The questions come from tracing what is left after a sequence of pushes and pops, and from two classic puzzles: build a stack out of queues, and delete the middle of a stack.

### Why this matters for this job

The one WellDev MCQ that is publicly quoted is a stack push/pop trace. Round 1 asked "delete the middle element of a stack without using another data structure" and "build a stack using queues". This topic has the highest hit rate of anything on the list.

### In plain words

**In plain words:** a stack has one opening at the top — you put in and take out from the same end. A queue has two openings — in at the back, out at the front.

| | Stack | Queue |
|---|---|---|
| Order | LIFO — last in, first out | FIFO — first in, first out |
| Add | `push` | `enqueue` |
| Remove | `pop` | `dequeue` |
| Used by | Function calls, undo, DFS, bracket matching | Print jobs, task queues, BFS |

### A tiny example

Push A, B, C, D, E onto an empty stack. Pop twice.

```
Push:  A B C D E   →   top is E
Pop → E
Pop → D
Left in the stack, bottom to top: A B C
```

**Trace it on paper. Every time.** Writing the letters out takes eight seconds and removes all the risk.

### How they will ask it

- *"Items A, B, C, D, E are pushed in that order, then S is popped twice…"* — trace it.
- *"Delete the middle element of a stack without using another data structure."* — use **recursion**. Pop items off one at a time (the call stack holds them for you), delete when you reach the middle, then push them back on the way out. The trick is that recursion is allowed because the call stack is not "another data structure" you declared.
- *"Implement a stack using two queues."* — make either push or pop expensive. On push, add to queue 2, move everything from queue 1 behind it, then swap the names. Now the newest item is at the front, so dequeue behaves like pop.
- *"Which data structure does DFS use? BFS?"* — **DFS uses a stack** (or recursion), **BFS uses a queue.** Memorise this pair; it is asked constantly.

### The trap

"Without using additional data structures" does not mean "without recursion". Recursion is the intended answer. If you say "it's impossible", you have failed the question they were actually asking.

#### Say this out loud

"A stack is last in, first out; a queue is first in, first out. To delete the middle of a stack without a second structure, I'd use recursion — pop elements off, letting the call stack hold them, remove the middle one when I reach it, then push everything back as the recursion unwinds. And DFS uses a stack while BFS uses a queue."

### Listen instead — search YouTube for

- `Stack and queue data structure explained` — about 10 minutes
- `Implement stack using queues explained` — about 8 minutes

---

## 5. Trees and binary search trees

### The 60-second version

A **tree** is data shaped like a family tree — one root at the top, branches below. A **binary tree** gives every node at most two children. A **binary search tree (BST)** adds one rule: everything smaller goes left, everything bigger goes right. That rule is what makes searching fast — you throw away half the tree at every step.

### Why this matters for this job

"Binary trees" is named in the MCQ topic list. Reported questions include post-order traversal and reverse-iterating a BST.

### In plain words

**In plain words:** a BST is a sorted structure you can search by asking "bigger or smaller?" over and over. Each answer discards half of what is left.

Three ways to walk a tree. The name tells you **when you visit the node itself**:

| Traversal | Order | Memory hook |
|---|---|---|
| **Pre-order** | **Node** → left → right | Node comes *pre*, first |
| **In-order** | left → **Node** → right | Node in the middle — **gives sorted output on a BST** |
| **Post-order** | left → right → **Node** | Node comes *post*, last |

### A tiny example

```
        8
      /   \
     3     10
    / \      \
   1   6      14
```

- **In-order:** 1, 3, 6, 8, 10, 14 ← sorted, always, on a BST
- **Pre-order:** 8, 3, 1, 6, 10, 14
- **Post-order:** 1, 6, 3, 14, 10, 8

Searching for 6: start at 8 → 6 is smaller, go left to 3 → 6 is bigger, go right → found. Three steps instead of six.

### How they will ask it

- *"Give the post-order traversal of this tree."* — draw it, then apply left-right-node.
- *"How do you print a BST in descending order?"* — a **reverse in-order** traversal: right → node → left.
- *"What is the time complexity of searching a BST?"* — **O(log n) when balanced, O(n) in the worst case.**
- *"What is the worst case, and why?"* — insert already-sorted data and the tree becomes a straight line, which is just a linked list.

### The trap

O(log n) is **not guaranteed**. It only holds if the tree is balanced. That "it depends on balance" caveat is exactly the kind of thing the interviewer is listening for — say it unprompted.

#### Say this out loud

"A binary search tree keeps smaller values on the left and larger on the right, so searching discards half the tree each step — that's order log n when it's balanced. If you insert sorted data it degenerates into a linked list and search becomes linear, which is why balanced variants like AVL and red-black trees exist. And an in-order traversal of a BST always comes out sorted."

### Listen instead — search YouTube for

- `Binary search tree explained simply` — about 10 minutes
- `Tree traversal inorder preorder postorder` — about 8 minutes

---

## 6. Graphs, DFS, BFS, MST and greedy

### The 60-second version

A **graph** is dots joined by lines — cities and roads, people and friendships. You explore it two ways: **DFS** goes deep down one path before backing up, **BFS** spreads out level by level. A **minimum spanning tree** is the cheapest set of roads that still connects every city. **Greedy** means always taking the best-looking option right now.

### Why this matters for this job

"MST" and "greedy algorithms" are both named in the reported MCQ topics. Round 1 asked a knight-on-a-chessboard question, which is a BFS problem in disguise.

### In plain words

**In plain words:** DFS is one person exploring a maze, following each corridor to its end. BFS is water flooding the maze, reaching everything one step away, then everything two steps away.

| | DFS | BFS |
|---|---|---|
| Uses | A **stack** (or recursion) | A **queue** |
| Goes | Deep first | Wide first |
| Best for | Cycle detection, topological sort, "is there a path?" | **Shortest path in an unweighted graph** |

**Two ways to store a graph:**
- **Adjacency list** — for each node, a list of its neighbours. Good when there are few edges. Space O(V + E).
- **Adjacency matrix** — a grid of true/false. Fast to ask "are these two connected?" but space O(V²).

### A tiny example

Minimum spanning tree — the cheapest wiring that connects everything, with no loops:

- **Kruskal's algorithm** — sort all the edges by cost, keep adding the cheapest one that does not create a cycle.
- **Prim's algorithm** — start at one node, keep adding the cheapest edge that reaches somewhere new.

Both are **greedy**: take the cheapest option available right now, never look back. For MSTs, greedy happens to give the true best answer.

### How they will ask it

- *"Which data structure does BFS use?"* — a **queue**. DFS uses a **stack**.
- *"Shortest number of moves for a knight to reach a square?"* — **BFS.** Each move is one level. The first time you land on the target, you are there by the shortest route.
- *"Name two MST algorithms."* — Kruskal and Prim.
- *"What is a greedy algorithm?"* — one that makes the locally best choice at each step and never reconsiders.
- *"When does greedy fail?"* — when a worse choice now enables a much better one later. Coin change with odd denominations is the standard example.

### The trap

Greedy is not always correct. It is correct for MSTs and for Dijkstra, and wrong for many other problems. If asked "will greedy work here?", the safe honest answer is *"it depends on whether the problem has the greedy-choice property — it does for MST, but not in general."*

#### Say this out loud

"DFS uses a stack and goes deep; BFS uses a queue and goes level by level, which is why BFS gives the shortest path in an unweighted graph — so a knight's-minimum-moves problem is BFS. A minimum spanning tree connects every node at the lowest total cost, and Kruskal and Prim both build one greedily, by always taking the cheapest safe edge."

### Listen instead — search YouTube for

- `BFS and DFS explained simply` — about 10 minutes
- `Minimum spanning tree Kruskal Prim explained` — about 12 minutes

---

## 7. Recursion

### The 60-second version

A recursive function calls itself on a smaller version of the same problem, until the problem is small enough to answer directly. Two parts, always: a **base case** that stops it, and a **recursive case** that shrinks the problem. Miss the base case and it runs forever.

### Why this matters for this job

Round 1 asked for the naming and complexity of a recursive sum function, and the complexity of recursive Fibonacci. The stack middle-deletion puzzle is also solved with recursion.

### In plain words

**In plain words:** recursion is delegation. "I don't know the answer for 5, but if someone tells me the answer for 4, I can finish it." Eventually someone gets a problem so small they just know it.

Every pending call sits on the **call stack**, waiting. That is why deep recursion causes a stack overflow, and why the call stack can be borrowed as free temporary storage.

### A tiny example

```python
def total(n):
    if n == 0:        # base case — stops the recursion
        return 0
    return n + total(n - 1)   # recursive case — smaller problem
```

`total(3)` → `3 + total(2)` → `3 + 2 + total(1)` → `3 + 2 + 1 + total(0)` → 6.
**Time O(n), space O(n)** — because n calls are stacked up waiting.

### How they will ask it

- *"Time complexity of recursive Fibonacci?"* — **O(2ⁿ)**. Each call makes two more, so the call tree doubles at every level.
- *"How do you fix it?"* — **memoisation**: cache each result the first time you compute it. That drops it to **O(n)**. Or use two variables in a loop, which is O(n) time and **O(1) space**.
- *"Fibonacci with two variables"* — a reported question. Keep only the last two numbers and slide forward.
- *"What is the space complexity of a recursive function?"* — O(depth of recursion), because of the call stack. This is the part people forget.

### The trap

Time and space are different answers. Recursive sum is O(n) time **and** O(n) space. The iterative loop version is O(n) time and **O(1)** space. Interviewers ask the space question specifically to see whether you remember the call stack costs memory.

#### Say this out loud

"Recursion needs a base case and a shrinking recursive case. Naive Fibonacci is order two-to-the-n because each call branches into two, and you fix that with memoisation to get order n — or just iterate with two variables, which is order n time and constant space. And recursion isn't free on memory: the space complexity is the depth of the call stack."

### Listen instead — search YouTube for

- `Recursion explained for beginners programming` — about 10 minutes
- `Memoization dynamic programming Fibonacci explained` — about 12 minutes

---

## 8. SQL — the queries they actually ask

### The 60-second version

Four things cover almost every SQL question WellDev has asked: the **order the clauses run in**, the **joins**, **finding duplicates**, and **DELETE vs TRUNCATE vs DROP**. Learn those four and you can answer the reported questions cold.

### Why this matters for this job

Reported in round 1 and round 2: clause execution order, duplicate rows, products sharing the same price, DELETE/TRUNCATE/DROP, joins. This is the highest-density SQL topic list you could ask for.

### In plain words

**Clause execution order is not the order you write them.** You write `SELECT` first, but the database runs it almost last:

```
FROM  →  WHERE  →  GROUP BY  →  HAVING  →  SELECT  →  ORDER BY  →  LIMIT
```

**In plain words:** get the tables, throw away rows you don't want, bundle them into groups, throw away groups you don't want, then pick which columns to show, then sort.

That order explains a real puzzle: **you cannot use a `SELECT` alias in a `WHERE` clause**, because `WHERE` runs before `SELECT` exists. But you *can* use it in `ORDER BY`, which runs after.

**The joins:**

| Join | Keeps |
|---|---|
| `INNER JOIN` | Only rows matching in both tables |
| `LEFT JOIN` | All of the left table, plus matches; NULLs where none |
| `RIGHT JOIN` | All of the right table, plus matches |
| `FULL OUTER JOIN` | Everything from both sides |

### A tiny example

**Find duplicate rows** — group by the column, then keep groups with more than one member:

```sql
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**Products sharing the same price** — same shape:

```sql
SELECT price, COUNT(*)
FROM products
GROUP BY price
HAVING COUNT(*) > 1;
```

**Second-highest salary:**

```sql
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### How they will ask it

- *"What is the execution order of an SQL query?"* — recite the seven steps.
- *"WHERE vs HAVING?"* — `WHERE` filters **rows before grouping**; `HAVING` filters **groups after**. You cannot use an aggregate like `COUNT(*)` in `WHERE`.
- *"Find duplicates"* — `GROUP BY ... HAVING COUNT(*) > 1`.
- *"DELETE vs TRUNCATE vs DROP?"* — see below. This is asked verbatim.

| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Removes | Chosen rows | All rows | The whole table |
| `WHERE` allowed | Yes | No | No |
| Table still exists | Yes | Yes | **No** |
| Rollback-able | Yes | Usually no | Usually no |
| Speed | Slow (row by row, logged) | Fast | Fast |

### The trap

People say "TRUNCATE is just a fast DELETE." Add the difference that matters: **TRUNCATE cannot be filtered, does not fire row triggers, and normally resets the auto-increment counter.**

#### Say this out loud

"SQL runs FROM, then WHERE, then GROUP BY, then HAVING, then SELECT, then ORDER BY — which is why you can't reference a SELECT alias in WHERE but you can in ORDER BY. WHERE filters rows before grouping and HAVING filters groups after. To find duplicates I group by the column and keep groups with a count above one. And DELETE removes chosen rows and can be rolled back, TRUNCATE clears the whole table fast without a WHERE, and DROP removes the table itself."

### Listen instead — search YouTube for

- `SQL joins explained visually` — about 10 minutes
- `SQL query execution order explained` — about 8 minutes

---

## 9. DBMS theory — ACID, normalisation, indexes, NoSQL

### The 60-second version

Four recall answers cover this: **ACID** (what a transaction guarantees), **normalisation** (removing duplicated data), **indexes** (why lookups are fast) and **SQL vs NoSQL** (structure vs flexibility). All four are asked as short definitions, not as deep design questions.

### Why this matters for this job

ACID, normalisation, triggers, SQL vs NoSQL and ER diagrams are all in the reported question lists. "DBMS" is named in the MCQ topics.

### In plain words

**ACID** — the four promises a database makes about a transaction:

| Letter | Means | In plain words |
|---|---|---|
| **A** — Atomicity | All or nothing | Money leaves one account *and* arrives, or neither happens |
| **C** — Consistency | Rules stay true | No transaction can leave the data breaking its own constraints |
| **I** — Isolation | Transactions don't see each other's half-done work | Two people paying at once don't corrupt each other |
| **D** — Durability | Once committed, it survives | Power cut after "success" doesn't lose it |

**Normalisation** — organise tables so each fact is stored **once**.

- **1NF** — no repeating groups; every cell holds one value.
- **2NF** — 1NF, plus every non-key column depends on the *whole* key.
- **3NF** — 2NF, plus no column depends on another non-key column.

The point: if a customer's address is in one table only, changing it can never leave two different answers. That is what "fix redundancy by normalising" means.

**Indexes** — a sorted lookup structure (usually a B-tree) so the database finds rows without scanning every one. Reads get much faster; **writes get slower**, because every insert must update the index too.

### A tiny example

```sql
CREATE TRIGGER log_price_change
AFTER UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION record_history();
```

A **trigger** is code the database runs automatically when something happens. **Cascading** is the related idea: `ON DELETE CASCADE` means deleting a parent row automatically deletes its children.

### How they will ask it

- *"What are the ACID properties?"* — recite all four with one line each.
- *"There's redundant data in this table. What do you do?"* — normalise it; split the repeated facts into their own table and reference them by key.
- *"SQL vs NoSQL?"* — SQL has a fixed schema, relations and strong ACID guarantees; NoSQL is schema-flexible, scales horizontally more easily, and often trades consistency for availability. Use SQL when relationships and correctness matter, NoSQL for huge volumes of loosely-structured data.
- *"How do you detect changes in a database?"* — triggers, an audit/history table, a `updated_at` timestamp column, or the database's change-data-capture log.
- *"Why not index every column?"* — writes slow down and the index consumes storage.

### The trap

Normalisation is not always the goal. Real systems **denormalise deliberately** for read speed. Saying *"I'd normalise to 3NF, then denormalise selectively where read performance demands it"* is a much stronger answer than "normalise everything."

#### Say this out loud

"ACID is atomicity, consistency, isolation and durability — all-or-nothing, rules stay valid, transactions don't see each other's partial work, and committed data survives a crash. Normalisation removes duplicated data so each fact lives in one place, which is how you fix redundancy. Indexes speed reads and slow writes. And SQL gives you a fixed schema with strong guarantees, while NoSQL trades some of that for flexibility and horizontal scale."

### Listen instead — search YouTube for

- `ACID properties in DBMS explained` — about 8 minutes
- `Database normalization 1NF 2NF 3NF explained` — about 12 minutes

---

## 10. Object-oriented programming

### The 60-second version

OOP organises code around **objects** — things that hold data and the actions that work on that data. Four ideas carry the whole topic: encapsulation, inheritance, polymorphism and abstraction. Learn them as four one-line answers plus one example each, and you have covered most of what they ask.

### Why this matters for this job

OOP is in the MCQ topic list, was asked in round 1 ("OOP fundamentals", "spot the access-modifier violation"), and the JD itself demands *"a firm grasp of object-oriented analysis and design."* You already do this daily in Django — you just need the vocabulary.

### In plain words

| Pillar | In plain words | Your own example |
|---|---|---|
| **Encapsulation** | Keep the data private, expose controlled methods | A service layer that owns writes; views never touch the ORM directly |
| **Inheritance** | A child class reuses a parent's behaviour | Your `BaseModel` giving every model soft delete and timestamps |
| **Polymorphism** | One name, different behaviour depending on the object | `soft_delete()` behaving correctly on any model that inherits it |
| **Abstraction** | Hide the messy detail, show a simple interface | A payment provider enum where Stripe and Tap sit behind one shape |

**Access modifiers** control who can touch what:

| Modifier | Who can access it |
|---|---|
| `public` | Anyone |
| `private` | Only inside that class |
| `protected` | That class and its children |
| *(default / package-private in Java)* | Anything in the same package |

### A tiny example

```java
class Account {
    private double balance;              // nobody outside can touch it

    public void deposit(double amount) { // controlled way in
        if (amount > 0) balance += amount;
    }
}

Account a = new Account();
a.balance = -500;   // ❌ COMPILE ERROR — balance is private
```

That last line is the "access-modifier violation" they show you. The fix is to go through `deposit()`, which validates.

### How they will ask it

- *"What are the four pillars of OOP?"* — pure recall.
- *"Spot the error in this code"* — usually touching a `private` field from outside, or overriding a method with weaker access.
- *"Abstract class vs interface?"* — an abstract class can hold state and partly-written methods, and a class can extend only one. An interface is a pure contract, and a class can implement many.
- *"Overloading vs overriding?"* — **overloading** is same name, different parameters, decided at compile time. **Overriding** is a child replacing a parent's method, decided at run time.
- *"Composition vs inheritance?"* — prefer composition; inheritance couples the child to the parent's internals.

### The trap

Polymorphism is the one people fumble. Do not define it as "many forms" and stop. Say **what it buys you**: you can write code against the parent type and it works for every child, so adding a new child needs no change to the calling code.

#### Say this out loud

"The four pillars are encapsulation, inheritance, polymorphism and abstraction. Encapsulation is hiding state behind controlled methods — in my Django work that's a service layer that owns every write, so views never touch the ORM directly. Inheritance I use through a BaseModel that gives every model soft delete and timestamps. Polymorphism means I can call the same method on any subclass and get the right behaviour, so new models need no change to the calling code."

### Listen instead — search YouTube for

- `Four pillars of OOP explained with examples` — about 12 minutes
- `Abstract class vs interface explained` — about 8 minutes

---

## 11. Software engineering principles

### The 60-second version

Recall questions about how software gets built: the **SDLC** stages, **Agile vs Waterfall**, **SOLID**, **testing types**, and **version control**. You already do all of this — including formal requirement analysis, DFDs and ERDs — so this is about naming what you already practise.

### Why this matters for this job

"SWE principles" is in the MCQ topic list. ER diagrams and dependency injection appear in the short-answer list. And the JD's first responsibility is *"build a foundation in software development life cycle (SDLC)"* — your SafeTag documentation work is direct evidence here.

### In plain words

**SDLC — the stages:**

Requirements → Design → Implementation → Testing → Deployment → Maintenance.

**Waterfall vs Agile:**

| | Waterfall | Agile |
|---|---|---|
| Shape | One pass, stage after stage | Short repeated cycles (sprints) |
| Change | Expensive once you've moved on | Expected and welcomed |
| Delivery | Everything at the end | Working software every sprint |
| Fits | Fixed, well-understood requirements | Ambiguous, evolving requirements |

**SOLID — five design principles:**

| Letter | Principle | In plain words |
|---|---|---|
| **S** | Single responsibility | One class, one job, one reason to change |
| **O** | Open/closed | Open to extend, closed to modify |
| **L** | Liskov substitution | A child must work anywhere its parent works |
| **I** | Interface segregation | Many small interfaces beat one fat one |
| **D** | Dependency inversion | Depend on abstractions, not concrete classes |

**Dependency injection** is the practical face of that last one: a class is *given* what it needs instead of building it itself. That makes it testable, because you can hand it a fake.

**Testing levels:** unit (one function) → integration (parts together) → system (the whole thing) → acceptance (does it meet the requirement).

### A tiny example

**An ER diagram** shows entities, their attributes, and the relationships between them, with cardinality — one-to-one, one-to-many, many-to-many. You have drawn these formally: use-case, activity, swimlane, ERD and data-flow diagrams to four levels on the SafeTag system design document.

That is not a "revision topic" for you. It is a **story to tell**.

### How they will ask it

- *"What are the SDLC phases?"* — the six above, in order.
- *"Agile vs Waterfall?"* — iterative and change-tolerant vs sequential and plan-heavy.
- *"What is dependency injection?"* — passing a dependency in rather than constructing it inside, so it can be swapped or mocked.
- *"Difference between unit and integration testing?"* — one piece in isolation vs pieces working together.
- *"What is an ER diagram?"* — a model of entities, attributes and relationships used to design a schema before writing it.

### The trap

Do not recite SOLID as five letters with no meaning. If you can give **one real example** — "single responsibility is why my views never touch the ORM; reads go through selectors and writes through services" — you have answered better than someone who memorised the acronym.

#### Say this out loud

"The SDLC runs requirements, design, implementation, testing, deployment, maintenance. Waterfall does that once in sequence; Agile repeats it in short sprints so requirements can change. In my own work I enforce single responsibility with a strict layering — models, then selectors for reads, then services for writes, and views never touch the ORM directly. And I've produced the formal side too: use case, activity, swimlane, ERD and data-flow diagrams as a client deliverable."

### Listen instead — search YouTube for

- `SDLC phases explained` — about 8 minutes
- `SOLID principles explained with examples` — about 15 minutes

---

## 12. Networking — HTTP, status codes and subnetting

### The 60-second version

Three things get asked: **HTTP status codes** (learn the families, not all 60), **what happens when you type a URL into a browser** (a story you recite), and **subnetting** (a bit of binary arithmetic). Status codes are the cheapest marks on the paper.

### Why this matters for this job

Networking is in the MCQ topic list, and HTTP status codes and subnetting are both named specifically. "What happens when you browse a website" was asked in round 2.

### In plain words

**Status codes come in families.** Learn the first digit and a handful of specifics.

| Family | Means | Know these |
|---|---|---|
| **1xx** | Information | rarely asked |
| **2xx** | Success | **200** OK · **201** Created · **204** No Content |
| **3xx** | Redirect | **301** moved permanently · **302** found (temporary) · **304** not modified |
| **4xx** | **You** made a mistake | **400** bad request · **401** not authenticated · **403** authenticated but not allowed · **404** not found · **409** conflict · **429** too many requests |
| **5xx** | **The server** made a mistake | **500** internal error · **502** bad gateway · **503** unavailable |

**401 vs 403 is the classic trick.** 401 = *I don't know who you are.* 403 = *I know who you are, and you still can't.*

**What happens when you type a URL** — the story, in order:

1. Browser checks its cache, then **DNS** turns the domain into an IP address.
2. **TCP** connection opens to that IP (the three-way handshake), and **TLS** negotiates HTTPS.
3. The browser sends an **HTTP GET** request.
4. The server (often behind a reverse proxy like Nginx or Caddy) handles it and returns HTML plus a status code.
5. The browser **parses the HTML**, builds the DOM, and requests CSS, JS and images.
6. It renders the page, then runs the JavaScript.

### A tiny example

**Subnetting.** An IP has a network part and a host part. The `/24` tells you how many bits are the network.

```
192.168.1.0/24
→ 24 network bits, 8 host bits
→ 2^8 = 256 addresses
→ minus network address and broadcast address
→ 254 usable hosts
```

**The formula to memorise:** usable hosts = **2^(32 − prefix) − 2**.

| Prefix | Total | Usable |
|---|---|---|
| /24 | 256 | 254 |
| /25 | 128 | 126 |
| /26 | 64 | 62 |
| /27 | 32 | 30 |
| /28 | 16 | 14 |
| /30 | 4 | 2 |

### How they will ask it

- *"What status code for a successful POST that created a record?"* — **201**.
- *"User is logged in but lacks permission?"* — **403**.
- *"How many usable hosts in a /26?"* — 2⁶ − 2 = **62**.
- *"TCP vs UDP?"* — TCP is reliable, ordered, connection-based (web, email). UDP is fast, no guarantees (video calls, games, DNS).
- *"What happens when you browse a website?"* — tell the six-step story above.

### The trap

Do not say "404 means the server is broken." 404 is a **client-side** error — you asked for something that isn't there. Server errors are 5xx. Mixing up the 4xx/5xx boundary is a common and very visible mistake.

#### Say this out loud

"Status codes group by first digit — two hundreds are success, three hundreds redirect, four hundreds mean the client got it wrong, five hundreds mean the server did. The one people confuse is 401 versus 403: 401 means I don't know who you are, 403 means I know and you still aren't allowed. For subnetting, usable hosts is two to the power of the host bits, minus two for the network and broadcast addresses — so a slash twenty-six gives sixty-two."

### Listen instead — search YouTube for

- `HTTP status codes explained` — about 8 minutes
- `Subnetting made easy for beginners` — about 15 minutes
- `What happens when you type a URL into a browser` — about 10 minutes

---

## 13. REST APIs

### The 60-second version

**This is your home ground.** REST is a set of conventions for building web APIs: use the right HTTP verb, name your URLs after nouns, and return the right status code. You build these for a living. Read this file once to lock the vocabulary, then move on — spend your time elsewhere.

### Why this matters for this job

"REST API knowledge" is in the MCQ topic list. Round 2 asked about a health-check API, what GET does, how many APIs a ticket system needs, and pagination. The JD names *"REST, gRPC, event-driven architectures."*

### In plain words

**In plain words:** REST treats everything as a **resource** with an address, and uses the HTTP verb to say what you want done to it.

| Verb | Does | Safe? | Idempotent? |
|---|---|---|---|
| **GET** | Read | Yes — changes nothing | Yes |
| **POST** | Create | No | **No** — twice makes two |
| **PUT** | Replace the whole thing | No | **Yes** — twice = same result |
| **PATCH** | Update part of it | No | Usually yes |
| **DELETE** | Remove | No | **Yes** — deleting twice leaves it deleted |

**Idempotent** means doing it twice has the same effect as doing it once. That is why a failed POST is dangerous to retry and a failed PUT is safe — and it is exactly why you put a unique `stripe_event_id` on webhook tables to make replays harmless.

**URL naming:** nouns, plural, no verbs.

```
✅ GET    /api/v1/users/42/orders
❌ GET    /api/v1/getUserOrders?id=42
```

### A tiny example

**Pagination** — never return a million rows.

- **Offset pagination:** `?page=3&limit=50`. Simple; gets slow and can skip or repeat rows if data changes underneath.
- **Cursor pagination:** `?after=<id>&limit=50`. Stable and fast on big tables.

**Health check:** `GET /health` returning 200 plus the status of each dependency — database, cache, queue. You have built exactly this: a dashboard covering database, Redis, SMTP, Celery worker and Celery Beat.

### How they will ask it

- *"What does GET do, and how would you write a health-check API call?"* — GET reads without side effects; `GET /health` returning 200 and a JSON body of dependency states.
- *"How many APIs would a ticket booking system need?"* — do not guess a number. **List the resources, then the operations**: list events, get one event, list seats, hold a seat, confirm a booking, cancel, list my bookings, pay. Roughly eight endpoints across four resources — and say *why*, because the reasoning is the answer.
- *"How do you show a very large dataset?"* — pagination, plus filtering and sorting server-side.
- *"REST vs gRPC?"* — REST is HTTP + JSON, human-readable, universal. gRPC uses binary protobuf over HTTP/2, faster for service-to-service. **Be honest: you have not used gRPC.** Say you work with REST and event-driven patterns and would pick gRPC up as needed.

### The trap

Do not claim gRPC. It is on the JD but there is no gRPC anywhere in your history, and the CV that got you here deliberately left it out. The honest line lands better than a bluff that collapses under one follow-up.

#### Say this out loud

"REST models everything as resources addressed by URL, with the HTTP verb saying what to do — GET reads, POST creates, PUT replaces, PATCH updates part, DELETE removes. GET and DELETE are idempotent, POST isn't, which is why webhook handlers need an idempotency key. For a booking system I'd start from the resources — events, seats, bookings, payments — and derive the endpoints from the operations each one needs, rather than guessing a count."

### Listen instead — search YouTube for

- `REST API concepts and examples` — about 8 minutes
- `Idempotency in APIs explained` — about 6 minutes

---

## 14. JavaScript fundamentals — for a Python developer

### The 60-second version

**This is your biggest gap, and it is worth real time.** JavaScript is named first in the reported MCQ topic list, and you are a Python engineer. You do not need to write JavaScript. You need to answer six or seven MCQs about how it behaves oddly. Those oddities are the whole exam.

### Why this matters for this job

*"JavaScript fundamentals"* leads the reported MCQ topic list. "JavaScript events" appears in the short-answer list. Your CV is Python, Django and FastAPI — the paper will not care.

### In plain words

**`==` vs `===` — the most-asked JavaScript question in existence.**

- `==` converts types before comparing. `"5" == 5` is **true**.
- `===` compares value **and** type. `"5" === 5` is **false**.
- Always use `===`. Always say so.

**`var`, `let`, `const`:**

| Keyword | Scope | Reassignable? | Hoisted as |
|---|---|---|---|
| `var` | whole function | yes | `undefined` |
| `let` | the `{ }` block | yes | error if used early |
| `const` | the block | **no** | error if used early |

`const` stops *reassignment*, not *mutation* — you can still `push` into a `const` array.

**Hoisting:** declarations are moved to the top of their scope before the code runs. `var x` exists (as `undefined`) before its line; `let` and `const` exist but throw if touched early.

**`null` vs `undefined`:** `undefined` means never given a value. `null` means deliberately set to nothing.

**The event loop:** JavaScript runs one thing at a time. Slow work (network, timers) is handed off, and its callback is queued to run once the main work finishes. That is how single-threaded code stays responsive — and it is the same idea as `async`/`await` in FastAPI, which you already know.

**Events:** things that happen in the browser — click, submit, keypress. **Bubbling** means an event fires on the element, then its parent, then upward. `event.stopPropagation()` halts that.

### A tiny example

```javascript
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);

// prints: 1, 4, 3, 2
```

Why: synchronous lines first (1, 4), then **promises** (microtasks, 3), then **timers** (macrotasks, 2). Even with a 0 ms delay, `setTimeout` goes last.

**A closure** is a function that remembers the variables around it after the outer function has finished:

```javascript
function counter() {
  let count = 0;
  return () => ++count;    // still remembers `count`
}
```

### How they will ask it

- *"What does `"5" == 5` return?"* — `true`. And `===` gives `false`.
- *"Difference between `let` and `var`?"* — block scope vs function scope, plus hoisting behaviour.
- *"What is a closure?"* — a function plus the variables it captured from where it was defined.
- *"Predict the output"* with `setTimeout` — apply the event-loop order above.
- *"What is event bubbling?"* — the event travels from the target up through its ancestors.

### The trap

Do not answer JavaScript questions with Python reasoning. `==` in Python does **not** convert `"5"` to `5` — in JavaScript it does. When you see a JS question, deliberately switch languages in your head before answering.

#### Say this out loud

"Double equals coerces types before comparing, so string five equals number five is true; triple equals compares type as well, so it's false — and you always use triple equals. `var` is function-scoped and hoisted as undefined, while `let` and `const` are block-scoped. A closure is a function that keeps access to the variables it was defined alongside. And JavaScript is single-threaded with an event loop, so promises resolve before timers even at zero delay."

### Listen instead — search YouTube for

- `JavaScript == vs === explained` — about 5 minutes
- `JavaScript event loop explained` — about 12 minutes
- `JavaScript closures explained simply` — about 8 minutes

---

## 15. Analytical and mathematical reasoning

### The 60-second version

Part of the MCQ is not about programming at all. It is GRE-style reasoning — percentages, ratios, work rate, speed, series and logic puzzles. These are **fast marks if you recognise the shape**, and a total time sink if you try to reason from scratch. Learn the five shapes below.

### Why this matters for this job

"Analytical reasoning" is in the reported MCQ topic list, and round 1 included a GRE-style maths question. Puzzle questions (river crossing, coin problems) are reported too. The two-eggs problem came up in round 2.

### In plain words

**The five shapes that cover most of it:**

**1. Percentage change.** Up 20% then down 20% does **not** return to the start. 100 → 120 → 96. Always multiply, never add percentages.

**2. Work rate.** Convert to work-per-hour, then add.
> A does a job in 6 hours, B in 3. Together?
> A = 1/6 per hour, B = 1/3 per hour. Sum = 1/2. So **2 hours**.

**3. Average speed.** Not the average of the speeds. Total distance ÷ total time.
> 60 km/h out, 30 km/h back → 40 km/h, not 45.

**4. Ratios.** Turn the ratio into parts. 3:5 over 40 items = 8 parts of 5 → 15 and 25.

**5. Series.** Look for the difference, then the difference of the differences. 2, 6, 12, 20 → gaps 4, 6, 8 → next gap 10 → **30**.

### A tiny example

**Two eggs, 100 floors** — find the highest floor an egg survives, with only two eggs, minimising worst-case drops.

The idea: the first egg drops in **shrinking steps** so that every path costs the same. Start at floor 14, then +13, +12, +11… If the first egg breaks at step *k*, the second egg walks up the *k−1* floors below. Answer: **14 drops** in the worst case.

You are not expected to derive that under pressure. You **are** expected to say the reasoning: *"I'd balance the two search phases so the worst case is equal everywhere, which gives a decreasing step size rather than a fixed one."*

### How they will ask it

- Straight arithmetic under time pressure — percentages, ratios, averages.
- A number series, asking for the next term.
- A logic puzzle — river crossing, weighing coins, prisoners and hats.
- **The two-eggs / 100-floors problem**, which is reported at WellDev specifically.

### The trap

Time. These questions are designed so that one stubborn puzzle eats the minutes you needed for eight easy DSA questions. **Set a limit: 90 seconds, then guess and move on.** A guessed answer costs you nothing unless there is negative marking — and you can come back if time allows.

#### Say this out loud

"For the two-eggs problem I'd use a decreasing step size — start around floor fourteen, then thirteen, then twelve — so that however early the first egg breaks, the linear search below it costs the same total. That balances the worst case at fourteen drops instead of the twenty-five you'd get from fixed ten-floor jumps."

### Listen instead — search YouTube for

- `Aptitude test time and work problems shortcut` — about 15 minutes
- `Two egg problem 100 floors explained` — about 8 minutes
