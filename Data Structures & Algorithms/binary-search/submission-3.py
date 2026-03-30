class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find mid element
        # target>mid -> search in right, else in left
        # if mid = targe: found answer
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+(end-start)//2) #might be possibe that start + end exceed the range of int
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                return mid
        return -1