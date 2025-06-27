# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        temp=head
        while temp is not None:
            dum=Node(temp.data)
            dum.next=temp.next
            temp.next=dum
            temp=dum.next
        temp=head
        while temp is not None:
            if temp.random:
              temp.next.random=temp.random.next
            temp=temp.next.next
        res=head.next
        temp=head
        while temp:
            old=temp.next.next
            temp.next.next=old.next if old else None
            temp.next=old
            temp=old
            
        return res
            