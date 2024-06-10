from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            data[key] += [strs[i]]
        res = []
        for i in data.values():
            res.append(i)
        return res


    def groupAnagramsEasy(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in data:
                data[key] = [strs[i]]
            else:
                data[key].append(strs[i])
        res = []
        for i in data.values():
            res.append(i)
        return res

