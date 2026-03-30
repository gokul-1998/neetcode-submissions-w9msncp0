from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        op=c.most_common(k)
        fin=[]
        for i in op:
            fin.append(i[0])
        return fin

