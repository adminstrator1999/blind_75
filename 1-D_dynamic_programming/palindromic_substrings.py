class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        length = len(s)

        def count(l, r):
            c = 0
            while l >=0 and r < length and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        for i in range(length):
            # odd len palindrome substrings
            counter += count(i, i)
            # even len palindrome substrings
            counter += count(i, i+1)
        return counter