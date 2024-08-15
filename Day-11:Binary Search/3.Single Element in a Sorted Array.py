# Problem :- https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# Solution :- https://youtube.com/watch?v=PzszoiY5XMQ&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=65


# ---------------------- Solution->1 ---------------------
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)  # Size of the array
        ans = 0
        # XOR all the elements
        for i in range(n):
            ans = ans ^ nums[i]
        return ans


# ------------------- Solution->2----------------------
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            elif i == n - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
        return -1
