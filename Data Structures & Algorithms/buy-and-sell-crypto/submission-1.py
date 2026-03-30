class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right,maxprofit=0,1,0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxprofit=max(maxprofit,profit)
            else:
                left=right
            right+=1
        return maxprofit


        # set left=0, and right =1 because we compare the diff of left and right, 
        # also set maxprofit=0
        # while right<len(prices) # need to iterate till the end of the prices
        # if left price is less than right prices
            # profit=diff of right and left
            # maxprofit = max(maxprofit,profit)
        # else
            # left=right
        # right+=1
        # return maxprofit