class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, nums):
        # code here
        mid=0
        low=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        