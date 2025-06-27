'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        f=head1
        s=head2
        c=0
        d=0
        while f is not None:
            c+=1
            f=f.next
        while s is not None:
            d+=1
            s=s.next
        f=head1
        s=head2
        if(c>d):
            dif=c-d
            while dif>0:
                f=f.next
                dif-=1
        else:
            dif=d-c
            while dif>0:
                s=s.next
                dif-=1
        while s is not None:
            if s==f:
                return s
            s=s.next
            f=f.next
        