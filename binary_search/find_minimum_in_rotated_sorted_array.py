from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        curr_min = float('inf')
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < curr_min:
                curr_min = nums[mid]

            if nums[mid] > nums[end]:
                # search right side
                start = mid + 1
            else:
                # search left side
                end = mid - 1

        return min(curr_min, nums[start])



    def findMinBrute(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start < end:
            if end - start == 1 or nums[start] < nums[end]:
                return min(nums[start], nums[end])
            if nums[start] > nums[end]:
                mid = start + (end - start) // 2
                if nums[start] > nums[mid]:
                    end = mid
                else:
                    start = mid


nums = [4, 5, 1, 2]
s = Solution()
print(s.findMin(nums))
