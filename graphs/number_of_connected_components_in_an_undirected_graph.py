from typing import List


class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x: int) -> int:
        y = self.f.get(x, x)

        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x: int, y: int):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()

        for u, v in edges:
            dsu.union(u, v)

        return len(set(dsu.findParent(x) for x in range(n)))


# class Solution:
#
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         # Union find algorithm
#         parents = [i for i in range(n)]
#         ranks = [1] * n
#
#         def find(node):
#             res = node
#
#             while res != parents[res]:
#                 # to optimize
#                 parents[res] = parents[parents[res]]
#                 res = parents[res]
#
#             return res
#
#         def union(node1, node2):
#             p1, p2 = find(node1), find(node2)
#
#             if p1 == p2:
#                 return 0
#
#             if ranks[p1] > ranks[p2]:
#                 parents[p2] = p1
#                 ranks[p1] += ranks[p2]
#             else:
#                 parents[p1] = p2
#                 ranks[p2] += ranks[p1]
#             return 1
#
#         ans = n
#         for u, v in edges:
#             ans -= union(u, v)
#
#         return ans
#
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         adj_list = {i: [] for i in range(n)}
#
#         for u, v in edges:
#             adj_list[u].append(v)
#             adj_list[v].append(u)
#
#         visits = set()
#
#         def dfs(node, prev):
#             if node in visits:
#                 return
#             visits.add(node)
#             for i in adj_list[node]:
#                 if i == prev:
#                     continue
#                 dfs(i, node)
#         ans = 0
#         for i in range(n):
#             if i not in visits:
#                 dfs(i, -1)
#                 ans += 1
#         return ans

# Input:
n=3
edges=[[0,1], [0,2]]

# Output: 1

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output: 2
solution = Solution()
print(solution.countComponents(n, edges))