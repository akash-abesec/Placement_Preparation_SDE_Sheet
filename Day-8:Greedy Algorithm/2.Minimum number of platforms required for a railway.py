# Problem :- https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

# Solution :- https://www.youtube.com/watch?v=AsGzwR_FWok

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i, j, res, curr = 1, 0, 1, 1
        while i<n and j<n:
            if arr[i] <= dep[j]:
                curr +=1
                i+=1
            else:
                curr -=1
                j+=1
            res = max(res, curr)
        return res
