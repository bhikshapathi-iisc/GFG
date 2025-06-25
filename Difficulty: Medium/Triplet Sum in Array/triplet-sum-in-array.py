#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()
        n=len(arr)
        for i in range(n):
            su=target-arr[i]
            j=i+1
            k=n-1
            while j<k:
                if arr[j]+arr[k]==su:
                    return True
                elif arr[j]+arr[k]>su:
                    k-=1
                else:
                    j+=1
        return False
                  