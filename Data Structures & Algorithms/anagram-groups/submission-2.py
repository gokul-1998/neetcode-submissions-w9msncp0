class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data={}
        for ana in strs:
            if tuple(sorted(ana)) not in data:
                data[tuple(sorted(ana))]=[ana]
            else:
                data[tuple(sorted(ana))].append(ana)
        return list(data.values())