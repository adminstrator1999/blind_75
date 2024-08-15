from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     def is_prefix(start, end, word):
    #         if s[start:end] != word:
    #             return False
    #         if end == len(s):
    #             return True
    #         for w in wordDict:
    #             if is_prefix(start=end, end=end+len(w), word=w):
    #                 return True
    #         return False
    #
    #     for w in wordDict:
    #         if is_prefix(0, len(w), w):
    #             return True
    #     return False


# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "applepenapple"
wordDict = ["apple","pen"]
solution = Solution()
print(solution.wordBreak(s, wordDict))
