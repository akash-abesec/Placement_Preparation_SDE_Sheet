#  problem :- https://leetcode.com/problems/delete-node-in-a-linked-list/

#  Solution :- https://www.youtube.com/watch?v=icnp4FJdZ_c&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=32


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next
