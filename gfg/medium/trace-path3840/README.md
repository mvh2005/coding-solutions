# trace-path3840

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

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