# 88. Merge Sorted Array

## 🔗 Problem

You are given two sorted integer arrays, `nums1` and `nums2`, and two integers `m` and `n`.

- `nums1` contains the first `m` valid elements, followed by `n` empty spaces (`0`s).
- `nums2` contains `n` sorted elements.

Merge `nums2` into `nums1` as one sorted array.

The merge must be performed **in-place**, meaning you are not allowed to use another array.

---

## Example 1

```text
Input:

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Output:

[1,2,2,3,5,6]
```

Explanation:

Both arrays are already sorted.

After merging them while keeping the order, `nums1` becomes:

```text
[1,2,2,3,5,6]
```

---

## Example 2

```text
Input:

nums1 = [1]
m = 1

nums2 = []
n = 0

Output:

[1]
```

Explanation:

The second array is empty, so nothing needs to be merged.

---

## Example 3

```text
Input:

nums1 = [0]
m = 0

nums2 = [1]
n = 1

Output:

[1]
```

Explanation:

The first array has no valid elements.

Simply copy the elements from `nums2`.

---

## Difficulty

Easy

---

## Topics

- Array
- Two Pointers
- Sorting

---

## Approach

The key idea is to merge the arrays **from the end** instead of the beginning.

Why?

If we start from the front, we may overwrite valid elements in `nums1`.

Instead, we compare the largest remaining elements and place the larger one at the end of `nums1`.

---

### Step 1

Create three pointers.

```text
i → Last valid element in nums1

j → Last element in nums2

k → Last position in nums1
```

Example:

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

i = 2
j = 2
k = 5
```

---

### Step 2

Compare the elements at `i` and `j`.

```text
nums1[i] = 3

nums2[j] = 6
```

Since `6` is larger,

place it at position `k`.

```text
[1,2,3,0,0,6]
```

Move the pointers.

```text
j--
k--
```

---

### Step 3

Continue comparing until one array is exhausted.

Each step places the largest remaining element into its correct position.

---

### Step 4

If there are still elements left in `nums2`, copy them into `nums1`.

If `nums1` still has remaining elements, nothing needs to be done because they are already in the correct position.

---

## Solution

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Dry Run

Example:

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

| i | j | k | Action | nums1 |
|--:|--:|--:|--------|--------|
|2|2|5|6 is larger → place 6|[1,2,3,0,0,6]|
|2|1|4|5 is larger → place 5|[1,2,3,0,5,6]|
|2|0|3|3 is larger → place 3|[1,2,3,3,5,6]|
|1|0|2|2 is equal → place nums2 value|[1,2,2,3,5,6]|

The final merged array is:

```text
[1,2,2,3,5,6]
```

---

## Key Idea

Instead of shifting elements to make space, fill the array **from the end**.

This prevents overwriting existing values and allows the merge to be completed **in-place**.

---

## Time Complexity

```text
O(m + n)
```

Each element is processed at most once.

---

## Space Complexity

```text
O(1)
```

Only three pointers are used.

No additional array is created.

---

## What I Learned

- How the **Two Pointers** technique works.
- Why merging from the end avoids overwriting existing values.
- How to perform an **in-place** merge.
- How to solve the problem without using extra memory.
- How multiple pointers can simplify array manipulation.