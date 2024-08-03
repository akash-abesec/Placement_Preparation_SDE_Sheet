# Problem :-https://leetcode.com/problems/two-sum/description/

# Solution :- https://www.youtube.com/watch?v=UXDSeD9mN-k&ab_channel=takeUforward

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
