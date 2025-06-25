#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code 
        n=len(nums)
        ans=[1]*n
        cur=1
        for i in range(n):
            ans[i]=cur
            cur*=nums[i]
        cur=1
        for i in range(n-1,-1,-1):
            ans[i]*=cur
            cur*=nums[i]
        return ans
            