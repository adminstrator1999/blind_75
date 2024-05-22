from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def hasDuplicate2(self, nums: List[int]) -> bool:
        original_numbers = set()
        for num in nums:
            if num in original_numbers:
                return True
            original_numbers.add(num)
        return False
