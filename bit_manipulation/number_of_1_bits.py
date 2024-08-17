from typing import List


class Solution:

    def hammingWeight(self, n: int) -> int:
        s=format(n,"b")
        s1=str(s)
        return s1.count("1")

    # def hammingWeight(self, n: int) -> int:
    #     res = 0
    #     while n:
    #         n &= n - 1
    #         res += 1
    #     return res

    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n > 1:
    #         if n % 2 == 1:
    #             count += 1
    #         n = n // 2
    #     return count + 1

n = 2147483645
solution = Solution()
print(solution.hammingWeight(n))
