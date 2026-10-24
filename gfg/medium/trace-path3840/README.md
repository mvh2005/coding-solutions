# Trace Path

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a rectangular grid with n rows and m columns, and a string s representing a sequence of movement commands. Geek can start from any cell of the grid and follows all the commands in s in the same order.

The string s consists only of the characters L, R, D, and U, where:

L: Move one cell left, from (i, j) to (i, j - 1).
R: Move one cell right, from (i, j) to (i, j + 1).
D: Move one cell up, from (i, j) to (i - 1, j).
U: Move one cell down, from (i, j) to (i + 1, j).
Determine whether there exists at least one starting cell such that Geek remains within the grid while following all the commands in s.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:33:30.819Z  

```py
class Solution:
    def isPossible(self, n, m, s):
        x = y = a = b = c = d = 0
        for ch in s:
            if ch == 'L': y -= 1
            elif ch == 'R': y += 1
            elif ch == 'D': x -= 1
            else: x += 1
            a, b = min(a, x), max(b, x)
            c, d = min(c, y), max(d, y)
        return b - a < n and d - c < m


                
                
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/trace-path3840/1)
