# 27. Remove Element

## 🔗 Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.

Return the number of elements that are **not equal** to `val`.

The order of the remaining elements does not matter.

---

## Example 1

```text
Input:

nums = [3,2,2,3]
val = 3

Output:

2
```

Explanation:

After removing all occurrences of `3`, the remaining elements are:

```text
[2,2]
```

The function returns:

```text
2
```

---

## Example 2

```text
Input:

nums = [0,1,2,2,3,0,4,2]
val = 2

Output:

5
```

Explanation:

After removing all occurrences of `2`, one possible result is:

```text
[0,1,3,0,4]
```

The function returns:

```text
5
```

The order of the remaining elements is not important.

---

## Difficulty

Easy

---

## Topics

- Array
- Two Pointers

---

## Approach

This solution uses the **Two Pointers** technique.

Instead of creating a new array, we overwrite unwanted elements while traversing the original array.

---

### Step 1

Create a pointer `k`.

```text
k = 0
```

This pointer represents the position where the next valid element should be placed.

---

### Step 2

Traverse every element in the array.

If the current element is **not equal** to `val`, copy it to position `k`.

```text
nums[k] = current_element
```

Then move `k` one step forward.

```text
k += 1
```

---

### Step 3

Ignore every element equal to `val`.

Those values are simply skipped.

---

### Step 4

After the loop finishes, `k` represents the number of valid elements remaining in the array.

Return `k`.

---

## Solution

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for num in nums:

            if num != val:
                nums[k] = num
                k += 1

        return k
```

---

## Dry Run

Example:

```text
nums = [3,2,2,3]
val = 3
```

Initial array

```text
[3,2,2,3]
```

| Current Element | Action | k | Array |
|---------------:|--------|--:|-------|
| 3 | Skip | 0 | [3,2,2,3] |
| 2 | Copy to index 0 | 1 | [2,2,2,3] |
| 2 | Copy to index 1 | 2 | [2,2,2,3] |
| 3 | Skip | 2 | [2,2,2,3] |

The first `k` elements are:

```text
[2,2]
```

Return:

```text
2
```

---

## Key Idea

Use one pointer to scan the array and another pointer to keep track of where the next valid element should be placed.

This allows the array to be modified **in-place** without using extra memory.

---

## Time Complexity

```text
O(n)
```

Each element is visited exactly once.

---

## Space Complexity

```text
O(1)
```

No extra array is created.

Only one pointer is used.

---

## What I Learned

- How the **Two Pointers** technique works.
- How to filter elements without creating a new array.
- How to modify an array **in-place**.
- How to overwrite unwanted values efficiently.
- How to solve the problem using **constant extra space**.