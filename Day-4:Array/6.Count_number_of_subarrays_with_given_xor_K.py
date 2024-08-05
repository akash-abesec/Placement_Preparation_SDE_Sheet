#  Problem :- https://www.interviewbit.com/problems/subarray-with-given-xor/

#  Solution :- https://www.youtube.com/watch?v=eZr-6p0B7ME&ab_channel=takeUforward


def subarraysWithXorK(a: [int], b: int) -> int:
    n = len(a)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            xorr = 0
            for K in range(i, j + 1):
                xorr = xorr ^ a[K]
            if (xorr == k):
                cnt += 1

    return cnt
