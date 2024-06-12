# Time: O(n * log(n)) where n = len(intervals)
# Space: O(n)
from heapq import heappush, heappop
class Solution:
    # Approach: heap
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        q = [] # contains end times of meetings
        intervals.sort(key = lambda x: x[0])
        # add 1st meeting end time
        heappush(q, intervals[0][1])
        for meeting in intervals[1:]:
            # if earliest room to be free is available, assign that room to this meeting
            if q[0] <= meeting[0]:
                heappop(q)
            # if new room need to be added
            heappush(q, meeting[1])
        return len(q)


# Time: O(n * log(n)) where n = len(intervals)
# Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        s = e = 0
        res = count = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res

