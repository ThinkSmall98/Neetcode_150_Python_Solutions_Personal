# Time: O(n * log(n)) where n = len(intervals)
# Space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(lastEnd, end)
        return res
