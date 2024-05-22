from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def hasDuplicate2(self, nums: List[int]) -> bool:
        original_numbers = set()
        for num in nums:
            if num not in original_numbers:
                original_numbers.add(num)
            else:
                return True
        return False
