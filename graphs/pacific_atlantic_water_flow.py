from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(row, col, visits, prev_height):

            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                heights[row][col] < prev_height or
                (row, col) in visits
            ):
                return
            visits.add((row, col))

            dfs(row - 1, col, visits, heights[row][col])
            dfs(row, col - 1, visits, heights[row][col])
            dfs(row + 1, col, visits, heights[row][col])
            dfs(row, col + 1, visits, heights[row][col])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res


# heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
heights = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]
# [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
solution = Solution()
print(solution.pacificAtlantic(heights))
