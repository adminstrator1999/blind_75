from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save top left
                top_left = matrix[top][l + i]

                # rotate from bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # rotate from bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # rotate from top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # rotate from top left to top right
                matrix[top + i][r] = top_left
            r -= 1
            l += 1

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     transposed = zip(*matrix)
    #     for i, row in enumerate(transposed):
    #         matrix[i] = reversed(row)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
solution = Solution()
solution.rotate(matrix)
print(matrix)
