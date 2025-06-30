'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        #Your code here
        def merge(a,b):
            dummy=Node(0)
            temp=dummy
            while a and b:
                if a.data<b.data:
                    temp.bottom=a
                    a=a.bottom
                else:
                    temp.bottom=b
                    b=b.bottom
                temp=temp.bottom
            if a is not None:
                temp.bottom=a
            if b is not None:
                temp.bottom=b
            return dummy.bottom
                
        if root is None or root.next is None:
            return root
        root.next=self.flatten(root.next)
        root=merge(root,root.next)
        return root
        