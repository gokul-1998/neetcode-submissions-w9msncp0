class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        response=defaultdict(list)
        for i in strs:
            data="".join(sorted(i))
            response[data].append(i)
        return list(response.values())
