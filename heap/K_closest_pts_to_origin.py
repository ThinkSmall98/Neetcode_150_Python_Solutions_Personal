# Time: O(k*log(n)), Space: O(n)
from heapq import heapify, heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            minHeap.append([dist, x, y])
        heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
