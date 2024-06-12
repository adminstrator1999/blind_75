class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res, l = 0, 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstringEasy(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        max_length = 0
        while l <= r and r < len(s):
            if s[r] in s[l: r]:
                max_length = max(max_length, r - l)
                l += 1
            else:
                r += 1
        max_length = max(max_length, r - l)
        return max_length


s = ""
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
