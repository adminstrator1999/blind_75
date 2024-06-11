from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for ch in s:
                res += str(ord(ch))
                res += "+"
            res += "_"
        return res

    def decode(self, s: str) -> List[str]:
        p2, p3 = 0, 0
        res = []
        word = ""
        while p3 < len(s):
            if s[p3] == "_":
                res.append(word)
                p2 += 1
                word = ""
            if s[p3] == "+":
                word += chr(int(s[p2:p3]))
                p2 = p3 + 1
            p3 += 1
        return res

s = Solution()
print(s.encode(["", "ss", ""]))
print(s.decode("_"))
st = '_115+115+__'
print(st[5:8])
print(chr(97))