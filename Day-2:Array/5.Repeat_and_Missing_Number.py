Problem :-  https://leetcode.com/problems/find-missing-and-repeated-values/description/

# Solution :- https://www.youtube.com/watch?v=2D0D8HE6uak&ab_channel=takeUforward

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums,lis = [], []
        sumnum, nat  = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                lis.append(nums[i])
        for i in range(len(nums)):
            sumnum += nums[i]
        sumnum = sumnum-lis[0]
        for i in range(len(nums)+1):
            nat += i
        pre = nat-sumnum
        lis.append(pre)
        return lis
