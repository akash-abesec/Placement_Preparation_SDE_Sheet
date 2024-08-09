#  Problem :-https://leetcode.com/problems/max-consecutive-ones/description/

#  Solution :- https://www.youtube.com/watch?v=bYWLJb3vCWY&t=1124s


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        mx = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                mx = max(mx, count)
                count = 0
        return max(mx, count)
        
