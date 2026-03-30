class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1


        while low<high:
            if nums[low]<nums[high]: # [2,3,4,5,1](X) ,[1,2,3,4,5], [3,4,5,1,2](X), (4,5,1,2,3), (5,1,2,3,4)
                return nums[low]

            mid=(low+high)//2
            # if mid>high means left part is sorted => low = mid+1 # this means that the min is in the right part
            if nums[mid]>nums[high]:# [3,4,5,1,2] or [2,3,4,5,1] 
                low=mid+1
            else:#[5,1,2,3,4] this means that the min is in the left part
                high=mid
        return nums[low]
            # if mid <= high means right part is sorted.,  => 


# [5,1,2,3,4]