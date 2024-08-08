#  Problem :- https://leetcode.com/problems/intersection-of-two-linked-lists/description/

#  Soluiton :- https://www.youtube.com/watch?v=u4FWXfgS8jw&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=34


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1 = headA
        s2 = headB
        while s1 or s2:
            if s1==None:
                s1 = headB
            if s2==None:
                s2 = headA
            if s1 == s2:
                return s1
            s1 = s1.next
            s2 = s2.next
        return 
