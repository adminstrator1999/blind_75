from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = 0
        for num in nums:
            cur_max = max(num, cur_max + num)
            res = max(res, cur_max)
        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArray(nums))
