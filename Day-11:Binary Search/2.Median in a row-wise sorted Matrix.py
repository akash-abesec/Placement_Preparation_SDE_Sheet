# Problem :- https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=median-in-a-row-wise-sorted-matrix

# Solution :- https://www.youtube.com/watch?v=Q9wXgdxJq48


class Solution:
    def median(self, matrix, R, C):
        arr = []
        for i in range(R):
            for j in range(C):
                arr.append(matrix[i][j])
        
        # Sort the array
        arr.sort()
        
        # Find the median element
        mid = len(arr) // 2
        if len(arr) % 2 == 0:
            median = (arr[mid-1] + arr[mid]) / 2
        else:
            median = arr[mid]
        
        return median
