class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], len(s) + 1
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != len(s) + 1 else ""


    def check(self, counter_s, counter_t):
        for c in counter_t:
            if c not in counter_s or counter_s[c] < counter_t[c]:
                return False
        return True

    def minWindowBrute(self, s: str, t: str) -> str:
        counter_t = {}
        for c in t:
            counter_t[c] = 1 + counter_t.get(c, 0)

        counter_s = {}
        shortest = len(s) + 1
        shortest_s = ""
        l = 0
        for r in range(len(s)):
            counter_s[s[r]] = 1 + counter_s.get(s[r], 0)

            while self.check(counter_s, counter_t):
                counter_s[s[l]] -= 1
                if shortest > r - l + 1:
                    shortest = r - l + 1
                    shortest_s = s[l: r + 1]
                l += 1

        return shortest_s


s = "YZX"
t = "XYZ"
solution = Solution()
print(solution.minWindow(s, t))