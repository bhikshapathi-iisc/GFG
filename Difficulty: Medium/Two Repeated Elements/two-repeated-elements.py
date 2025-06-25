#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, n, arr):
        #Your code here
        res=[1]*2
        j=0
        for i in range(n+2):
            cur=abs(arr[i])
            if arr[cur]<0:
                res[j]=cur
                j+=1
            arr[cur]*=-1
        return res
