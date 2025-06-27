'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        temp=head
        for i in range(k-1):
            if temp.next is None:
                return -1
            temp=temp.next
        while temp.next!=None:
            temp=temp.next
            head=head.next
        return head.data
            
            