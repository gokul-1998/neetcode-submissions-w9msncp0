class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))# set to remove duplicates,
        max_so_far=0
        count=0
        print(nums)
        if not nums:
            return 0
        for i in range(len(nums)-1):
            print(nums[i],nums[i+1],count,max_so_far)
            if nums[i]+1==nums[i+1]:
                count+=1
                if max_so_far<count:
                    max_so_far=count
            else:
                count=0
        return max_so_far+1

            