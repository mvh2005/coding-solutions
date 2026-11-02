class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(num - median) for num in nums) #Understanding the logic in this phase while sorting and finding the median of the array and finding the total sum of the differences of each number by meadiam term 
        