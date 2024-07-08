def search(nums: [int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] > target or nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[right] < target or nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return -1


nums = [6, 7, 1, 2, 3, 4, 5]
target = 2
print(search(nums, target))