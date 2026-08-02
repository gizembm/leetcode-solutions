# 217. Contains Duplicate

## 🔗 Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array. Otherwise, return `false`.

---

## Example 1

```text
Input:
nums = [1,2,3,1]

Output:
true
```

Explanation:

The number `1` appears **twice**, so the array contains a duplicate.

---

## Example 2

```text
Input:
nums = [1,2,3,4]

Output:
false
```

Explanation:

Every element appears only once.

---

## Example 3

```text
Input:
nums = [1,1,1,3,3,4,3,2,4,2]

Output:
true
```

Explanation:

Several numbers appear more than once.

---

## Difficulty

Easy

---

## Topics

- Array
- Hash Table

---

## Approach

This solution uses a **Hash Set** to keep track of the numbers that have already been seen.

### Step 1

Create an empty set.

```python
seen = set()
```

The set will store every number we have visited.

---

### Step 2

Traverse the array one element at a time.

For each number:

- If it already exists in the set, a duplicate has been found.
- Return `True` immediately.

```text
Current Number → Already in Set?
```

---

### Step 3

If the number has not been seen before, add it to the set.

Example:

```text
nums = [5,7,2,5]
```

| Current Number | Set |
|---------------:|-----|
| 5 | {5} |
| 7 | {5,7} |
| 2 | {5,7,2} |
| 5 | Duplicate found ✅ |

As soon as the second `5` is found, return `True`.

---

### Step 4

If the loop finishes without finding any duplicates, return `False`.

---

## Solution

```python
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

---

## Dry Run

Example:

```text
nums = [1,2,3,1]
```

Initial set

```text
{}
```

Process each element

| Current Number | Set After Processing |
|---------------:|----------------------|
| 1 | {1} |
| 2 | {1,2} |
| 3 | {1,2,3} |
| 1 | Duplicate found → Return True |

---

## Key Idea

Instead of comparing every number with every other number, remember the numbers that have already been seen.

A **Hash Set** allows us to check whether a value already exists in **constant time**, making the solution much faster.

---

## Time Complexity

```text
O(n)
```

The array is traversed only once.

Each lookup and insertion into the Hash Set takes approximately **O(1)** time.

---

## Space Complexity

```text
O(n)
```

In the worst case, every element is unique, so all elements are stored in the Hash Set.

---

## What I Learned

- How to use a **Hash Set (`set`)** in Python.
- How to check whether an element has already been seen.
- Why Hash Sets provide fast lookup operations.
- How to solve duplicate detection in **O(n)** time.
- The difference between a brute-force **O(n²)** solution and an optimized **O(n)** solution.