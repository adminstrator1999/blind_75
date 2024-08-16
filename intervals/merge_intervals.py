from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            before = res[-1]
            if before[1] < interval[0]:
                res.append(interval)
            else:
                before[1] = max(before[1], interval[1])
        return res

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
solution = Solution()
print(solution.merge(intervals))
