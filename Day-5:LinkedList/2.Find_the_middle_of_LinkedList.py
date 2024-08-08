#  Problrm :- https://leetcode.com/problems/middle-of-the-linked-list/

#  Solution :- https://www.youtube.com/watch?v=sGdwSH8RK-o&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=29&ab_channel=takeUforward

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and slow!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
