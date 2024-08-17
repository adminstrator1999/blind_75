from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum(range(n)) - sum(nums)
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.missingNumber(nums))
