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