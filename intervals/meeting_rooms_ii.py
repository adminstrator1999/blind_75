from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            start, end = i.start, i.end
            time.append((start, 1))
            time.append((end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

    # def minMeetingRooms(self, intervals: List[Interval]) -> int:
    #     start = sorted([i.start for i in intervals])
    #     end = sorted([i.end for i in intervals])
    #
    #     s, e = 0, 0
    #     res, count = 0, 0
    #
    #     while s < len(start):
    #         if start[s] < end[e]:
    #             s += 1
    #             count += 1
    #         else:
    #             e += 1
    #             count -= 1
    #         res = max(res, count)
    #     return res

    # def minMeetingRooms(self, intervals: List[Interval]) -> int:
    #     if not intervals:
    #         return 0
    #     intervals.sort(key=lambda x: x.start)
    #     days = set()
    #     days.add(intervals[0])
    #     for interval in intervals[1:]:
    #         found = False
    #         for day in days:
    #             if interval.start >= day.end:
    #                 if not found:
    #                     found = day
    #                 if found.end > day.end:
    #                     found = day
    #         if found:
    #             days.remove(found)
    #         days.add(interval)
    #     return len(days)


intervals = [(0, 40), (5, 10), (15, 20)]
solution = Solution()
print(solution.minMeetingRooms())
