# Time: O(n * log(n))
# Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            prev_interval = intervals[i - 1]
            curr_interval = intervals[i]
            if prev_interval[1] > curr_interval[0]:
                return False
        return True
# Take prev & curr intervals and check if last val of prev interval is greater than 1st val of curr interval
