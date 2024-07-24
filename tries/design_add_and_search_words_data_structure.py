# class TrieNode:
#
#     def __init__(self):
#         self.children = [None] * 26
#         self.end = False
#
#
# class WordDictionary:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def addWord(self, word: str) -> None:
#         curr = self.root
#
#         for c in word:
#             i = ord(c) - ord('a')
#             if not curr.children[i]:
#                 curr.children[i] = TrieNode()
#             curr = curr.children[i]
#         curr.end = True
#
#     def search(self, word: str) -> bool:
#         def dfs(j, root):
#             curr = root
#
#             for index in range(j, len(word)):
#                 c = word[index]
#                 if c == '.':
#                     for node in curr.children:
#                         if node and dfs(index + 1, node):
#                             return True
#                     return False
#                 else:
#                     i = ord(c) - ord('a')
#                     if not curr.children[i]:
#                         return False
#                     curr = curr.children[i]
#             return curr and curr.end
#
#         return dfs(0, self.root)
#

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = ''

    def search(self, word: str) -> bool:

        def dfs(j, root):

            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for node in curr.values():
                        if node and dfs(i+1, node):
                            return True
                    return False

                else:
                    if c not in curr:
                        return False
                    curr = curr[c]
            return '*' in curr

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
["WordDictionary","addWord","complex","addWord","complication","search","c.mpl.x","search","complic.tion","search","...........","search","c....."]
obj = WordDictionary()
obj.addWord('complex')
obj.addWord('complication')
# param_1 = obj.search('c.mpl.x')
# param_2 = obj.search('complic.tion')
param_3 = obj.search('...........')
# param_4 = obj.search('c.....')
# print(param_1, param_2, param_3, param_4)
print(param_3)