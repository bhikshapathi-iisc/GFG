'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        a=head
        b=head.next
        c=a
        d=b
        head=head.next.next
        while head and head.next :
            a.next=head
            b.next=head.next
            a=a.next
            b=b.next
            head=head.next.next
        if head:
            a.next=head
            a=a.next
        a.next=None
        b.next=None
        return [c,d]
        
            
        