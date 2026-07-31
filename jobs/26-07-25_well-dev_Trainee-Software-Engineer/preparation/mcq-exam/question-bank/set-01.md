# Question bank — set 01

**78 questions** for the onsite MCQ test. Built 31 July 2026.

Answers are collapsed inside `<details>` blocks — attempt each question and commit to an answer
*before* you open one. Manifest, coverage gaps and extension history: [`INDEX.md`](INDEX.md).

**Six subjects below**, in the same order as [`../preparation.md`](../preparation.md):
DSA (22) · DBMS & SQL (14) · OOP & software engineering (12) · Networking & REST (12) ·
JavaScript (10) · Analytical reasoning (8).

---

## Data structures & algorithms

> **Tagging note.** Almost every WellDev question in the public record was asked *in an interview*, not on the MCQ paper. Where I have turned one into multiple-choice form, it is tagged `[Pattern]` even though the underlying topic is reported — the topic is real, the four options are mine. Only `Q-DSA-001` is a genuine reported MCQ.

Answers are collapsed. Attempt first, then open.

---

### Q-DSA-001 · stacks · Easy · [Reported]

Suppose that items A, B, C, D and E are pushed in that order onto an initially empty stack S. S is then popped four times, and each popped item is pushed onto a second, initially empty stack T. Two items are then popped from T. What is at the top of T now?

A. A · B. B · C. C · D. D

<details>
<summary>Answer</summary>

**Short answer (say this):** D.

**Why:** trace it in two lines.
- S after pushing: `A B C D E` — E on top. Popping four times yields **E, D, C, B**.
- Pushed onto T in that order, T reads bottom-to-top: `E D C B`. Popping twice removes **B**, then **C**. The top of T is now **D**.

**The lesson, not the letter:** never answer a stack trace from intuition. Write the letters down, mark the top, and cross them off. Eight seconds of writing removes all the risk. *(Source: the opening question of a leaked WellDev MCQ paper — [Course Hero listing](https://www.coursehero.com/file/74748681/Well-DEV-QUESpdf/); the full paper is paywalled, so the option list here is mine.)*

**They may follow up with:** "What real-world thing uses a stack?" — function calls, undo, browser back, DFS.
</details>

---

### Q-DSA-002 · complexity · Easy · [Pattern]

What is the time complexity of the naive recursive Fibonacci function?

A. O(n) · B. O(n log n) · C. O(2ⁿ) · D. O(n²)

<details>
<summary>Answer</summary>

**Short answer (say this):** O(2ⁿ).

**Why:** each call makes two more calls, so the call tree roughly doubles at every level. Memoising the results drops it to O(n); an iterative two-variable version is O(n) time and O(1) space.

**They may follow up with:** "How would you improve it?" — memoisation, or two variables in a loop.
</details>

---

### Q-DSA-003 · complexity · Easy · [Pattern]

Accessing the 500th element of an array vs the 500th node of a singly linked list:

A. O(1) and O(1) · B. O(1) and O(n) · C. O(n) and O(1) · D. O(n) and O(n)

<details>
<summary>Answer</summary>

**Short answer (say this):** O(1) for the array, O(n) for the linked list.

**Why:** an array is contiguous memory, so the address is computed directly. A linked list has to walk from the head, following 499 pointers.

**They may follow up with:** "Then why ever use a linked list?" — constant-time insert and delete once you're at the node, and no need for one contiguous block.
</details>

---

### Q-DSA-004 · linked lists · Medium · [Pattern]

Can binary search be performed efficiently on a **sorted singly linked list**?

A. Yes, O(log n) · B. No — reaching the middle costs O(n), so the benefit is lost · C. Yes, but only if it is circular · D. Only if it is doubly linked

<details>
<summary>Answer</summary>

**Short answer (say this):** No — you can't jump to the middle in constant time, so it degrades to O(n).

**Why:** binary search depends on random access. A linked list only offers sequential access. Even a doubly linked list doesn't fix it.

**They may follow up with:** "What structure gives you sorted data *and* fast search?" — a balanced BST, or a sorted array.
</details>

---

### Q-DSA-005 · arrays · Medium · [Pattern]

In C, given `int arr[5];` what does printing `arr` alone produce?

A. The contents of the array · B. The number of elements · C. The base address of the array · D. A compile error

<details>
<summary>Answer</summary>

**Short answer (say this):** The base address — the memory address of the first element.

**Why:** an array name decays to a pointer to its first element. `arr` and `&arr[0]` are the same value.

**They may follow up with:** "What does `sizeof(arr)` give?" — the total bytes (5 × 4 = 20 on a typical build), which is one of the few places the array does *not* decay to a pointer.
</details>

---

### Q-DSA-006 · traversal · Easy · [Pattern]

Which traversal of a **binary search tree** produces the values in ascending sorted order?

A. Pre-order · B. In-order · C. Post-order · D. Level-order

<details>
<summary>Answer</summary>

**Short answer (say this):** In-order — left, node, right.

**Why:** the BST rule puts everything smaller on the left, so visiting left before the node before right emits values in increasing order.

**They may follow up with:** "How would you print it in descending order?" — reverse in-order: right, node, left.
</details>

---

### Q-DSA-007 · traversal · Medium · [Pattern]

For the tree with root 8, left child 3 (children 1 and 6), right child 10 (right child 14), what is the **post-order** traversal?

A. 8 3 1 6 10 14 · B. 1 3 6 8 10 14 · C. 1 6 3 14 10 8 · D. 1 6 14 3 10 8

<details>
<summary>Answer</summary>

**Short answer (say this):** 1, 6, 3, 14, 10, 8.

**Why:** post-order is left → right → node. Finish the entire left subtree (1, 6, then 3), then the right subtree (14, then 10), then the root last.

**They may follow up with:** "Where is post-order actually used?" — deleting a tree (free children before the parent), and evaluating expression trees.
</details>

---

### Q-DSA-008 · sorting · Easy · [Pattern]

Which sorting algorithm has O(n log n) time complexity in the **worst** case?

A. Quicksort · B. Bubble sort · C. Merge sort · D. Insertion sort

<details>
<summary>Answer</summary>

**Short answer (say this):** Merge sort. Heap sort also qualifies.

**Why:** quicksort averages O(n log n) but degrades to O(n²) on a bad pivot. Bubble and insertion are O(n²).

**They may follow up with:** "Then why is quicksort preferred in practice?" — it sorts in place (O(log n) extra memory vs merge sort's O(n)) and has smaller constant factors.
</details>

---

### Q-DSA-009 · sorting · Medium · [Pattern]

Which of these sorting algorithms is **not stable**?

A. Merge sort · B. Insertion sort · C. Bubble sort · D. Quicksort

<details>
<summary>Answer</summary>

**Short answer (say this):** Quicksort.

**Why:** stable means two equal elements keep their original relative order. Quicksort's partitioning swaps distant elements, which can reorder equal ones. Heap sort is also unstable.

**They may follow up with:** "When does stability matter?" — when you sort by one field after already sorting by another and want the first order preserved.
</details>

---

### Q-DSA-010 · sorting · Easy · [Pattern]

What is the **best-case** time complexity of insertion sort?

A. O(1) · B. O(n) · C. O(n log n) · D. O(n²)

<details>
<summary>Answer</summary>

**Short answer (say this):** O(n), on already-sorted input.

**Why:** each element is compared once to its predecessor and stays put. It is the one quadratic sort with a genuinely good best case, which is why it is used for small or nearly-sorted arrays inside hybrid sorts.
</details>

---

### Q-DSA-011 · graphs · Easy · [Pattern]

BFS uses which data structure, and DFS uses which?

A. Queue, stack · B. Stack, queue · C. Both use a queue · D. Both use a stack

<details>
<summary>Answer</summary>

**Short answer (say this):** BFS uses a queue; DFS uses a stack (or recursion).

**Why:** a queue is first-in-first-out, so BFS finishes an entire level before starting the next. A stack is last-in-first-out, so DFS keeps diving down the newest path.

**They may follow up with:** "Which finds the shortest path in an unweighted graph?" — BFS.
</details>

---

### Q-DSA-012 · graphs · Medium · [Pattern]

You need the minimum number of moves for a knight to reach a target square on a chessboard. Which approach?

A. DFS · B. BFS · C. Greedy nearest-square · D. Binary search

<details>
<summary>Answer</summary>

**Short answer (say this):** BFS.

**Why:** every knight move costs the same, so the board is an unweighted graph. BFS explores in rings of increasing distance, so the first time you land on the target you arrived by the fewest moves. DFS would find *a* path, not the shortest.

**They may follow up with:** "What if moves had different costs?" — Dijkstra's algorithm. *(This question is reported at WellDev in interview form.)*
</details>

---

### Q-DSA-013 · graphs · Easy · [Pattern]

Which pair of algorithms both build a minimum spanning tree?

A. Dijkstra and Bellman-Ford · B. Kruskal and Prim · C. Floyd-Warshall and Prim · D. Kruskal and Dijkstra

<details>
<summary>Answer</summary>

**Short answer (say this):** Kruskal and Prim.

**Why:** both are greedy. Kruskal sorts all edges and adds the cheapest that doesn't create a cycle; Prim grows one tree outward, always taking the cheapest edge to a new node. Dijkstra solves shortest path, not MST.
</details>

---

### Q-DSA-014 · greedy · Medium · [Pattern]

Which statement about greedy algorithms is true?

A. They always produce the optimal solution · B. They reconsider earlier choices when a better option appears · C. They take the locally best option at each step and never backtrack · D. They are always faster than dynamic programming

<details>
<summary>Answer</summary>

**Short answer (say this):** They take the locally best option and never backtrack.

**Why:** that is the definition. Greedy gives the true optimum only when the problem has the greedy-choice property — true for MST and Dijkstra, false for many others, such as coin change with awkward denominations.
</details>

---

### Q-DSA-015 · graphs · Medium · [Pattern]

For a graph with many nodes but very few edges, which representation uses less memory?

A. Adjacency matrix · B. Adjacency list · C. Identical · D. Depends on whether it is directed

<details>
<summary>Answer</summary>

**Short answer (say this):** Adjacency list — O(V + E) versus the matrix's O(V²).

**Why:** a matrix reserves a cell for every possible pair whether an edge exists or not. For a sparse graph almost all cells are empty. The matrix wins only when you constantly ask "are these two directly connected?", which it answers in O(1).
</details>

---

### Q-DSA-016 · stacks · Medium · [Pattern]

How do you delete the middle element of a stack **without using another data structure**?

A. It is impossible · B. Use recursion — the call stack holds the elements · C. Sort the stack first · D. Convert it to an array

<details>
<summary>Answer</summary>

**Short answer (say this):** Recursion — pop items off, let the call stack hold them, remove the middle one, push the rest back as the recursion unwinds.

**Why:** the constraint bans *declaring* a second structure. The call stack is not one you declared, so recursion is the intended solution.

**They may follow up with:** "What's the space complexity?" — O(n), because the call stack still holds n frames. Be honest about that. *(Reported at WellDev in interview form.)*
</details>

---

### Q-DSA-017 · queues · Medium · [Pattern]

To implement a stack using two queues, which operation becomes expensive?

A. Neither — both stay O(1) · B. One of push or pop becomes O(n) · C. Both become O(n) · D. Only peek

<details>
<summary>Answer</summary>

**Short answer (say this):** One of them — you choose which. Making push O(n) keeps pop at O(1), or vice versa.

**Why:** a queue only releases its oldest element, but a stack needs its newest. Somewhere you must reverse the order, and that costs a pass over n elements.

**They may follow up with:** "Show the push-heavy version." — enqueue the new item into the empty queue, move every element from the other queue in behind it, then swap the two queue references.
</details>

---

### Q-DSA-018 · complexity · Medium · [Pattern]

What is the **space** complexity of a recursive function that sums 1 to n?

A. O(1) · B. O(log n) · C. O(n) · D. O(n²)

<details>
<summary>Answer</summary>

**Short answer (say this):** O(n) — n call frames stack up before any of them return.

**Why:** recursion is not free. Each pending call holds its own frame. The iterative loop version does the same work in O(1) space.

**They may follow up with:** "What is tail-call optimisation?" — a compiler transform that reuses the frame when the recursive call is the last operation. **CPython does not do it**, so deep recursion in Python still overflows.
</details>

---

### Q-DSA-019 · hashing · Easy · [Pattern]

Average-case time to look up a key in a hash table:

A. O(1) · B. O(log n) · C. O(n) · D. O(n log n)

<details>
<summary>Answer</summary>

**Short answer (say this):** O(1) average, O(n) worst case.

**Why:** the hash function jumps straight to a bucket. The worst case is every key colliding into one bucket, degrading to a linear scan of a chain.

**They may follow up with:** "How are collisions handled?" — chaining (a list per bucket) or open addressing (probe for the next free slot).
</details>

---

### Q-DSA-020 · two pointers · Medium · [Pattern]

To move all zeroes in an array to the end while keeping the order of the non-zero elements, the most efficient approach is:

A. Sort the array · B. Two pointers in a single pass, O(n) time and O(1) space · C. Build a new array, O(n) space · D. Nested loops, O(n²)

<details>
<summary>Answer</summary>

**Short answer (say this):** Two pointers — one write index, one read index, single pass, constant extra space.

**Why:** walk the array with the read pointer; every time you find a non-zero, write it at the write index and advance it. At the end, fill the remainder with zeroes. O(n) time, O(1) space, order preserved. *(Reported at WellDev.)*
</details>

---

### Q-DSA-021 · arrays · Easy · [Pattern]

The fastest way to find the second-largest element in an unsorted array of n elements:

A. Sort it, O(n log n) · B. One pass tracking the two largest, O(n) · C. Two nested loops, O(n²) · D. Binary search

<details>
<summary>Answer</summary>

**Short answer (say this):** One pass, tracking the largest and second-largest as you go — O(n).

**Why:** sorting does far more work than the question needs. Watch the edge cases: duplicates of the maximum, and arrays with fewer than two distinct values.
</details>

---

### Q-DSA-022 · linked lists · Medium · [Pattern]

How do you detect a cycle in a linked list in O(1) extra space?

A. Store every visited node in a set · B. Two pointers, one moving twice as fast as the other · C. Sort the list · D. It cannot be done in O(1) space

<details>
<summary>Answer</summary>

**Short answer (say this):** Floyd's cycle detection — a slow pointer moving one step and a fast pointer moving two. If they ever meet, there is a cycle.

**Why:** a set works but costs O(n) memory. If there is a loop, the fast pointer laps the slow one and they collide. If it reaches the end, there is no loop.
</details>

---

## DBMS & SQL

> Topics here are reported at WellDev; the multiple-choice framing and options are mine, so they are tagged `[Pattern]`.

---

### Q-DB-001 · SQL · Medium · [Pattern]

What is the correct **execution** order of an SQL query?

A. SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
B. FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
C. FROM → SELECT → WHERE → GROUP BY → HAVING → ORDER BY
D. WHERE → FROM → GROUP BY → SELECT → HAVING → ORDER BY

<details>
<summary>Answer</summary>

**Short answer (say this):** FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT.

**Why:** you *write* SELECT first but the engine runs it almost last. That explains a real consequence: a column alias defined in SELECT cannot be used in WHERE (WHERE runs first) but can be used in ORDER BY (which runs after).

**They may follow up with:** "So why does `WHERE COUNT(*) > 1` fail?" — aggregates don't exist until GROUP BY has run. Use HAVING. *(Reported at WellDev.)*
</details>

---

### Q-DB-002 · SQL · Easy · [Pattern]

Which query finds duplicate email addresses in a `users` table?

A. `SELECT email FROM users WHERE COUNT(email) > 1`
B. `SELECT email FROM users GROUP BY email HAVING COUNT(*) > 1`
C. `SELECT DISTINCT email FROM users`
D. `SELECT email FROM users ORDER BY email`

<details>
<summary>Answer</summary>

**Short answer (say this):** B — group by the column, then filter the groups with HAVING.

**Why:** A fails because WHERE cannot see aggregates. C removes duplicates rather than finding them.

**They may follow up with:** "Now find products sharing the same price" — identical shape: `GROUP BY price HAVING COUNT(*) > 1`. *(Both reported at WellDev.)*
</details>

---

### Q-DB-003 · SQL · Easy · [Pattern]

Which statement about DELETE, TRUNCATE and DROP is correct?

A. All three remove the table structure
B. TRUNCATE accepts a WHERE clause
C. DELETE removes chosen rows and can be rolled back; TRUNCATE clears all rows quickly; DROP removes the table itself
D. DROP only removes the rows, keeping the schema

<details>
<summary>Answer</summary>

**Short answer (say this):** C.

**Why:** DELETE is row-by-row, filterable, logged and rollback-able. TRUNCATE clears everything fast, takes no WHERE, normally resets the auto-increment counter and doesn't fire row triggers. DROP deletes the table definition as well as the data. *(Reported at WellDev.)*
</details>

---

### Q-DB-004 · DBMS · Easy · [Pattern]

The "I" in ACID stands for isolation. What does it guarantee?

A. Each transaction runs on its own server
B. Concurrent transactions do not see each other's uncommitted, partial work
C. Data is written to disk immediately
D. Every transaction completes fully or not at all

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** D is atomicity, C is durability. Isolation is specifically about concurrency — one transaction must not observe another's half-finished state.

**They may follow up with:** "Name the isolation levels." — read uncommitted, read committed, repeatable read, serializable, in increasing strictness and decreasing concurrency. *(ACID is reported at WellDev.)*
</details>

---

### Q-DB-005 · normalisation · Medium · [Pattern]

A table stores a customer's full address on every one of their order rows. What is the problem and the fix?

A. Nothing wrong — it is faster
B. Redundancy — normalise by moving the address into a customers table referenced by a foreign key
C. Add an index on the address column
D. Convert the table to NoSQL

<details>
<summary>Answer</summary>

**Short answer (say this):** B — that is an update anomaly waiting to happen.

**Why:** if the customer moves, you must update every order row, and any missed row leaves two contradictory answers. Storing the fact once and referencing it makes that impossible.

**They may follow up with:** "Is normalisation always right?" — no. Real systems denormalise deliberately for read performance. Say you'd normalise to 3NF then denormalise selectively where reads demand it. *(Reported at WellDev.)*
</details>

---

### Q-DB-006 · normalisation · Medium · [Pattern]

Which condition defines third normal form (3NF)?

A. Every cell holds a single value
B. Every non-key column depends on the whole primary key
C. No non-key column depends on another non-key column
D. Every table has a primary key

<details>
<summary>Answer</summary>

**Short answer (say this):** C — no transitive dependencies.

**Why:** A is 1NF, B is 2NF. 3NF adds that non-key columns must depend on the key alone, not on each other. The mnemonic: *the key, the whole key, and nothing but the key.*
</details>

---

### Q-DB-007 · indexes · Medium · [Pattern]

What is the main cost of adding an index to a column?

A. Reads become slower · B. Writes become slower and storage grows · C. The table can no longer be joined · D. There is no cost

<details>
<summary>Answer</summary>

**Short answer (say this):** Writes slow down and the index consumes disk.

**Why:** every INSERT, UPDATE and DELETE must maintain the index as well as the table. That is why you index the columns you filter and join on, not every column.

**They may follow up with:** "What structure is an index usually?" — a B-tree, which is why range queries and ORDER BY benefit too.
</details>

---

### Q-DB-008 · joins · Easy · [Pattern]

A LEFT JOIN between `customers` and `orders` returns:

A. Only customers who have orders
B. All customers, with NULLs where they have no orders
C. All orders, with NULLs for missing customers
D. Every combination of both tables

<details>
<summary>Answer</summary>

**Short answer (say this):** B — every row from the left table, matched where possible.

**Why:** INNER JOIN would be A. D describes a CROSS JOIN.

**They may follow up with:** "How do you find customers with *no* orders?" — LEFT JOIN then `WHERE orders.id IS NULL`. That is a very common follow-up.
</details>

---

### Q-DB-009 · SQL vs NoSQL · Easy · [Pattern]

Which is the clearest reason to choose a relational database over a document store?

A. It is always faster
B. The data has strong relationships and you need transactional guarantees across them
C. It scales horizontally more easily
D. It requires no schema design

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** relational databases give you joins, constraints and ACID transactions across related tables. NoSQL trades some of that for schema flexibility and easier horizontal scaling. Neither is "better" — it depends on the shape of the data. *(Reported at WellDev.)*
</details>

---

### Q-DB-010 · triggers · Medium · [Pattern]

What is a database trigger?

A. A scheduled job that runs nightly
B. Code the database runs automatically in response to an INSERT, UPDATE or DELETE
C. An index that fires on read
D. A constraint that rejects invalid data

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** triggers run inside the database, not the application. Common uses are audit history and derived values. The related idea is cascading: `ON DELETE CASCADE` removes child rows when a parent is deleted.

**They may follow up with:** "How else would you detect database changes?" — an audit table, `updated_at` timestamps, or change-data-capture from the write-ahead log. *(Reported at WellDev.)*
</details>

---

### Q-DB-011 · SQL · Medium · [Pattern]

Which query returns the second-highest salary?

A. `SELECT salary FROM employees ORDER BY salary DESC LIMIT 1`
B. `SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)`
C. `SELECT MIN(salary) FROM employees`
D. `SELECT salary FROM employees WHERE salary = 2`

<details>
<summary>Answer</summary>

**Short answer (say this):** B — the largest value below the largest value.

**Why:** it handles duplicate top salaries correctly, which `ORDER BY ... LIMIT 1 OFFSET 1` does not. If two people both earn the maximum, the offset approach returns the maximum again.
</details>

---

### Q-DB-012 · DBMS · Easy · [Pattern]

What does an ER diagram model?

A. The sequence of function calls
B. Entities, their attributes, and the relationships and cardinality between them
C. Network topology
D. The user interface flow

<details>
<summary>Answer</summary>

**Short answer (say this):** B — it's the blueprint you draw before creating tables.

**Why:** cardinality (one-to-one, one-to-many, many-to-many) is the part that turns into foreign keys and join tables.

**They may follow up with:** "Have you produced one?" — yes, formally: ERDs, DFDs to four levels, use-case, activity and swimlane diagrams as a client deliverable. *(Reported at WellDev.)*
</details>

---

### Q-DB-013 · transactions · Medium · [Pattern]

Two users try to book the same seat at the same moment. What is the most reliable safeguard?

A. Check availability before writing
B. A unique constraint in the database, plus a row-level lock inside a transaction
C. Make the front end disable the button
D. Retry the request

<details>
<summary>Answer</summary>

**Short answer (say this):** B — application logic plus a database constraint as the final guarantee.

**Why:** A is exactly the bug — the check and the write aren't atomic, so both requests pass the check. Only the database can arbitrate reliably. *(Reported at WellDev in interview form; see [`technical-interview/preparation.md`](../../technical-interview/preparation.md).)*
</details>

---

### Q-DB-014 · pagination · Easy · [Pattern]

An endpoint must return two million rows to a client. The correct approach is:

A. Return them all in one response
B. Paginate — return a page at a time with filtering and sorting done server-side
C. Send them as a CSV attachment
D. Cache the full response

<details>
<summary>Answer</summary>

**Short answer (say this):** B — pagination, server-side.

**Why:** offset pagination (`?page=3&limit=50`) is simple but drifts if rows change underneath. Cursor pagination (`?after=<id>`) is stable and stays fast on large tables. *(Reported at WellDev.)*
</details>

---

## OOP & software engineering

> Topics reported at WellDev; multiple-choice framing and options are mine → `[Pattern]`.

---

### Q-OOP-001 · pillars · Easy · [Pattern]

Which are the four pillars of OOP?

A. Abstraction, encapsulation, inheritance, polymorphism
B. Classes, objects, methods, attributes
C. Coupling, cohesion, abstraction, modularity
D. Inheritance, recursion, iteration, composition

<details>
<summary>Answer</summary>

**Short answer (say this):** Abstraction, encapsulation, inheritance, polymorphism.

**Why:** B lists the building blocks, not the principles. Pure recall — never lose this mark. *(Reported at WellDev.)*
</details>

---

### Q-OOP-002 · access modifiers · Medium · [Pattern]

```java
class Account {
    private double balance;
    public void deposit(double a) { if (a > 0) balance += a; }
}
// elsewhere:
Account acc = new Account();
acc.balance = -500;
```
What happens?

A. Runs fine, balance becomes -500 · B. Compile error — `balance` is private · C. Runtime exception · D. Balance stays 0 silently

<details>
<summary>Answer</summary>

**Short answer (say this):** Compile error — you cannot touch a private field from outside the class.

**Why:** this is encapsulation doing its job. The public `deposit()` method is the controlled way in, and it validates the amount. *(Reported at WellDev as "identify the access modifier violation".)*

**They may follow up with:** "What are the access levels?" — public, private, protected, and Java's package-private default.
</details>

---

### Q-OOP-003 · polymorphism · Medium · [Pattern]

What does polymorphism buy you in practice?

A. Faster execution
B. Code written against a parent type works for every subclass, so adding a subclass needs no change to the caller
C. Less memory usage
D. Automatic error handling

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** "many forms" is the textbook phrase, but the *value* is that calling code stays untouched when you add a new type. That is the answer interviewers are actually listening for. *(Reported at WellDev.)*
</details>

---

### Q-OOP-004 · overloading · Easy · [Pattern]

Overloading vs overriding:

A. Both are resolved at run time
B. Overloading = same name, different parameters, resolved at compile time; overriding = subclass replaces a parent method, resolved at run time
C. Overloading is inheritance; overriding is composition
D. They are two words for the same thing

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** overloading is compile-time (static) polymorphism; overriding is run-time (dynamic) polymorphism. Remember which is which by the word *ride* — a child rides over the parent, at run time.
</details>

---

### Q-OOP-005 · abstraction · Medium · [Pattern]

Abstract class vs interface — which is true?

A. An abstract class can hold state and partly-implemented methods; a class can implement many interfaces but extend only one abstract class
B. Interfaces can hold instance fields; abstract classes cannot
C. They are interchangeable
D. Abstract classes cannot have constructors

<details>
<summary>Answer</summary>

**Short answer (say this):** A.

**Why:** the practical rule — use an abstract class for shared state and shared partial behaviour; use an interface for a pure capability contract that unrelated classes can all satisfy. *(Reported at WellDev.)*
</details>

---

### Q-OOP-006 · encapsulation · Easy · [Pattern]

Which best describes encapsulation?

A. Hiding internal state and exposing controlled methods to change it
B. One class inheriting from another
C. Breaking a program into functions
D. Compiling code into a single binary

<details>
<summary>Answer</summary>

**Short answer (say this):** A.

**Why:** the point is invariants. If nobody can set `balance` directly, `balance` can never go negative behind your back. *(Reported at WellDev.)*
</details>

---

### Q-OOP-007 · SOLID · Medium · [Pattern]

The "S" in SOLID means:

A. A class should have one reason to change
B. Subclasses must be substitutable for their parents
C. Depend on abstractions, not concretions
D. Classes should be open for extension, closed for modification

<details>
<summary>Answer</summary>

**Short answer (say this):** A — single responsibility.

**Why:** B is Liskov, C is dependency inversion, D is open/closed. Have one real example ready: *"views never touch the ORM — reads go through selectors, writes through services."*
</details>

---

### Q-OOP-008 · DI · Medium · [Pattern]

What is dependency injection?

A. Importing a module at the top of a file
B. Passing a class its dependencies from outside rather than constructing them internally
C. Installing packages with pip
D. Injecting SQL into a query

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** it is the practical face of the "D" in SOLID. The payoff is testability — you can hand the class a fake in a unit test instead of a real database or payment gateway. *(Reported at WellDev.)*
</details>

---

### Q-OOP-009 · SDLC · Easy · [Pattern]

The standard SDLC phases, in order:

A. Design → Requirements → Testing → Implementation → Deployment
B. Requirements → Design → Implementation → Testing → Deployment → Maintenance
C. Implementation → Testing → Requirements → Deployment
D. Planning → Coding → Shipping

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** the JD's very first responsibility is building a foundation in the SDLC, so this is worth knowing crisply. You have delivered the formal artefacts of the early phases as client deliverables.
</details>

---

### Q-OOP-010 · methodology · Easy · [Pattern]

The main difference between Agile and Waterfall:

A. Agile has no documentation
B. Agile works in short iterations and expects requirements to change; Waterfall runs the phases once in sequence
C. Waterfall is always faster
D. Agile has no testing phase

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** A is a common misreading — Agile values working software *over* comprehensive documentation, which is not the same as none.
</details>

---

### Q-OOP-011 · testing · Easy · [Pattern]

Unit testing vs integration testing:

A. Unit tests the whole system; integration tests one function
B. Unit tests one piece in isolation; integration tests several pieces working together
C. They are the same
D. Integration testing is done by the customer

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** D describes acceptance testing. The usual ladder is unit → integration → system → acceptance.

**They may follow up with:** "How do you test in isolation?" — mock or inject the dependencies, which loops back to dependency injection.
</details>

---

### Q-OOP-012 · composition · Medium · [Pattern]

Why is composition often preferred over inheritance?

A. It runs faster
B. Inheritance couples a child to the parent's internals, so a parent change can break every subclass
C. Inheritance is deprecated
D. Composition uses less memory

<details>
<summary>Answer</summary>

**Short answer (say this):** B — inheritance is the tightest coupling in object-oriented design.

**Why:** a deep hierarchy makes every parent change risky, and a subclass inherits things it may not want. Composition assembles behaviour from parts you can swap. "Favour composition over inheritance" is a rule you already apply — your `ai_rules.md` states it explicitly.
</details>

---

## Networking & REST APIs

> Networking (including HTTP status codes and subnetting) and REST are named in the reported MCQ topic list. Options are mine → `[Pattern]`.

---

### Q-NET-001 · status codes · Easy · [Pattern]

A POST request successfully creates a new resource. Correct status code?

A. 200 · B. 201 · C. 204 · D. 302

<details>
<summary>Answer</summary>

**Short answer (say this):** 201 Created.

**Why:** 200 is generic success, 204 means success with no body (typical for DELETE). A well-behaved 201 also returns a `Location` header pointing at the new resource.
</details>

---

### Q-NET-002 · status codes · Medium · [Pattern]

A user is logged in but tries to open an admin-only page. Correct code?

A. 400 · B. 401 · C. 403 · D. 404

<details>
<summary>Answer</summary>

**Short answer (say this):** 403 Forbidden.

**Why:** the classic trap. **401 = I don't know who you are** (not authenticated). **403 = I know who you are and you still can't** (authenticated, not authorised). *(HTTP status codes are reported in the WellDev MCQ.)*
</details>

---

### Q-NET-003 · status codes · Easy · [Pattern]

Which family means the **server** failed?

A. 2xx · B. 3xx · C. 4xx · D. 5xx

<details>
<summary>Answer</summary>

**Short answer (say this):** 5xx.

**Why:** 4xx is the client's fault — bad request, unauthorised, not found. 5xx is the server's — 500 internal error, 502 bad gateway, 503 unavailable. Mixing these up is very visible.
</details>

---

### Q-NET-004 · subnetting · Medium · [Pattern]

How many **usable** host addresses in a /26 network?

A. 64 · B. 62 · C. 32 · D. 30

<details>
<summary>Answer</summary>

**Short answer (say this):** 62.

**Why:** 32 − 26 = 6 host bits → 2⁶ = 64 addresses → minus the network address and the broadcast address → **62**. The formula is 2^(32−prefix) − 2. *(Subnetting is reported in the WellDev MCQ.)*
</details>

---

### Q-NET-005 · subnetting · Medium · [Pattern]

How many usable hosts in a /28?

A. 16 · B. 14 · C. 12 · D. 30

<details>
<summary>Answer</summary>

**Short answer (say this):** 14.

**Why:** 4 host bits → 16 total → minus 2 → 14. Memorise the short ladder: /24→254, /25→126, /26→62, /27→30, /28→14, /30→2.
</details>

---

### Q-NET-006 · protocols · Easy · [Pattern]

TCP vs UDP:

A. TCP is faster but unreliable; UDP is slow but reliable
B. TCP is connection-oriented, ordered and reliable; UDP is connectionless, faster, with no delivery guarantee
C. They are identical apart from the port range
D. UDP is only used for email

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** TCP handshakes, acknowledges and retransmits — used by HTTP and email. UDP just fires packets — used by video calls, games and DNS, where a late packet is worse than a lost one.
</details>

---

### Q-NET-007 · web · Medium · [Pattern]

What happens first when you type a URL and press enter?

A. The TCP connection opens
B. DNS resolves the domain to an IP address (after a cache check)
C. The HTML is parsed
D. TLS negotiates

<details>
<summary>Answer</summary>

**Short answer (say this):** DNS resolution — you cannot connect to a name, only to an address.

**Why:** the full order is cache → DNS → TCP handshake → TLS → HTTP request → server response → HTML parsed → sub-resources fetched → render → JavaScript runs. *(Reported at WellDev as "what happens when you browse a website".)*
</details>

---

### Q-NET-008 · REST · Easy · [Pattern]

Which HTTP methods are idempotent?

A. Only GET · B. GET, PUT and DELETE · C. Only POST · D. All of them

<details>
<summary>Answer</summary>

**Short answer (say this):** GET, PUT and DELETE. POST is not.

**Why:** idempotent means calling it twice has the same effect as once. Two POSTs create two records — which is exactly why webhook handlers need an idempotency key. You do this in production with a unique `stripe_event_id` on the webhook table.
</details>

---

### Q-NET-009 · REST · Easy · [Pattern]

Which URL best follows REST conventions?

A. `GET /api/getUserOrders?userId=42`
B. `GET /api/v1/users/42/orders`
C. `POST /api/fetchOrders`
D. `GET /api/orders/get/42`

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** REST addresses resources with nouns and lets the HTTP verb express the action. Putting a verb in the path duplicates what the method already says.
</details>

---

### Q-NET-010 · REST · Medium · [Pattern]

What should a health-check endpoint do?

A. Return the full database contents
B. Return 200 with the status of each critical dependency — database, cache, queue
C. Restart the server
D. Require admin authentication and return a log file

<details>
<summary>Answer</summary>

**Short answer (say this):** B — a cheap, fast GET that reports whether each dependency is reachable.

**Why:** load balancers and monitors poll it constantly, so it must be quick and side-effect free. You have built exactly this: a dashboard covering database, Redis, SMTP, Celery worker and Celery Beat. *(Reported at WellDev.)*
</details>

---

### Q-NET-011 · REST · Medium · [Pattern]

Which best describes what GET should do?

A. Read a resource without changing server state
B. Create a resource
C. Replace a resource entirely
D. Anything, as long as the URL is correct

<details>
<summary>Answer</summary>

**Short answer (say this):** A — GET is *safe*: it reads and changes nothing.

**Why:** "safe" means no side effects; "idempotent" means repeatable without extra effect. GET is both. A GET that mutates data breaks caching and pre-fetching, and is a genuine bug. *(Reported at WellDev.)*
</details>

---

### Q-NET-012 · caching · Medium · [Pattern]

Which is the standard in-memory store for caching expensive query results?

A. PostgreSQL · B. Redis · C. S3 · D. Nginx

<details>
<summary>Answer</summary>

**Short answer (say this):** Redis.

**Why:** it holds key-value data in RAM, so lookups are sub-millisecond. The usual pattern is cache-aside with a TTL: check Redis, on a miss read the database and write the result back. The hard part is invalidation on change. *(Reported at WellDev as "cache to RAM".)*
</details>

---

## JavaScript fundamentals

> **Your weakest area against this paper, and it leads the reported topic list.** Spend real time here. Options are mine → `[Pattern]`.

---

### Q-JS-001 · equality · Easy · [Pattern]

What does `"5" == 5` return, and what does `"5" === 5` return?

A. true, true · B. true, false · C. false, false · D. false, true

<details>
<summary>Answer</summary>

**Short answer (say this):** true, then false.

**Why:** `==` coerces types before comparing, so the string becomes a number. `===` compares value *and* type, so a string is never equal to a number. Always use `===`.

**They may follow up with:** "`null == undefined`?" — **true** with `==`, **false** with `===`. That pair is a favourite.
</details>

---

### Q-JS-002 · scope · Easy · [Pattern]

Difference between `var` and `let`:

A. None
B. `var` is function-scoped and hoisted as `undefined`; `let` is block-scoped and errors if used before its declaration
C. `let` is function-scoped, `var` is block-scoped
D. `var` cannot be reassigned

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** `var` leaks out of `if` and `for` blocks to the whole function. `let` and `const` stay inside the braces. The gap before a `let` declaration is called the temporal dead zone.
</details>

---

### Q-JS-003 · const · Medium · [Pattern]

```javascript
const arr = [1, 2];
arr.push(3);
```
What happens?

A. Error — `arr` is constant · B. Works; `arr` is now `[1,2,3]` · C. Silently ignored · D. `arr` becomes `undefined`

<details>
<summary>Answer</summary>

**Short answer (say this):** It works.

**Why:** `const` prevents **reassignment** of the binding, not **mutation** of the object it points at. `arr = [4]` would throw; `arr.push(3)` would not.
</details>

---

### Q-JS-004 · event loop · Hard · [Pattern]

```javascript
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);
```
Output order?

A. 1 2 3 4 · B. 1 4 2 3 · C. 1 4 3 2 · D. 1 3 4 2

<details>
<summary>Answer</summary>

**Short answer (say this):** 1, 4, 3, 2.

**Why:** synchronous code first (1 and 4). Then the **microtask** queue — promises — gives 3. Then the **macrotask** queue — timers — gives 2. Even a 0 ms `setTimeout` waits for the microtasks.

**They may follow up with:** "Why is JavaScript single-threaded but not blocking?" — slow work is handed off and its callback queued, which is the same idea as `await` in FastAPI.
</details>

---

### Q-JS-005 · closures · Medium · [Pattern]

What is a closure?

A. A function that closes a file
B. A function that keeps access to the variables of the scope where it was defined, even after that scope has returned
C. A loop that terminates
D. A private class method

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** it is how JavaScript does private state — a counter function that remembers `count` between calls without exposing it.
</details>

---

### Q-JS-006 · types · Easy · [Pattern]

`null` vs `undefined`:

A. Identical
B. `undefined` means no value was ever assigned; `null` means deliberately set to nothing
C. `null` is a syntax error
D. `undefined` only appears in loops

<details>
<summary>Answer</summary>

**Short answer (say this):** B.

**Why:** an unassigned variable or a missing object property gives `undefined`. `null` is a value a programmer chose. Oddity worth knowing: `typeof null` returns `"object"` — a long-standing bug in the language.
</details>

---

### Q-JS-007 · events · Medium · [Pattern]

What is event bubbling?

A. Events fire on the target, then on each ancestor upward
B. Events fire on the outermost element first
C. Events fire twice
D. Events queue until the page loads

<details>
<summary>Answer</summary>

**Short answer (say this):** A — the event travels up from the target through its parents.

**Why:** the downward phase is *capturing*; the upward phase is *bubbling*. `event.stopPropagation()` halts it. Bubbling is what makes event delegation possible — one listener on a parent handling clicks on many children. *(JavaScript events are reported at WellDev.)*
</details>

---

### Q-JS-008 · hoisting · Medium · [Pattern]

```javascript
console.log(x);
var x = 5;
```
Output?

A. 5 · B. `undefined` · C. ReferenceError · D. null

<details>
<summary>Answer</summary>

**Short answer (say this):** `undefined`.

**Why:** the *declaration* is hoisted to the top of the function, but the *assignment* stays where it was. So `x` exists but has no value yet. With `let` instead of `var`, the same code throws a ReferenceError.
</details>

---

### Q-JS-009 · arrays · Easy · [Pattern]

What does `[1,2,3].map(x => x * 2)` return?

A. `[1,2,3]` · B. `[2,4,6]` · C. `6` · D. `undefined`

<details>
<summary>Answer</summary>

**Short answer (say this):** `[2,4,6]` — a **new** array; the original is unchanged.

**Why:** `map` transforms, `filter` selects, `reduce` collapses to a single value. All three return new values rather than mutating. Same mental model as a Python list comprehension.
</details>

---

### Q-JS-010 · async · Medium · [Pattern]

What does an `async` function always return?

A. The raw value · B. A Promise · C. `undefined` · D. A callback

<details>
<summary>Answer</summary>

**Short answer (say this):** A Promise — even if you return a plain number.

**Why:** `await` unwraps a promise; `async` wraps the return value in one. It is the same relationship as `async def` and `await` in Python, which you already use in FastAPI.
</details>

---

## Analytical & mathematical reasoning

> "Analytical reasoning" is named in the reported MCQ topics, and a GRE-style maths question was asked in round 1. Do these **with a timer** — 90 seconds each, then move on.

---

### Q-APT-001 · percentages · Easy · [Pattern]

A price rises by 20%, then falls by 20%. Compared with the original, the final price is:

A. The same · B. 4% lower · C. 4% higher · D. 2% lower

<details>
<summary>Answer</summary>

**Short answer (say this):** 4% lower.

**Why:** 100 → 120 → 96. The 20% fall is taken from the *larger* number. **Never add or subtract percentages — multiply.** 1.2 × 0.8 = 0.96.
</details>

---

### Q-APT-002 · work rate · Medium · [Pattern]

A finishes a job in 6 hours, B in 3 hours. Working together, how long?

A. 4.5 hours · B. 3 hours · C. 2 hours · D. 1.5 hours

<details>
<summary>Answer</summary>

**Short answer (say this):** 2 hours.

**Why:** convert to work per hour and add. A = 1/6, B = 1/3 = 2/6. Together 3/6 = 1/2 of the job per hour → 2 hours. Never average the times.
</details>

---

### Q-APT-003 · average speed · Medium · [Pattern]

You drive to a town at 60 km/h and return along the same road at 30 km/h. Average speed for the whole trip?

A. 45 km/h · B. 40 km/h · C. 50 km/h · D. 36 km/h

<details>
<summary>Answer</summary>

**Short answer (say this):** 40 km/h.

**Why:** average speed is total distance ÷ total time, not the average of the two speeds. Take 60 km each way: 1 hour out, 2 hours back, 120 km in 3 hours = 40. The slower leg takes longer, so it weighs more.
</details>

---

### Q-APT-004 · series · Easy · [Pattern]

What comes next: 2, 6, 12, 20, 30, __?

A. 40 · B. 42 · C. 36 · D. 44

<details>
<summary>Answer</summary>

**Short answer (say this):** 42.

**Why:** the gaps are 4, 6, 8, 10 — so the next gap is 12. 30 + 12 = 42. (It is also n × (n+1): 1×2, 2×3, 3×4…)

**Method:** for any series, write the differences underneath. If they aren't obvious, take the differences of the differences.
</details>

---

### Q-APT-005 · ratios · Easy · [Pattern]

40 items are split between two teams in the ratio 3:5. How many does the larger team get?

A. 15 · B. 20 · C. 25 · D. 30

<details>
<summary>Answer</summary>

**Short answer (say this):** 25.

**Why:** 3 + 5 = 8 parts; 40 ÷ 8 = 5 per part. The larger team gets 5 × 5 = 25, the smaller 3 × 5 = 15. Always find the value of one part first.
</details>

---

### Q-APT-006 · puzzle · Hard · [Reported]

You have two eggs and a 100-storey building. Find the highest floor from which an egg can be dropped without breaking, minimising the number of drops in the worst case.

<details>
<summary>Answer</summary>

**Short answer (say this):** 14 drops in the worst case, using a decreasing step size — first drop at floor 14, then +13, then +12, and so on.

**Why:** with a fixed 10-floor step the worst case is 10 + 9 = 19. The fix is to balance the two phases: each time the first egg survives, the remaining linear search shrinks by one, so the step should shrink by one too. Solve n(n+1)/2 ≥ 100 → n = 14.

**What matters more than the number:** say the *reasoning* — "I'd equalise the worst case across all outcomes, which means a decreasing step size rather than a fixed one." That is what they are testing. *(Reported at WellDev.)*
</details>

---

### Q-APT-007 · puzzle · Medium · [Pattern]

A man must carry a wolf, a goat and a cabbage across a river. The boat holds him plus one item. The wolf eats the goat if left alone with it; the goat eats the cabbage. How?

<details>
<summary>Answer</summary>

**Short answer (say this):** Take the goat over, come back empty. Take the wolf over, **bring the goat back**. Leave the goat, take the cabbage over, return empty, then take the goat.

**Why:** the insight is that a trip can go *backwards*. Most people never consider carrying something back, which is exactly the assumption the puzzle is testing. *(Reported in the WellDev-adjacent aptitude sets.)*
</details>

---

### Q-APT-008 · logic · Medium · [Pattern]

You have 8 identical-looking balls; one is heavier. Using a balance scale, what is the minimum number of weighings needed to find it?

A. 1 · B. 2 · C. 3 · D. 4

<details>
<summary>Answer</summary>

**Short answer (say this):** 2.

**Why:** split into 3, 3, 2. Weigh the two groups of three. If they balance, the heavy ball is in the pair — one more weighing finds it. If one side is heavier, take those three, weigh one against another; either one drops or it is the third. Each weighing has **three** outcomes, so you divide by 3, not 2.
</details>
