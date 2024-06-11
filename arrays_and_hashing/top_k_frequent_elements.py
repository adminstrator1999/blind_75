from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, f in counter.items():
            freq[f].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            if freq[i] and k:
                res += freq[i]
                k -= len(freq[i])
        return res


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))
