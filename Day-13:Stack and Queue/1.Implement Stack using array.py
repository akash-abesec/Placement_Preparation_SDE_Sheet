# Problem :- https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-array

# Solution :- https://www.youtube.com/watch?v=tqQ5fTamIN4

#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        return self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.arr == []:
            return -1
        return self.arr.pop()
        
        
