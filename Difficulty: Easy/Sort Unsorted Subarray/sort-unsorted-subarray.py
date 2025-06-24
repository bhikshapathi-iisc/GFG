class Solution:
    def printUnsorted(self, arr):
        # Code here
        max_v=float('-inf')
        min_v=float('inf')
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                max_v=max(max_v,arr[i-1])
                min_v=min(min_v,arr[i])
        l=0
        r=len(arr)-1
        
        for i in range(len(arr)):
            if arr[i]>min_v:
                l=i
                break
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<max_v:
                r=i
                break
        return [l,r]