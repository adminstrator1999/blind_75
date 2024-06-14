from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid

            if nums[start] <= nums[mid]:
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
target = 10
s = Solution()
print(s.search(nums, target))
