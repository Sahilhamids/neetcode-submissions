class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        n = len(prices)
        
        while i < n - 1:
            # 1. Find the valley: keep moving until prices stop decreasing
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            # 2. Find the peak: keep moving until prices stop increasing
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            # 3. Add the profit from this trend
            max_profit += peak - valley
            
        return max_profit