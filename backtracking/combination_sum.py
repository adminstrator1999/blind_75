from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(i, target, res):
            if target > 0:
                res.append(nums[i])
            if target == 0:
                res.append(nums[i])
                ans.append(res)
                return
            if target < 0:
                return
            for j in range(i, len(nums)):
                helper(j, target - nums[j], res.copy())

        for i in range(len(nums)):
            helper(i, target - nums[i], [])
        return ans

    def combinationSumBad(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(i, target, res):
            if target == 0:
                ans.append(res.copy())
                return
            if target < 0:
                return
            for j in range(i, len(nums)):
                res.append(nums[j])
                helper(j, target - nums[j], res)
                if res:
                    res.pop()
        for i in range(len(nums)):
            helper(i, target - nums[i], [nums[i]])
        return ans

    def combinationSumNew(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res


nums = [2,5,6,9]
target = 9
s = Solution()
print(s.combinationSumBad(nums, target))
