class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit=0
        l=0
        r=1
        while r<len(prices):
            if(prices[l]<prices[r]):
                if(prices[r]-prices[l]>maxProfit):
                    maxProfit=prices[r]-prices[l]
            else:
                l=r
            r+=1
        return maxProfit