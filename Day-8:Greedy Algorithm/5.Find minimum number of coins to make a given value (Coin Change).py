# Problem :- https://leetcode.com/problems/coin-change/

# Solution :- https://www.youtube.com/watch?v=mVg9CfJvayM&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=49


class Solution:
    def minPartition(self, N):
        # code here
        coin = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ][::-1]
        ans = []
        for i in coin :
            if i<=N:
                while i<=N:
                    ans.append(i)
                    N-=i
        return ans
