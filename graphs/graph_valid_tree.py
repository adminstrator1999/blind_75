from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        pre_list = {i: [] for i in range(n)}

        for u, v in edges:
            pre_list[u].append(v)
            pre_list[v].append(u)

        visits = set()

        def dfs(node, prev):
            if node in visits:
                return False

            visits.add(node)
            for n in pre_list[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True

        return dfs(0, -1) and len(visits) == n


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# True

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# False

solution = Solution()
print(solution.validTree(n, edges))