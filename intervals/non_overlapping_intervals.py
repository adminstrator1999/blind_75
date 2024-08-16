from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda x: x[0])
    #     ans = 0
    #     last = intervals[0]
    #     for interval in intervals[1:]:
    #         if interval[0] < last[1]:
    #             if interval[1] < last[1]:
    #                 last = interval
    #             ans += 1
    #         else:
    #             last = interval
    #     return ans

    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda x: x[1])
    #     ans = 0
    #     last = intervals[0]
    #     for interval in intervals[1:]:
    #         if interval[0] < last[1]:
    #             ans += 1
    #         else:
    #             last = interval
    #     return ans


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
solution = Solution()
print(solution.eraseOverlapIntervals(intervals))
