from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        total = 0
        for num in nums:
            if total < 0:
                return False
            elif num > total:
                total = num
            total -= 1
        return True

    # def canJump(self, nums: List[int]) -> bool:
    #     length = len(nums) - 1
    #     before = length - 1
    #     while length > 0:
    #         if before < 0:
    #             return False
    #         while length <= before + nums[before]:
    #             length = before
    #             break
    #         before -= 1
    #     return length == 0


nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
solution = Solution()
print(solution.canJump(nums))
