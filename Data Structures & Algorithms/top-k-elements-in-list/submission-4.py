class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        
        buckets=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        
        res=[]
        for count in range(len(nums),0,-1):
            res.extend(buckets[count])
            if len(res)>=k:
                return res[:k]