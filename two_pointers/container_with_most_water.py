from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_store = 0
        while l < r:
            max_store = max((r - l) * min(heights[l], heights[r]), max_store)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return max_store


height = [1, 7, 2, 5, 4, 7, 3, 6]
s = Solution()
print(s.maxArea(height))
