# 88. Merge Sorted Array

## 🔗 Problem

Merge two sorted arrays into `nums1` in-place.

## Difficulty

Easy

## Topics

- Array
- Two Pointers

## Approach

This solution uses three pointers:

- `i`: points to the last valid element in `nums1`
- `j`: points to the last element in `nums2`
- `k`: points to the last position in `nums1`

Since `nums1` has empty space at the end, the merge operation starts from the back to avoid overwriting existing elements.

## Time Complexity

O(m + n)

## Space Complexity

O(1)

## What I Learned

- Two Pointer technique
- In-place array modification
- Merging sorted arrays from the end