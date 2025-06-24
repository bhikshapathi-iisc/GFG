#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        sum=0
        for i in range(len(arr)):
            sum^=arr[i]
        return sum
