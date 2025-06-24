class Solution:
    def missingNum(self, arr):
        # code here
        sum_arr=sum(arr)
        n=len(arr)+1
        sum_n=(n*(n+1))//2
        return sum_n-sum_arr
        
