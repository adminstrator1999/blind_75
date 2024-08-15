class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        col, row = len(text2), len(text1)
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]


text1 = "abcde"
text2 = "ace"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))
