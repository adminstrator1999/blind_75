class Solution:

    def longestPalindrome(self, s: str) -> str:
        # time O(n^2)
        length = len(s)
        res = ''
        res_len = 0

        def is_palindrome(l, r):
            nonlocal res
            nonlocal res_len
            while l >= 0 and r < length and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        for i in range(length):
            # odd length palindrome
            is_palindrome(i, i)
            # even length palindrome
            is_palindrome(i, i+1)
        return res

    # def longestPalindrome(self, s: str) -> str:
        # def is_palindrome(word):
        #     n = len(word)
        #     half = n // 2
        #     if n % 2 == 1:
        #         l, r = half, half
        #     else:
        #         l, r = half - 1, half
        #     while r < n:
        #         if word[l] != word[r]:
        #             return False
        #         r += 1
        #         l -= 1
        #     return True
        #
        # visits = set()
        # maximum, word = 0, ''
        # for right in range(len(s) + 1):
        #     for left in range(right):
        #         if (left, right) in visits or is_palindrome(word=s[left:right]):
        #             visits.add((left, right))
        #             if right - left > maximum:
        #                 maximum = right - left
        #                 word = s[left:right]
        # return word


    # def longestPalindrome(self, s: str) -> str:
    #     # brute force
    #     maximum = 0
    #     word = ''
    #     def is_palindrome(word):
    #         l, r = 0, len(word) - 1
    #         while l < r:
    #             if word[l] != word[r]:
    #                 return False
    #             l += 1
    #             r -= 1
    #         return True
    #
    #     for right in range(len(s) + 1):
    #         for left in range(right):
    #             if is_palindrome(word=s[left:right]):
    #                 if right - left > maximum:
    #                     maximum = right - left
    #                     word = s[left:right]
    #     return word


s = 'anona'
solution = Solution()
print(solution.longestPalindrome(s))
