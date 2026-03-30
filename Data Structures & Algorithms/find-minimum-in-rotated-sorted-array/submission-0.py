class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            if nums[low]<nums[high]: # [2,3,4,5,1] or [2,3,4,5,1]
                return nums[low]

            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
            # if mid>high means left part is sorted => low = mid+1
            # if mid <= high means right part is sorted.,  => 


# [5,1,2,3,4]