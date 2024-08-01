# Problem :- https://leetcode.com/problems/find-the-duplicate-number/description/

#  Solution :- https://www.youtube.com/watch?v=32Ll35mhWg0&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=2&ab_channel=takeUforward


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        inte = 0
        mydict = Counter(nums)
        for i in mydict:
            if mydict[i]>=2:
                inte = i
        return inte
