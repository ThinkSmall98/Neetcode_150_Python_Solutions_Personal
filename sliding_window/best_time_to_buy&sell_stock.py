class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                buy = prices[i]
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)
        return max_profit

    # Time: O(n) 
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return profit
