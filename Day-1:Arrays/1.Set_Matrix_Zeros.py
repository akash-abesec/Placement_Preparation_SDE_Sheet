# Problem :- https://leetcode.com/problems/set-matrix-zeroes/description/

# Solution Video :- https://www.youtube.com/watch?v=N0MgLvceX7M&t=1s&ab_channel=takeUforward


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col = [0] *m
        row = [0] *n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(n):
            for j in range(m):
                if row[i] or col [j] :
                    matrix[i][j] = 0
        return matrix
