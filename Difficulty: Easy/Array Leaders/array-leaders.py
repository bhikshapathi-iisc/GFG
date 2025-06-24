class Solution:
    def leaders(self, arr):
        # code here
        res=[]
        max_v=arr[-1]
        res.append(max_v)
        for i in range(len(arr)-2,-1,-1):
            if max_v<=arr[i]:
                res.append(arr[i])
                max_v=arr[i]
        return res[::-1]