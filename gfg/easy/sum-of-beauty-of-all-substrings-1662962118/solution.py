class Solution:
    def beautySum(self, s):
        total = 0
        n = len(s)
        for i in range(n):
            counts = {}
            for j in range(i, n):
                counts[s[j]] = counts.get(s[j], 0) + 1
                total += max(counts.values()) - min(counts.values())
        return total