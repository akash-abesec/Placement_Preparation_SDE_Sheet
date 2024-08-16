# Problem :- https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Solution :- https://youtube.com/watch?v=C2rRzz-JDk8


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        n=len(nums3)
        if n%2!=0:
            return nums3[n//2]
        else:
            return (nums3[(n+1)//2]+nums3[(n-1)//2])/2
