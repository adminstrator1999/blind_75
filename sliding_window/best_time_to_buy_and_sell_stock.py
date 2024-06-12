from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0
        while l <= r < len(prices):
            if prices[r] - prices[l] >= 0:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
            else:
                l += 1
        return max_profit

    def maxProfitEasy(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)

        return res



prices = [2, 1, 2, 1, 0, 1, 2]
s = Solution()
print(s.maxProfit(prices))
