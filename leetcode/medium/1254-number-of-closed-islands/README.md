# Number of Closed Islands

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An  *island*  is a maximal 4-directionally connected group of `0s` and a  *closed island*  is an island  **totally**  (all left, top, right, bottom) surrounded by `1s.`

Return the number of  *closed islands*.

 

 **Example 1:** 

```
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

 **Example 2:** 

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

```

 **Example 3:** 

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

```

 

 **Constraints:** 

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 76.61%)  
**Memory:** 12.6 MB (beats 83.87%)  
**Submitted:** 2026-10-25T02:21:22.583Z  

```py
class Solution(object):
    def closedIsland(self, grid):
        a,b = len(grid) ,len(grid[0])
        def island(i,j):
            if not(0<=i<a and 0<=j<b):
                return False #Steps of the Boundaries of the grid the island touches the boundry
            if grid[i][j]:
                return True
            grid[i][j] = 1
            return island(i+1,j) & island(i-1,j) & island(i,j+1) & island(i,j-1)
        return sum(island(i,j) for i in range(a) for j in range(b) if not grid[i][j])
        
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)