# Problem :- https://leetcode.com/problems/rotate-image/description/

#  Solution :- https://www.youtube.com/watch?v=Z0R2u6gd3GU&ab_channel=takeUforward

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
