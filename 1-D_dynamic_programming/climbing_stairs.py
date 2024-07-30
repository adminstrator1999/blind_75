class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # recursive and memoization
        if n in memo:
            return memo[n]
        if n < 3:
            return n
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]

    # def climbStairs(self, n: int) -> int:
    #     # bottom up memory O(n)
    #     arr = [1] * (n + 1)
    #     for i in range(n - 2, -1, -1):
    #         arr[i] = arr[i+1] + arr[i+2]
    #     return arr[0]

    # def climbStairs(self, n: int) -> int:
    #     # bottom up memory O(1)
    #     one, two = 1, 1
    #     for i in range(n-1):
    #         temp = one
    #         one += two
    #         two = temp
    #     return one


n = 5
solution = Solution()
print(solution.climbStairs(n))

