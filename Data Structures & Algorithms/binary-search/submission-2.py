class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n<1:
            return -1
        left=0
        right=n-1# remember : the right is n-1
        while left<=right: # remember it should be less than or equal to
            mid=(left+right)//2
            print(left,right,mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1