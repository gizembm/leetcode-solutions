# 27. Remove Element

## 🔗 Problem

Remove all occurrences of `val` from the array in-place and return the number of remaining elements.

## Difficulty

Easy

## Topics

- Array
- Two Pointers

## Approach

This solution uses the **Two Pointer** technique.

- `num`: iterates through every element in the array.
- `k`: points to the position where the next valid element should be placed.

If the current element is different from `val`, it is copied to index `k`, and `k` is incremented. This keeps all valid elements at the beginning of the array without using extra space.

## Time Complexity

O(n)

## Space Complexity

O(1)

## What I Learned

- Two Pointer technique
- In-place array modification
- Filtering elements without creating a new array