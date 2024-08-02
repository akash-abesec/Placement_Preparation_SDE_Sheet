# Problem  :- https://leetcode.com/problems/search-a-2d-matrix/description/

#  Solution :- https://www.youtube.com/watch?v=JXU4Akft7yk&ab_channel=takeUforward

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        low=0
        high=(row*col)-1
        while low<=high:
            mid=(low+high)//2
            r=mid//col
            c=(mid%col)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                high=mid-1
            else:
                low=mid+1
        return False
