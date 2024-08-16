# Problem :- https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Solution:- https://www.youtube.com/watch?v=r3pMQ8-Ad5s&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=66

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid +1
            else:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
