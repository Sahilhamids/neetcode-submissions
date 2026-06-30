class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r=0,1
        max_profit=0

        while r < len(prices):
            #check if we can make profit

            if prices[l]  < prices[r]:
                current = prices[r]-prices[l]
                max_profit = max(max_profit, current)
            else:
                l=r
            r+=1
        return max_profit


             

        