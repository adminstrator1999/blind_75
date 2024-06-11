from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)

        return longest

    def longestConsecutiveEasy(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums = sorted(nums)
        p1, longest, dub = 0, 0, 0
        print(nums)

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                dub += 1
                continue

            if nums[i] - nums[i - 1] != 1:
                longest = max(longest, i - p1 - dub)
                dub, p1 = 0, i
        longest = max(longest, i + 1 - p1 -dub)
        return longest


nums = [0,3,2,5,4,6,1,1]
s = Solution()
print(s.longestConsecutive(nums))
