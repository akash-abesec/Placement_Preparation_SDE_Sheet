
# ===================================== Doubly linked list ============================================= #
# Implementation of doubly linkedlist
class Node:
    def __int__(self, data):
        self.val = data
        self.next = None
        self.prev = None


# ---------------------- Traversal --------------------- #
# Simple traversal
def traversal(curr):
    while(curr != None):
        print(curr.val, end = " ")
        curr = curr.next

# Recursive Traversal
def RecTraversal(curr):
    if curr == None:
        return
    print(curr.val, end = " ")
    RecTraversal(curr.next)


# ----------------------- Insertion -------------------------#
# Insertion in the beginning of doubly linked list
def InsertBegin(curr, data):
    newNode = Node(data)
    if curr == None:
        return newNode
    newNode.next = curr
    curr.prev = newNode
    return newNode
