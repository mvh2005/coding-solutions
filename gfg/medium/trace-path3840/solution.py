class Solution:
    def isPossible(self, n, m, s):
        x = y = a = b = c = d = 0
        for ch in s:
            if ch == 'L': y -= 1
            elif ch == 'R': y += 1
            elif ch == 'D': x -= 1
            else: x += 1
            a, b = min(a, x), max(b, x)
            c, d = min(c, y), max(d, y)
        return b - a < n and d - c < m


                
                
        