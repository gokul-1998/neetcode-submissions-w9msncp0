class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sett=set(numbers)
        dic={}
        for index,u in enumerate(numbers):
            dic[u]=index
        for i in numbers:
            if target-i in dic:
                return [dic[i]+1,dic[target-i]+1]
        