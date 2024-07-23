from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(i, j):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            return True

        def dfs(i, j, curr):
            if curr == len(word):
                return True
            if not is_valid(i, j) or board[i][j] != word[curr]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = dfs(i + 1, j, curr + 1) or dfs(i, j + 1, curr + 1) or dfs(i - 1, j, curr + 1) or dfs(i, j - 1,
                                                                                                         curr + 1)
            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
s = Solution()
print(s.exist(board, word))
