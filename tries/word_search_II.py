from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def add_word(self, word: str):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.isWord = True

    def remove_word(self, word: str):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1




class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visits = set(), set()

        def dfs(row, col, node, word):

            if row not in range(ROWS) or \
                    col not in range(COLS) or \
                    board[row][col] not in node.children or \
                    node.children[board[row][col]].refs < 1 or \
                    (row, col) in visits:
                return

            ch = board[row][col]
            word += ch
            node = node.children[ch]
            if node.isWord:
                node.isWord = False
                res.add(word)
                trie.remove_word(word)
            visits.add((row, col))

            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)

            visits.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, '')

        return list(res)


board = [["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]]
words = ["bat", "cat", "back", "backend", "stack"]

solution = Solution()
print(solution.findWords(board, words))
