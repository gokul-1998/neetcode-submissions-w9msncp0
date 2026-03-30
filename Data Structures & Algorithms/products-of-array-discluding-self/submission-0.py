class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[]
        for index,x in enumerate(nums):
            prod=1
            for index2,y in enumerate(nums):
                if index!=index2:
                    prod*=y
            op.append(prod)
        return op