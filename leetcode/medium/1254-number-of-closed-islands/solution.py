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
        