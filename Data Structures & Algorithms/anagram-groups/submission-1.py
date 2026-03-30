class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data={}
        for i in strs:
            if tuple(sorted(i)) not in data:
                data[tuple(sorted(i))]=[i]
            else:
                data[tuple(sorted(i))].append(i)
        return list(data.values())