#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        temp=[0]*n
        d=d%n
        for i in range(len(arr)):
            temp[(n-d+i)%n]=arr[i]
        for i in range(len(arr)):
            arr[i]=temp[i]
        return arr