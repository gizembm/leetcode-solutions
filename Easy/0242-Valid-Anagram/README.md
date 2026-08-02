# 242. Valid Anagram

## 🔗 Problem

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other. Otherwise, return `false`.

An **anagram** is a word or phrase formed by rearranging the letters of another word while using **exactly the same characters** and **the same number of occurrences**.

---

## Example 1

```text
Input:
s = "racecar"
t = "carrace"

Output:
true
```

Explanation:

Both strings contain exactly the same characters.

| Character | Frequency |
|-----------|----------:|
| a | 2 |
| c | 2 |
| e | 1 |
| r | 2 |

Since every character appears the same number of times, the strings are anagrams.

---

## Example 2

```text
Input:
s = "jar"
t = "jam"

Output:
false
```

Explanation:

The character frequencies are different.

| Character | s | t |
|-----------|--:|--:|
| j | 1 | 1 |
| a | 1 | 1 |
| r | 1 | 0 |
| m | 0 | 1 |

Because the frequencies do not match, the strings are **not** anagrams.

---

## Difficulty

Easy

---

## Topics

- String
- Hash Table
- Sorting

---

## Approach

This solution uses a **Hash Map (Dictionary)** to count character frequencies.

### Step 1

Check whether both strings have the same length.

```python
if len(s) != len(t):
    return False
```

If the lengths are different, they cannot be anagrams.

---

### Step 2

Traverse the first string and count each character.

```text
s = "racecar"

Dictionary:

r → 2
a → 2
c → 2
e → 1
```

---

### Step 3

Traverse the second string and decrease the count of each character.

```text
t = "carrace"

Dictionary after processing:

r → 0
a → 0
c → 0
e → 0
```

If every value becomes **0**, both strings contain the same characters with the same frequencies.

---

### Step 4

Check every value in the dictionary.

If one value is not zero, return `False`.

Otherwise, return `True`.

---

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True
```

---

## Dry Run

Example:

```text
s = "jar"
t = "jam"
```

Initial dictionary

```text
{}
```

After processing **s**

```text
j → 1
a → 1
r → 1
```

After processing **t**

```text
j → 0
a → 0
r → 1
m → -1
```

Since not all values are `0`, the answer is:

```text
False
```

---

## Key Idea

Instead of comparing the strings directly, compare **how many times each character appears**.

If every character has the same frequency in both strings, they are anagrams.

---

## Time Complexity

```text
O(n)
```

Both strings are traversed once.

---

## Space Complexity

```text
O(n)
```

A dictionary is used to store character frequencies.

Since the problem contains only lowercase English letters, the dictionary can contain at most **26** different keys. Therefore, the extra space can also be considered **O(1)**.

---

## What I Learned

- How to use a Hash Map (Dictionary) in Python.
- How to count character frequencies efficiently.
- How `dict.get(key, default)` works.
- Why checking character frequencies is enough to determine an anagram.
- How to solve the problem in **O(n)** time instead of sorting the strings.
