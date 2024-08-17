from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lr, lc = len(matrix[0]), len(matrix)
        columns, rows = set(), set()
        for i in range(lc):
            for j in range(lr):
                if matrix[i][j] == 0:
                    columns.add(j)
                    rows.add(i)

        for c in columns:
            for i in range(lc):
                matrix[i][c] = 0

        for r in rows:
            for i in range(lr):
                matrix[r][i] = 0


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution = Solution()
solution.setZeroes(matrix)
print(matrix)
