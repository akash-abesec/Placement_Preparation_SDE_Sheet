# Probelm:- https://leetcode.com/problems/subsets-ii/description/

# Solution :- https://www.youtube.com/watch?v=RIn3gOkbhQE&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=55


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, ds = [], []
        def findsubsets(ind):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i!=ind and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                findsubsets(i+1)
                ds.pop()
        nums.sort()
        findsubsets(0)
        return ans
