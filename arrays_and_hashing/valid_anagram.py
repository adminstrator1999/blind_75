class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
    def is_anagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}

        for i in s:
            if i in counter_s:
                counter_s[i] += 1
            else:
                counter_s[i] = 1

        for i in t:
            if i in counter_t:
                counter_t[i] += 1
            else:
                counter_t[i] = 1

        for i in counter_s:
            if counter_s[i] != counter_t[i]:
                return False
        return True

    def is_anagram_cleaned(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s, counter_t = {}, {}

        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        return counter_s == counter_t
