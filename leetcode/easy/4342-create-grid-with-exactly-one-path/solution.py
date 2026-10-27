class Solution(object):
    def createGrid(self, m, n):
        return ['.' + '#' * (n - 1)] * (m - 1) + ['.' * n]


        