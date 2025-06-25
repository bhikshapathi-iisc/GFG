#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        high=len(arr)-1
        low=0
        mid=0
        while low<=high:
            mid=(high+low)//2
            if arr[mid]==key:
                return mid
            if arr[low]<=arr[mid]:
                if key>=arr[low] and key<arr[mid]:
                    high=mid-1
                else :
                    low=mid+1
            else:
                if key>arr[mid] and key<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
                
        return -1