from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):

            # to eliminate duplicates
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                tree_sum = num + nums[l] + nums[r]
                if tree_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # to get rid of duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif tree_sum > 0:
                    r -= 1
                elif tree_sum < 0:
                    l += 1
        return res


