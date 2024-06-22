def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left = left[1:]
        else:
            sorted_list.append(right[0])
            right = right[1:]

    if not left:
        sorted_list += right
    else:
        sorted_list += left
    return sorted_list


def merge_sort(nums):
    # base case
    if len(nums) == 1:
        return nums

    left = merge_sort(nums[0: len(nums)//2])
    right = merge_sort(nums[len(nums)//2:])
    res = merge(left, right)
    return res

