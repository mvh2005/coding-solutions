# Balanced Binary Tree Counter

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a height  **h**, find the maximum number of distinct balanced binary trees of height exactly h.

A binary tree is balanced if, for every node, the heights of its left and right subtrees differ by at most 1. A tree with a single node has height 1. An empty tree has height 0.

 **Note:**  Since the answer can be very large, return it modulo 109 + 7.

 **Examples:** 

```
Input: h = 1
Output: 1
Explanation: Only one tree of height 1 exists i.e. a single node.
```

```
Input: h = 2
Output: 3 
Explanation: 3 distinct balanced trees of height 2 exist.

```

```
Input: h = 3
Output: 15
Explanation: 15 distinct balanced trees of height 3 exist.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T04:06:41.220Z  

```py

class Solution:
    def countBT(self, h: int) -> int:
        MOD = 10**9 + 7

        if h == 0:
            return 1
        if h == 1:
            return 1

        dp = [0] * (h + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, h + 1):
            dp[i] = (
                dp[i-1] * dp[i-1] +
                2 * dp[i-1] * dp[i-2]
            ) % MOD

        return dp[h]

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/bbt-counter4914/1)