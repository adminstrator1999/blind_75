from typing import List


class Solution:
    def getProduct(self, nums):
        product = 1
        for num in nums:
            product *= num
        return product
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def productExceptSelfEasy(self, nums: List[int]) -> List[int]:
        product = self.getProduct(nums)
        result = []
        for num in nums:
            if num == 0:
                new_nums = nums.copy()
                new_nums.remove(0)
                product_new = self.getProduct(new_nums)
                result.append(product_new)
                continue
            result.append(product // num)

        return result


nums = [1, 2, 4, 6, 0]
s = Solution()
answer = s.productExceptSelfEasy(nums)
print(answer)
