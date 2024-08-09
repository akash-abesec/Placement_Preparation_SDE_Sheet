# Problem :- https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Solution :- https://youtube.com/watch?v=37E9ckMDdTk&t=1888s



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
