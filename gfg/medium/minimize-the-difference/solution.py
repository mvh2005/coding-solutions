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