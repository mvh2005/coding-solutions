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