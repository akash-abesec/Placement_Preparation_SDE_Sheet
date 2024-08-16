# Problem:- https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

# Solution :- https://www.youtube.com/watch?v=nv7F4PiLUzo&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=67

# ----------- Solution :-1-----------------


class Solution:
    def kthElement(self, k, arr1, arr2):
        arr3 = arr1 + arr2
        arr3.sort()
        n = len(arr3)
        return arr3[k-1]


# ---------------Solution -2 -------------------

class Solution:
    def kthElement(self, k, arr1, arr2):
        m, n=len(arr1), len(arr2)
        if m >n:
            return self.kthElement(k,arr2, arr1)
        left = k
        low = max(0,k-n)
        high = min(k,m)
        while low <=high:
            mid1 = (low+high)//2
            mid2 = (left-mid1)
            l1=float('-inf')
            l2=float('-inf')
            r1=float('inf')
            r2=float('inf')
            if mid1<m:
                r1 = arr1[mid1]
            if mid2<n:
                r2=arr2[mid2]
            if mid1-1>=0:
                l1=arr1[mid1-1]
            if mid2-1>=0:
                l2=arr2[mid2-1]
            if l1<=r2 and l2<=r1:
                return max(l1, l2)
            elif l1>r2 :
                high = mid1-1
            else:
                low = mid1+1
        return 0
