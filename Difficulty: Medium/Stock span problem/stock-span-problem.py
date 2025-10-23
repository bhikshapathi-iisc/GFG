class Solution:
    def calculateSpan(self, arr):
        # code here
        n=len(arr)
        stk=[]
        res=[0]*n
        for i in range(n):
            while  stk and arr[stk[-1]]<=arr[i]:
                stk.pop()
            if not stk:
                res[i]=i+1
            else:
                res[i]=i-stk[-1]
            stk.append(i)
        return res
            
        
        