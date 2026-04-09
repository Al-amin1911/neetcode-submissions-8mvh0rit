class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_gain = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            if prices[i] > min_price:
                profit = prices[i] - min_price
                max_gain = max(max_gain, profit)
        
        return max_gain


        