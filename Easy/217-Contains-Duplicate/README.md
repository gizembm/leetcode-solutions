# 217. Contains Duplicate

## 🔗 Problem

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

## Difficulty

Easy

## Topics

- Array
- Hash Table
- Sorting

## Approach

This solution uses a **Hash Set** to keep track of the numbers that have already been seen.

- Create an empty set.
- Traverse the array.
- If the current number already exists in the set, return `True`.
- Otherwise, add the number to the set.
- If no duplicates are found, return `False`.

## Time Complexity

O(n)

## Space Complexity

O(n)

## What I Learned

- How to use a Hash Set (`set`) in Python
- Checking whether an element has already been seen
- Using the `in` operator for fast lookups
- Reducing time complexity from O(n²) to O(n)

## Key Idea

Use a Hash Set to detect duplicate values efficiently in one pass.