from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 0
        for i in range(len(str(n))):
            ans += 2 ** power * int(str(n)[i])
            power += 1
        return ans


n = '11111111111111111111111111111101'
solution = Solution()
print(solution.reverseBits(n))
