from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        sum = numbers[start] + numbers[end]

        while sum != target:
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            sum = numbers[start] + numbers[end]
        return [start, end]


numbers = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(numbers, target))
