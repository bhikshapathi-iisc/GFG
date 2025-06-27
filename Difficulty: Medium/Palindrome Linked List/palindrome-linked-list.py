'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        if head is None or head.next is None:
            return True
        fast=head
        slow=head
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
        pre=None
        while slow is not None:
            temp=slow.next
            slow.next=pre
            pre=slow
            slow=temp
        left=head
        right=pre
        while right is not None:
            if left.data != right.data:
                return False
            left=left.next
            right=right.next
        return True
            
        