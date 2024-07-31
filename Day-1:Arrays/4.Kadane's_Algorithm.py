#  Problem :- https://leetcode.com/problems/maximum-subarray/

#  Solution :- https://www.youtube.com/watch?v=AHZpyENo7k4&ab_channel=takeUforward

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxEnding = nums[0]
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        return res
