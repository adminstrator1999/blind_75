class Solution:

    def numDecodings(self, s: str) -> int:
        last = 1
        curr = 1
        for i in range(len(s) - 1, - 1, -1):
            tmp = curr
            if s[i] == '0':
                curr = 0
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                curr += last
            last = tmp
        return curr

    # def numDecodings(self, s: str) -> int:
        # memo = {len(s): 1}
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == '0':
        #         memo[i] = 0
        #     else:
        #         memo[i] = memo[i + 1]
        #
        #     if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456"):
        #         memo[i] += memo[i + 2]
        #
        # return memo[0]

    # def numDecodings(self, s: str) -> int:
    #     memo = {len(s): 1}
    #
    #     def dfs(i):
    #         if i in memo:
    #             return memo[i]
    #         if s[i] == "0":
    #             return 0
    #
    #         res = dfs(i + 1)
    #         if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
    #             res += dfs(i+2)
    #         memo[i] = res
    #         return res
    #     return dfs(0)

s = '03'
solution = Solution()
print(solution.numDecodings(s))

