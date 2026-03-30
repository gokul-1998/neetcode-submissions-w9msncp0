class Solution:
    def topKFrequent(self,nums, k: int)  :
        freq_dic=defaultdict(int)
        for i in nums:
            freq_dic[i]+=1
        res=list(freq_dic.items())
        sorted_tuples=sorted(res,key=lambda x:x[1],reverse=True)
        return [x[0] for x in sorted_tuples[:k]]