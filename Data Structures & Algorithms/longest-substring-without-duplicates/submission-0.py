class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=0
        result=0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            result = max(result,right-left+1)
        return result

    # create and empty set, left=0 and result=0
    # for char in range(len(s)):
        # while s[right] in 