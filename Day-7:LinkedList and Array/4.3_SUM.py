#  Problem :- https://leetcode.com/problems/3sum/description/

#  Solution :- https://www.youtube.com/watch?v=DhFh8Kw7ymk



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        l=len(nums)
        for i in range(l-2):
            if i==0 or i>0 and nums[i]!=nums[i-1]:
                j=i+1
                k=l-1
                sm=0-nums[i]
                while j<k:
                    if nums[j]+nums[k]==sm:
                        result.append([nums[i],nums[j],nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j+=1
                        while j<k and nums[k]==nums[k-1]:
                            k-=1
                        j+=1
                        k-=1
                    elif nums[j]+nums[k]<sm:
                        j+=1
                    else:
                        k-=1
        return result
