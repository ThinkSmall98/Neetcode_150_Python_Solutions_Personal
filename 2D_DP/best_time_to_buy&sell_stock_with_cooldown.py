# Time: O(N) where N = len(prices)
# Space: O(1) 

class Solution(object):
    def maxProfit(self, prices):
        reset, hold, sold = 0, float('-inf'), float('-inf')
        for price in prices:
            reset, hold, sold = max(sold, reset), max(hold, reset - price), hold + price
