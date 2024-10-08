#  Problem :- https://leetcode.com/problems/reverse-nodes-in-k-group/description/

#  Solution :- https://www.youtube.com/watch?v=Of0HPkk3JgI&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=35


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None or k==1): return head
        temp=ListNode()
        temp.next=head
        pre=temp
        cur=None
        nex=None
        size=0
        curr=head
        while(curr!=None):
            size+=1
            curr=curr.next
        print(size)
        while size>=k:
            cur=pre.next
            nex=cur.next
            for i in range(k-1):
                cur.next=nex.next
                nex.next=pre.next
                pre.next=nex
                nex=cur.next
            pre=cur
            size-=k
        return temp.next
