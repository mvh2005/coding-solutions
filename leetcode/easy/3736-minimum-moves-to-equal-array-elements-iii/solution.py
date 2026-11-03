class Solution(object):
    def minMoves(self, nums):
        ma = max(nums)
        return sum(ma - x for x in nums)
        