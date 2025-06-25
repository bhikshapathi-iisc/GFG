class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def countInv(self,arr, l,r):
        res=0
        if l<r:
            m=(l+r)//2
            res+=self.countInv(arr,l,m)
            res+=self.countInv(arr,m+1,r)
            
            res+=self.Mergecount(arr,l,m,r)
        return res
    
    def Mergecount(self,arr,l,m,r):
        n1=m-l+1
        n2=r-m
        left=arr[l:m+1]
        right=arr[m+1:r+1]
        res=0
        i=0
        j=0
        k=l
        while i<n1 and j<n2 :
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                res+=(n1-i)
                j+=1
            k+=1
        while i< n1:
            arr[k]=left[i]
            i+=1
            k+=1
        while j< n2:
            arr[k]=right[j]
            j+=1
            k+=1
        return res
    def inversionCount(self, arr):
        # Your Code Here
        return self.countInv(arr,0,len(arr)-1)

        
        