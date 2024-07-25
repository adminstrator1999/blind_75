import collections
from typing import List

# DFS here
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         visits = set()
#         ans = 0
#
#         def dfs(r, c):
#
#             if r not in range(ROWS) or c not in range(COLS) or (r, c) in visits or grid[r][c] != '1':
#                 return 0
#
#             visits.add((r, c))
#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)
#             return 1
#
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if grid[row][col] == '1':
#                     ans += dfs(row, col)
#         return ans


class Solution:
    # BFS solution
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visits.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visits and grid[r][c] == '1':
                        visits.add((r, c))
                        q.append((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visits:
                    bfs(row, col)
                    islands += 1
        return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
print(solution.numIslands(grid))
