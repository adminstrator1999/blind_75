def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if target < nums[left] or target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target > nums[right] or target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1
