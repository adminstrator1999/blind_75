from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # def rob(self, nums: List[int]) -> int:
    #     # solved using array and iterative
    #     arr = [0] * len(nums)
    #     arr[0:2] = nums[0], max(nums[0:2])
    #     for i in range(2, len(nums)):
    #         arr[i] = max(nums[i] + arr[i-2], arr[i-1])
    #     return arr[-1]

    # def rob(self, nums: List[int]) -> int:
    #     # recursive & memoization
    #     n = len(nums)
    #
    #     def dp(n, memo=None):
    #         if memo is None:
    #             memo = {}
    #         if n in memo:
    #             return memo[n]
    #         if n <= 2:
    #             return max(nums[:n])
    #         memo[n] = max(nums[n - 1] + dp(n - 2), dp(n - 1))
    #         return memo[n]
    #
    #     return dp(n)


nums = [10, 7, 9, 3, 1]
nums=[5,1,2,10,6,2,7,9,3,1]
nums = [2, 1]
# Output: 12
solution = Solution()
print(solution.rob(nums))
