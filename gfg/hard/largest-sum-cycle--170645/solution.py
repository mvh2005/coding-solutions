class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)
        
        res = -1
        def dfs(v,path={},sum =0):
            nonlocal res
            if v== -1:
                return 
            sum+= v
            if v in path:
                res = max(res, sum - path[v])
                return 
            path[v] = sum
            dfs(edge[v],path,sum)
            edge[v] =-1
            path.pop(v)
            
        for i in range(n):
            if edge[i] != -1:
                dfs(i)
        return res
            