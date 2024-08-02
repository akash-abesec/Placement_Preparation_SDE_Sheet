#  Problem :- https://leetcode.com/problems/majority-element/

#  Solution :- https://www.youtube.com/watch?v=nP_ns3uSh80&ab_channel=takeUforward

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        candidate=nums[0]
        for x in nums:
            if c==0: 
                candidate=x
            if x==candidate:
                c+=1
            else:
                c-=1
        return candidate
        
