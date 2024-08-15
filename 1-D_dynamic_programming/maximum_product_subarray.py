from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1
        for num in nums[1:]:
            tmp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(tmp, curr_max * num, num)
            res = max(res, curr_max)
        return res


nums = [1, 2, -3, 4]
s = Solution()
print(s.maxProduct(nums))
