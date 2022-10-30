# Time: O(log(n)), Space: O(n)
from heapq import heapify, heappop, heappush

class MedianFinder:

    def __init__(self):
        # 2 heaps: small (max) & large (min)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        return ((self.small[0] * -1) + self.large[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
