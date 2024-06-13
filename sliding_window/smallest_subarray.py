# geeks for geeks
"""
Given an array arr[] of integers and a number X,
the task is to find the smallest subarray with a sum greater than the given value.
"""


def find_smallest_subarray(arr, x):
    l = 0
    res = []
    curr_sum = arr[0]

    for r in range(1, len(arr)):
        curr_sum = curr_sum + arr[r]
        while curr_sum > x:
            res.append(arr[l: r + 1])
            curr_sum -= arr[l]
            l += 1
    return res


arr = [2, 4, 5, 3, 6, 8, 3]
x = 7
print(find_smallest_subarray(arr, x))
