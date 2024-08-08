# Problem:- https://leetcode.com/problems/merge-two-sorted-lists/description/

#  Solution :- https://www.youtube.com/watch?v=Xb4slcp1U38&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=30

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:return list2
        if list2==None:return list1
        head=tail=None
        ptr1,ptr2=list1,list2
        if ptr1.val>=ptr2.val:
            tail=head=ptr2
            ptr2=ptr2.next
        else:
            tail=head=ptr1
            ptr1=ptr1.next
        while ptr1!=None and ptr2!=None:
            if ptr1.val<=ptr2.val:
                tail.next=ptr1
                tail=ptr1
                ptr1=ptr1.next
            else:
                tail.next=ptr2
                tail=ptr2
                ptr2=ptr2.next
        if ptr1==None:
            tail.next=ptr2
        else:
            tail.next=ptr1
        return head
