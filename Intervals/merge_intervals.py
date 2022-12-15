# Time: O(n * log(n)) bc of sort
# Space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd: # need to merge 2 intervals
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
