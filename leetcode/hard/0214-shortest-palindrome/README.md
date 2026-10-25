# Shortest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it.

Return  *the shortest palindrome you can find by performing this transformation*.

 

 **Example 1:** 

```
Input: s = "aacecaaa"
Output: "aaacecaaa"

```

 **Example 2:** 

```
Input: s = "abcd"
Output: "dcbabcd"

```

 

 **Constraints:** 

- 0 <= s.length <= 5 * 104
- s consists of lowercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 143 ms (beats 14.20%)  
**Memory:** 14.2 MB (beats 98.44%)  
**Submitted:** 2026-10-25T15:29:32.192Z  

```py
class Solution(object):
    def shortestPalindrome(self, s):
        r = s[::-1]

        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s
        
        return ""

        
```

---

[View on LeetCode](https://leetcode.com/problems/shortest-palindrome/)