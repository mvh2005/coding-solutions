# Minimum XOR Path in a Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2D integer array `grid` of size `m * n`.

You start at the  **top-left**  cell `(0, 0)` and want to reach the  **bottom-right**  cell `(m - 1, n - 1)`.

At each step, you  **may**  move either  **right or down**.

The  **cost**  of a path is defined as the  **bitwise XOR**  of all the values in the cells along that path,  **including**  the start and end cells.

Return the  **minimum**  possible XOR value among all valid paths from `(0, 0)` to `(m - 1, n - 1)`.

 

 **Example 1:** 

 **Input:**  grid = [[1,2],[3,4]]

 **Output:**  6

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
- (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

 **Example 2:** 

 **Input:**  grid = [[6,7],[5,8]]

 **Output:**  9

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
- (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

 **Example 3:** 

 **Input:**  grid = [[2,7,5]]

 **Output:**  0

 **Explanation:** 

There is only one valid path:

- (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

 

 **Constraints:** 

- 1 <= m == grid.length <= 1000
- 1 <= n == grid[i].length <= 1000
- m * n <= 1000
- 0 <= grid[i][j] <= 1023​

## Solution

**Language:** Python  
**Runtime:** 1065 ms (beats 66.67%)  
**Memory:** 18.2 MB (beats 88.89%)  
**Submitted:** 2026-10-28T04:51:55.895Z  

```py
class Solution(object):
    def minCost(self, grid):
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])

        # dp[j] = set of all XOR values reachable at the current row, column j
        dp = [set() for _ in range(n)]
        dp[0] = {grid[0][0]}

        for j in range(1, n):                      # first row
            dp[j] = {x ^ grid[0][j] for x in dp[j - 1]}

        for i in range(1, m):
            # first column: only comes from above
            dp[0] = {x ^ grid[i][0] for x in dp[0]}
            for j in range(1, n):
                # reachable from above (dp[j]) or from the left (dp[j-1])
                dp[j] = {x ^ grid[i][j] for x in (dp[j] | dp[j - 1])}

        return min(dp[n - 1])
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)