# 27. Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place and return the number of remaining elements.

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/remove-element/

---

## Approach

This solution uses the **two-pointer technique**.

- `num` iterates through every element.
- `k` points to the position where the next valid element should be placed.
- If the current element is different from `val`, it is copied to index `k`.
- Finally, `k` represents the number of remaining elements.

### Time Complexity

```
O(n)
```

### Space Complexity

```
O(1)
```

---

## Python Solution

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
```