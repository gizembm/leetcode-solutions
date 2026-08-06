# 347. Top K Frequent Elements

## 🔗 Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

The answer is guaranteed to be unique, and you may return the elements in any order.

---

## Example 1

```text
Input:

nums = [1,2,2,3,3,3]
k = 2

Output:

[2,3]
```

Explanation:

The frequency of each number is:

| Number | Frequency |
|--------:|----------:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

The two most frequent numbers are `3` and `2`.

Since the output order does not matter, both `[3,2]` and `[2,3]` are accepted.

---

## Example 2

```text
Input:

nums = [7,7]
k = 1

Output:

[7]
```

Explanation:

There is only one distinct number in the array, so it is returned.

---

## Difficulty

Medium

---

## Topics

- Array
- Hash Table
- Bucket Sort

---

## Approach

This solution combines a **Hash Map** with **Bucket Sort** to achieve an optimal **O(n)** time complexity.

### Step 1

Count the frequency of every number using a Hash Map.

Example:

```text
nums = [1,2,2,3,3,3]

Frequency Map

1 → 1
2 → 2
3 → 3
```

---

### Step 2

Create frequency buckets.

Each bucket index represents how many times a number appears.

```text
Index (Frequency)

0 → []
1 → []
2 → []
3 → []
...
```

---

### Step 3

Place every number into its corresponding bucket.

```text
Frequency 1 → [1]

Frequency 2 → [2]

Frequency 3 → [3]
```

---

### Step 4

Traverse the buckets from the highest frequency to the lowest.

Add numbers to the result until exactly `k` elements have been collected.

---

## Alternative Solutions

### 1. Sorting

Count the frequency of every number and sort them by frequency.

- Time Complexity: **O(n log n)**
- Space Complexity: **O(n)**

Easy to understand, but not the most efficient solution.

---

### 2. Heap (Priority Queue)

Store frequencies in a Heap and extract the `k` most frequent elements.

- Time Complexity: **O(n log k)**
- Space Complexity: **O(n)**

A good solution when `k` is much smaller than `n`.

---

### 3. Bucket Sort ✅ (Chosen Solution)

Instead of sorting by frequency, store each number inside the bucket that corresponds to its frequency.

Traverse the buckets from highest frequency to lowest until `k` elements are collected.

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

This is the optimal solution for this problem.

---

## Solution

```python
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
```

---

## Dry Run

Example:

```text
nums = [1,2,2,3,3,3]
k = 2
```

### Frequency Map

| Number | Count |
|--------:|------:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

---

### Buckets

| Frequency | Numbers |
|----------:|---------|
| 1 | [1] |
| 2 | [2] |
| 3 | [3] |

---

### Traverse Buckets

Start from the highest frequency.

```text
Frequency 3

↓

Add 3

Result = [3]

↓

Frequency 2

↓

Add 2

Result = [3,2]
```

We now have `k = 2` elements, so the algorithm stops.

---

## Key Idea

Instead of sorting numbers by their frequencies, use the frequency itself as an index.

Each bucket stores all numbers that appear the same number of times.

By traversing the buckets from the highest frequency to the lowest, we can find the answer in **linear time**.

---

## Time Complexity

```text
O(n)
```

- Counting frequencies: **O(n)**
- Filling buckets: **O(n)**
- Traversing buckets: **O(n)**

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

Additional space is used for:

- The frequency Hash Map
- The Bucket array

---

## What I Learned

- How to count frequencies using a Hash Map.
- How Bucket Sort can be used without sorting the input.
- Why Bucket Sort achieves linear time for this problem.
- The difference between Sorting, Heap, and Bucket Sort approaches.
- How to organize elements based on their frequencies instead of their values.