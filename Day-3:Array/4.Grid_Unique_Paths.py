 #  Problem :- https://leetcode.com/problems/unique-paths/

#  Solution :- https://youtu.be/t_f0nwwdg5o

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Number = m+n-2
        r = m-1
        res1, res2 = 1, 1
        for i in range(1, r+1):
            res1 *= Number - r +i
            res2 *= i
        return res1//res2
