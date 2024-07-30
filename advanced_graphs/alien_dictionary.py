from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {char: set() for word in words for char in word}

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])

        visits = {}
        res = []
        def dfs(char):
            if char in visits:
                return visits[char]

            visits[char] = True

            for neigh_char in adj_list[char]:
                if dfs(neigh_char):
                    return True

            visits[char] = False
            res.append(char)

        for ch in adj_list:
            if dfs(ch):
                return ""

        res.reverse()
        return "".join(res)


words = ["hrn", "hrf", "er", "enn", "rfnn"]
solution = Solution()
print(solution.foreignDictionary(words))
