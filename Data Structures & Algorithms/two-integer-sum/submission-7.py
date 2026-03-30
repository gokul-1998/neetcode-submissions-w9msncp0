class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for index,i in enumerate(nums):
            diff=target-i
            if diff in prev:
                return [prev[diff],index]
            prev[i]=index
           
        