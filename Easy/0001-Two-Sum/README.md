# 1. Two Sum

## 🔗 Problem

Given an integer array `nums` and an integer `target`, return the indices of two different elements whose sum is equal to `target`.

You may assume that exactly one valid answer exists.

Return the smaller index first.

---

## Example 1

```text
Input:

nums = [3,4,5,6]
target = 7

Output:

[0,1]
```

Explanation:

```text
nums[0] + nums[1] = 3 + 4 = 7
```

Therefore, the answer is:

```text
[0,1]
```

---

## Example 2

```text
Input:

nums = [4,5,6]
target = 10

Output:

[0,2]
```

Explanation:

```text
nums[0] + nums[2] = 4 + 6 = 10
```

---

## Example 3

```text
Input:

nums = [5,5]
target = 10

Output:

[0,1]
```

Explanation:

The two values are equal, but they are stored at different indices.

---

## Difficulty

Easy

---

## Topics

- Array
- Hash Table

---

## Approach

This solution uses a **Hash Map** to store numbers that have already been visited.

### Step 1

Create an empty dictionary.

```python
seen = {}
```

The dictionary stores:

```text
number → index
```

---

### Step 2

Traverse the array using `enumerate()`.

For each number, calculate the value required to reach the target.

```python
complement = target - num
```

---

### Step 3

Check whether the complement has already been seen.

If it exists in the dictionary, return its stored index and the current index.

```python
if complement in seen:
    return [seen[complement], index]
```

---

### Step 4

If the complement has not been found, store the current number and its index.

```python
seen[num] = index
```

---

## Solution

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index
```

---

## Dry Run

Example:

```text
nums = [3,4,5,6]
target = 7
```

| Index | Current Number | Complement | Hash Map Before | Action |
|------:|---------------:|-----------:|-----------------|--------|
| 0 | 3 | 4 | `{}` | Store `3: 0` |
| 1 | 4 | 3 | `{3: 0}` | Complement found, return `[0,1]` |

---

## Key Idea

For each number, calculate the value needed to reach the target.

A Hash Map allows us to check whether that value has already appeared in approximately constant time.

This avoids comparing every pair of elements.

---

## Time Complexity

```text
O(n)
```

The array is traversed once.

Hash Map lookup and insertion take approximately `O(1)` time.

---

## Space Complexity

```text
O(n)
```

In the worst case, the Hash Map stores most of the array elements.

---

## What I Learned

- How to use a Hash Map in Python.
- How to store values together with their indices.
- How to use `enumerate()` to access both an index and a value.
- How to calculate the complement using `target - num`.
- How to reduce a brute-force `O(n²)` solution to an optimized `O(n)` solution.