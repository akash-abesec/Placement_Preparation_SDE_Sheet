# Problem :- https://leetcode.com/problems/merge-intervals/description/

# Solution :- https://www.youtube.com/watch?v=IexN60k62jo&ab_channel=takeUforward

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        return stack
