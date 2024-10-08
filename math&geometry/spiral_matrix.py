from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # add top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # add right col
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            # add bottom row
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # add left row
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans


matrix = [[1, 2, 3]]

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]]
solution = Solution()
print(solution.spiralOrder(matrix))
# print(matrix[0:3])
