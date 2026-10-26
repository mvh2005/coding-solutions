class Solution(object):
    def countIslands(self, grid, k):
        count = 0
        m,n = len(grid) , len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0 
            sum_value = grid[i][j] 
            grid[i][j] = 0
            sum_value+=dfs(i+1,j)
            sum_value+=dfs(i-1,j)
            sum_value+=dfs(i,j+1)
            sum_value+=dfs(i,j-1)
            return sum_value
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)

                    if total % k == 0:
                        count += 1

        return count
                       
        