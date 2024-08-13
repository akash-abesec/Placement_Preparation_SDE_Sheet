# Problem :- https://www.geeksforgeeks.org/problems/subset-sums2234/1

# Solution :- https://www.youtube.com/watch?v=rYkfBRtMJr8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=53


#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
        ans = []
        def subsetsumshepler(ind, sum1):
            if ind == n:
                ans.append(sum1)
                return 
            subsetsumshepler(ind+1, sum1+arr[ind])
            subsetsumshepler(ind+1, sum1)
        subsetsumshepler(0,0)
        ans.sort()
        return ans
