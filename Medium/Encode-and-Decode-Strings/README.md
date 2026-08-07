# Encode and Decode Strings

## 🔗 Problem

Design an algorithm to encode a list of strings into a single string and decode it back into the original list of strings.

The encoded string may be sent over a network, so the decoding process must correctly reconstruct every original string.

---

## Examples

### Example 1

```text
Input:
["Hello", "World"]

Encoded:
"5#Hello5#World"

Decoded:
["Hello", "World"]
```

### Example 2

```text
Input:
[""]

Encoded:
"0#"

Decoded:
[""]
```

---

## Difficulty

🟡 Medium

---

## Topics

* String
* Array
* Two Pointers
* String Encoding
* String Parsing

---

## Approach

A simple separator such as `#` cannot safely be used by itself because the original strings may also contain that character.

Instead, each string is encoded using the following format:

```text
length#string
```

For example:

```text
"Hello"
```

becomes:

```text
5#Hello
```

If the input is:

```python
["Hello", "World"]
```

the encoded string becomes:

```text
5#Hello5#World
```

The number before `#` tells us exactly how many characters belong to the next string.

Because we know the length of every string, the contents of the string can contain any characters, including `#`.

---

## Step-by-Step

### Encoding

For every string:

1. Find its length.
2. Convert the length to a string.
3. Add `#` after the length.
4. Add the original string.

For example:

```text
["Hello", "World"]
```

becomes:

```text
5#Hello5#World
```

---

### Decoding

Use two pointers:

* `i` points to the beginning of the length.
* `j` searches for the `#` character.

When `#` is found:

1. Read the number between `i` and `j`.
2. Convert it to an integer.
3. Move past `#`.
4. Read exactly that many characters.
5. Add the extracted string to the result.
6. Continue until the encoded string is completely processed.

---

## Solution

```python
class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j

        return res
```

---

## Dry Run

Input:

```python
["Hello", "World"]
```

### Encode

First string:

```text
"Hello"
length = 5

→ 5#Hello
```

Second string:

```text
"World"
length = 5

→ 5#World
```

Final encoded string:

```text
5#Hello5#World
```

### Decode

Start:

```text
5#Hello5#World
^
i
```

Search until `#`:

```text
5#
```

So:

```python
length = 5
```

Read the next 5 characters:

```text
Hello
```

Result:

```python
["Hello"]
```

Continue from:

```text
5#World
```

Again:

```python
length = 5
```

Read:

```text
World
```

Final result:

```python
["Hello", "World"]
```

---

## Key Idea

Instead of relying only on a delimiter, store the length of every string before the string itself.

```text
length#string
```

This makes decoding unambiguous because we always know exactly how many characters belong to each string.

Even an input such as:

```python
["Hello#World"]
```

can safely be represented as:

```text
11#Hello#World
```

The `#` inside the original string does not cause a problem because the decoder already knows that it must read exactly 11 characters.

---

## Time Complexity

### Encode

```text
O(n)
```

where `n` is the total number of characters across all strings.

Every character is processed once.

### Decode

```text
O(n)
```

The encoded string is scanned once.

---

## Space Complexity

```text
O(n)
```

The encoded string and decoded result require space proportional to the total number of characters.

---

## What I Learned

* How to encode multiple strings into a single string
* How length-prefix encoding works
* Why using only a delimiter can be unsafe
* How to parse strings using two pointers
* How to handle empty strings correctly
* How storing metadata such as string length can make decoding unambiguous
* How this approach can work with arbitrary characters instead of depending on special separator characters
