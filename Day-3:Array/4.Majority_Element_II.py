# Problem :- https://leetcode.com/problems/majority-element-ii/description/

# Solution :- https://www.youtube.com/watch?v=vwZj1K0e9U8&ab_channel=takeUforward

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i] in freq):
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=0
        for i in freq:
            if freq[i]>=len(nums)//3:
                ans.append(i)
        return ans
