# optimal-file-merge

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T16:41:58.347Z  

```py
class Solution:
    def minComputation(self, files):
        import heapq
        pq = files
        heapq.heapify(pq)
        
        ans = 0
        while len(pq) > 1:
            x, y = heapq.heappop(pq), heapq.heappop(pq)
            ans += x + y
            heapq.heappush(pq, x+y)
        
        return ans
        
        #But i understand the floe of the second code and i dont know why thise time taking more of this simple code 
        # total = 0
        # files = files.copy()
        # while len(files) > 1:
        #     files.sort()
            
        #     x = files.pop(0)
        #     y = files.pop(0)
            
        #     cost = x + y
        #     total += cost
            
        #     files.append(cost)
        # return total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/optimal-file-merge/1)