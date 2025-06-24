class Solution:
    def missingNum(self, arr):
        # code here
        # sum_arr=sum(arr)
        # n=len(arr)+1
        # sum_n=(n*(n+1))//2
        # return sum_n-sum_arr
        sum=0
        n=len(arr)+1
        for i in range(1,n):
         sum^=i^arr[i-1]
        sum^=n
        return sum
         
        
