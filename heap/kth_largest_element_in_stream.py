# Time: O(N*log(N) + M*log(k)) where N = len of nums & M = # of calls to add() 
# 1st half: constructor, 2nd half: add()
# Space: O(N)

from heapq import heapify, heappop, heappush
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k: # Get rid of smallest values if len(heap) > k
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
