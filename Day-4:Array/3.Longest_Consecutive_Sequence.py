#  Problem :- https://leetcode.com/problems/longest-consecutive-sequence/description/

# Solution :- https://www.youtube.com/watch?v=oO5uLE7EUlM&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=29&ab_channel=takeUforward

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        prev_num = nums[0]
        max_size = 1
        current_size = 1
        for i in nums:
            if (prev_num+1) == i:
                current_size +=1 
                if current_size > max_size:
                    max_size = current_size
            elif prev_num == i:
                pass
            else:
                current_size = 1
            prev_num = i
        return max_size
        
