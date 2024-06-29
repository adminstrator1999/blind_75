"""
**Imagine you have a collection of integers in a list, along with two fixed integers: limit and divisor.
You need to determine the quantity of unique contiguous sublists,
which contain at most "limit" elements that are divisible by "divisor".

Two sublists, list1 and list2, are recognized as independent if:

They contain a different quantity of elements, or
There’s at least a single position, i, where list1[i] isn’t equivalent to list2[i].
A sublist is identified as an uninterrupted sequence of elements in a larger list.

Example 1:
Input: list = [6, 9, 9, 6, 6], limit = 3, divisor = 3
Output: 9
Explanation:
Every element in the list is divisible by the divisor = 3. As per our task, we can only have a maximum of
"limit" = 3 elements divisible by 3, within any sublist. The 9 unique sublists which satisfy
these conditions are: [6], [6, 9], [6, 9, 9], [9], [9, 9], [9, 9, 6], [9, 6], [9, 6, 6], [6].
Each sublist is unique and has at most "limit" = 3 elements divisible by 3.

Example 2:
Input: list = [5, 10, 15, 20], limit = 4, divisor = 5
Output: 10
Explanation:
Every element in the list is divisible by the divisor = 5. Any sublist will satisfy the condition of
containing at most "limit" = 4 elements divisible by 5.
Because of this, there are 10 sublists that fulfill the conditions.

Constraints:

The length of the list is between 1 and 200, inclusive.
The elements of the list and the divisor are between 1 and 200, inclusive.
The limit is less than or equal to the length of the list."""


def is_divisible(nums, divisor):
    for num in nums:
        if num % divisor == 0:
            return True
    return False


def limited_divisible_sublist_problem(nums: [int], limit: int, divisor: int):
    # this is false
    hash_set = set()

    left, right, count = 0, 1, 0
    while left < len(nums):
        while right - left <= limit:
            sub_list = nums[left: right]
            if str(sub_list) not in hash_set and is_divisible(sub_list, divisor):
                count += 1
                hash_set.add(str(sub_list))
            right += 1
        left += 1
        right = left + 1
    return count


def count_unique_sublist(nums: [int], limit: int, divisor: int):
    unique_sublists = set()
    left, num_divisible = 0, 0

    for right in range(len(nums)):

        # to check if number is divisible by divisor
        if nums[right] % divisor == 0:
            num_divisible += 1

        # need to check if number of divisible elements are not bigger than the limit
        while num_divisible > limit:
            if nums[left] % divisor == 0:
                num_divisible -= 1
            left += 1

        # need to update the count of unique sublists till it reaches to right pointer
        for tmp in range(left, right + 1):
            unique_sublists.add(tuple(nums[tmp: right + 1]))

    return len(unique_sublists)


list = [2, 3, 3, 2, 2]
limit = 2
divisor = 2
print(count_unique_sublist(list, limit, divisor))
