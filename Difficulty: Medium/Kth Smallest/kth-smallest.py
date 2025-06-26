#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        def find( left , right , k):
            if left==right:
                return arr[left]
            index=random.randint(left,right)
            index= partion(left,right,index)
            if k==index:
                return arr[k]
            elif k<index:
                return find(left,index-1,k)
            else:
                return find(index+1,right,k)
        def partion(left,right,index):
            pivot=arr[index]
            arr[index],arr[right]=arr[right],arr[index]
            i=left
            for j in range(left,right):
                if arr[j]<pivot:
                    arr[i], arr[j]= arr[j], arr[i]
                    i+=1
            arr[i], arr[right]= arr[right], arr[i]
            return i
        return find(0,len(arr)-1,k-1)