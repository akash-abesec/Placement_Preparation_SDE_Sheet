#  Problem :- https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Solution :- https://youtube.com/watch?v=Lhu3MsXZy-Q&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=31

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        c=0
        while fast:
            if c>n:
                slow = slow.next
            fast = fast.next
            c+=1
        if n==c:
            return head.next
        else:
            slow.next = slow.next.next
        return head
        
