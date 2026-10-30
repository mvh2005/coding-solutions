# Subsets with MEX in Range

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array **arr[]** of integers and a range  **[l, r]**, count the number of subsets whose Minimum Excluded (MEX) value lies within the given range, inclusive.

- Minimum Excluded (or MEX) of a subset is the smallest non-negative integer that is not present in the subset.
- An empty subset has Minimum Excluded as zero.

Since the answer can be very large, return the answer modulo  **109 + 7**.

 **Examples:** 

```
Input: arr[] = [2, 0, 1, 0], l = 1, r = 2
Output: 9
Explanation: The subsets whose MEX lies in the range [1, 2] are counted as follows:
MEX = 1: The subsets must contain at least one 0 and must not contain 1. These subsets are [0] (2 ways), [2, 0] (2 ways), [0, 0] (1 way), and [2, 0, 0] (1 way). Total = 6.
MEX = 2: The subsets must contain both 0 and 1 but must not contain 2. These subsets are [0, 1] (2 ways) and [0, 1, 0] (1 way). Total = 3.
The subsets [2, 0, 1] and [2, 0, 1, 0] have MEX = 3, which is outside the given range. Therefore, the total number of valid subsets is 6 + 3 = 9.
```

```
Input: arr[] = [2, 0, 1], l = 1, r = 2
Output: 3
Explanation: The subsets whose MEX lies in the range [1, 2] are [0] (MEX = 1), [2, 0] (MEX = 1), and [0, 1] (MEX = 2). Hence, the answer is 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T10:03:22.706Z  

```py
class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        cnt = [0] * (n + 2)
        for x in arr:
            if 0 <= x <= n:
                cnt[x] += 1
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD
        ans, mst, used = 0, 1, 0
        for m in range(min(r, n) + 1):
            used += cnt[m]
            if m >= l:                      
                ans = (ans + mst * pow2[n - used]) % MOD
            mst = mst * (pow2[cnt[m]] - 1) % MOD
            if mst == 0:
                break
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/crazy-subsets--131708/1)