from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        #Plan
        dp = [1] * len(nums) + 1
        """
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return dp


nums = [10, 9, 2, 5, 3, 7, 101, 18]
solution = Solution()
print(solution.lengthOfLIS(nums))
