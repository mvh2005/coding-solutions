# Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, return  *the longest*   *palindromic*   *substring*  in `s`.

 

 **Example 1:** 

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

 **Example 2:** 

```
Input: s = "cbbd"
Output: "bb"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution

**Language:** Python  
**Runtime:** 10171 ms (beats 5.01%)  
**Memory:** 12.2 MB (beats 94.08%)  
**Submitted:** 2026-10-25T15:17:29.532Z  

```py
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                          longest = substring 
        return longest
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)