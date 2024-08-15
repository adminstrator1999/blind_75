class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     # tle
    #     visits = set()
    #
    #     def dfs(r, c):
    #         if (r, c) in visits or r not in range(m) or c not in range(n):
    #             return 0
    #         if r + 1 == m and c + 1 == n:
    #             return 1
    #         visits.add((r, c))
    #         res = dfs(r + 1, c) + dfs(r, c + 1)
    #         visits.remove((r, c))
    #         return res
    #     return dfs(0, 0)


m = 3
n = 7
solution = Solution()
print(solution.uniquePaths(m, n))
