# Minimize Max Min Diff with Subarray Removal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array  **arr[]**  of size  **n**. You need to remove a subarray of size  **k** , such that the difference between the maximum and minimum values of the remaining array is minimized. Find the minimum value obtained after performing the operation of the removal of the subarray.

 **Examples:** 

```
Input: arr = [1, 2, 3, 4, 5], k = 3 
Output: 1
Explanation: We remove first subarray of length 3, the remaining array is [4,5] and the difference of maximum and minimum element is 1 i.e 5 - 4 = 1
```

```
Input: arr = [2, 3, 1, 4, 6, 7], k = 3
Output: 2
Explanation: 
If we remove the subarray [2,3,1] then remaining array is [4,6,7] and the difference  = 7-4 = 3
If we remove the subarray [3,1,4] then remaining array is [2,6,7] and the difference  = 7-2 = 5
If we remove the subarray [1,4,6] then remaining array is [2,3,7] and the difference  = 7-2 = 5
If we remove the subarray [4,6,7] then remaining array is [2,3,1] and the difference  = 3-1 = 2
So the answer is min(3,5,5,2) = 2
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T05:39:46.582Z  

```py
class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k >= n:
            return 0

        INF = float('inf')

        # prefix min/max: pmin[i], pmax[i] cover arr[:i]
        pmin = [INF] * (n + 1)
        pmax = [-INF] * (n + 1)
        for i in range(n):
            pmin[i + 1] = min(pmin[i], arr[i])
            pmax[i + 1] = max(pmax[i], arr[i])

        # suffix min/max: smin[j], smax[j] cover arr[j:]
        smin = [INF] * (n + 1)
        smax = [-INF] * (n + 1)
        for j in range(n - 1, -1, -1):
            smin[j] = min(smin[j + 1], arr[j])
            smax[j] = max(smax[j + 1], arr[j])

        best = INF
        for i in range(n - k + 1):
            lo = min(pmin[i], smin[i + k])
            hi = max(pmax[i], smax[i + k])
            best = min(best, hi - lo)

        return best
```
```py
class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:

        values = []
        for i in range(len(arr)-k+1):
            rem = arr[:i] + arr[i+k:] 
            
            if rem:
                value = max(rem) - min(rem)
                values.append(value)
            
        return min(values)

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimize-the-difference/1)
