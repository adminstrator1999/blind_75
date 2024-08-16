from typing import List

"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval.start >= prev.end:
                prev = interval
            else:
                return False
        return True


intervals = [(0, 30), (5, 10), (15, 20)]
solution = Solution()
print(solution.canAttendMeetings(intervals))
