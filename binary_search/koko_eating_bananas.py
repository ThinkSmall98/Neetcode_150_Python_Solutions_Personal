from math import ceil
class Solution:
    # Time: O(n * log(m)) where n = len(piles) & m = max(piles)
    # Space: O(1)
    # Min speed of eating will always be at least the average speed of eating bananas
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = ceil(sum(piles)/h), max(piles) 
        res = r
        while l <= r:
            m = l + ((r - l) // 2)
            hours = 0
            for p in piles:
                hours += ceil(p / m)
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
