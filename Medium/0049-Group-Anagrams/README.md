# 49. Group Anagrams

## 🔗 Problem

Given an array of strings `strs`, group all anagrams together into separate lists.

The groups may be returned in any order.

An **anagram** is a word formed by rearranging the letters of another word while using exactly the same characters with the same frequencies.

---

## Example 1

```text
Input:

strs = ["act","pots","tops","cat","stop","hat"]

Output:

[["hat"],["act","cat"],["stop","pots","tops"]]
```

Explanation:

- `"act"` and `"cat"` are anagrams.
- `"pots"`, `"tops"` and `"stop"` are anagrams.
- `"hat"` has no matching anagram.

The order of the groups and the words inside them may be different.

---

## Example 2

```text
Input:

strs = ["x"]

Output:

[["x"]]
```

Explanation:

There is only one word, so it forms its own group.

---

## Example 3

```text
Input:

strs = [""]

Output:

[[""]]
```

Explanation:

The empty string is grouped by itself.

---

## Difficulty

Medium

---

## Topics

- Array
- Hash Table
- String
- Sorting

---

## Approach

This solution uses a **Hash Map** and the sorted version of each word as a grouping key.

Anagrams contain the same characters with the same frequencies. Therefore, when their characters are sorted, they produce the same string.

For example:

```text
"act"  → "act"
"cat"  → "act"

"pots" → "opst"
"tops" → "opst"
"stop" → "opst"
```

---

### Step 1

Create an empty dictionary.

```python
groups = {}
```

The dictionary stores:

```text
sorted word → list of original words
```

---

### Step 2

Traverse every word in the input array.

```python
for word in strs:
```

---

### Step 3

Sort the characters of the current word and use the result as a key.

```python
key = "".join(sorted(word))
```

For example:

```text
word = "cat"
key = "act"
```

---

### Step 4

If the key does not exist in the dictionary, create an empty list.

```python
if key not in groups:
    groups[key] = []
```

---

### Step 5

Add the original word to the list associated with its key.

```python
groups[key].append(word)
```

Words with the same sorted key are placed in the same group.

---

### Step 6

Return all grouped lists.

```python
return list(groups.values())
```

---

## Solution

```python
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
```

---

## Dry Run

Example:

```text
strs = ["act","pots","tops","cat","stop","hat"]
```

| Word | Sorted Key | Dictionary After Processing |
|------|------------|-----------------------------|
| `"act"` | `"act"` | `{"act": ["act"]}` |
| `"pots"` | `"opst"` | `{"act": ["act"], "opst": ["pots"]}` |
| `"tops"` | `"opst"` | `{"act": ["act"], "opst": ["pots", "tops"]}` |
| `"cat"` | `"act"` | `{"act": ["act", "cat"], "opst": ["pots", "tops"]}` |
| `"stop"` | `"opst"` | `{"act": ["act", "cat"], "opst": ["pots", "tops", "stop"]}` |
| `"hat"` | `"aht"` | `{"act": ["act", "cat"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]}` |

Final result:

```text
[
    ["act", "cat"],
    ["pots", "tops", "stop"],
    ["hat"]
]
```

---

## Key Idea

Use the sorted version of each word as a common key.

All anagrams produce the same sorted string, so they can be grouped together in the same Hash Map entry.

---

## Time Complexity

```text
O(n × k log k)
```

Where:

- `n` is the number of strings.
- `k` is the average length of a string.

Each word is sorted, which takes `O(k log k)` time.

---

## Space Complexity

```text
O(n × k)
```

The Hash Map stores all input strings inside their corresponding groups.

---

## What I Learned

- How to group related values using a Hash Map.
- How to use a transformed value as a dictionary key.
- Why sorting anagrams produces the same representation.
- How `sorted()` and `"".join()` work together in Python.
- How to return dictionary values as a list.
- How the Valid Anagram idea can be extended to group multiple words.