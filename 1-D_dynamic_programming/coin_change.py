from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # One brute force way very inefficient
    #
    #     ans = float('infinity')
    #
    #     def dfs(target, count):
    #         nonlocal ans
    #         if target < 0:
    #             return False
    #         if target == 0:
    #             ans = min(ans, count)
    #             return True
    #         for c in coins:
    #             dfs(target - c, count + 1)
    #     dfs(amount, 0)
    #     if ans == float('infinity'):
    #         return -1
    #     return ans


coins=[1,2,5]
amount=12

solution = Solution()
print(solution.coinChange(coins, amount))
