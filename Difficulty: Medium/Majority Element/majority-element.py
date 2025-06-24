class Solution:
    def majorityElement(self, arr):
        #code here
        cand=arr[0]
        count=1
        for i in range(1,len(arr)):
            if count==0:
                cand=arr[i]
                count=1
            elif cand==arr[i]:
                count+=1
            else:
                count-=1
        count=0
        for i in range(len(arr)):
            if arr[i]==cand:
                count+=1
        if(count>len(arr)/2):
            return cand
        return -1
        
        