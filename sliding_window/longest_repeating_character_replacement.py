class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(maxf, counter[s[r]])
            while r - l + 1 - maxf > k:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


s = "AAABABB"
k = 1
solution = Solution()
print(solution.characterReplacement(s, k))
