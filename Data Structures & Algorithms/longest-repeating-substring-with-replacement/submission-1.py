class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0

        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1)- max(count.values())>k:
                count[s[l]]-=1
                l+=1 

            res= max(res,r-l+1)
        return res
        # set count,res,l as 0, and use for loop to iterate over s:
         # add r to count
         # case  when [len(substring)-max]max allowed replacements will be the diff,>k
          # reduce one from count of l
          # and incremente count of l
           # return max(result,r-l+1)