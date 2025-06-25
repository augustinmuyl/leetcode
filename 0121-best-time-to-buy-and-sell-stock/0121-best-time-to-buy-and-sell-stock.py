class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        maxval = 0

        for i in prices:
            if i < buy:
                buy = i
                sell = 0
            elif i > sell:
                sell = i
            maxval = max(maxval, sell - buy)
        
        return maxval
        