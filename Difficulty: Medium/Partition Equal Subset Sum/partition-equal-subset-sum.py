class Solution:

    def check(self,nums,n,asum,memo):
        if asum==0:
            return True
        if n==0:
            return False
        if (n,asum) in memo:
            return memo[(n,asum)]
        if nums[n-1]>asum:
            memo[(n,asum)]= self.check(nums,n-1,asum,memo)
        else:
            memo[(n,asum)]= self.check(nums,n-1,asum,memo) or self.check(nums,n-1,asum-nums[n-1],memo)
        return memo[(n,asum)]
    def equalPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        asum=sum(nums)
        if asum%2!=0:
            return False
        return self.check(nums,len(nums),asum//2,{})