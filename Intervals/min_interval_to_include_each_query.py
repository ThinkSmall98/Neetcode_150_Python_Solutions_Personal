# Time: O(nlog(n) + qlog(q)) where n = len(intervals) & q = len(queries) bc of sort
# Space: O(n)
from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l,r = intervals[i]
                heappush(minHeap, (r - l + 1, r))
                i += 1
            while minHeap and q > minHeap[0][1]: # take top of heap & last val of interval
                heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
