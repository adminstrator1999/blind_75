from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visits = set()
        pre_map = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            pre_map[u].append(v)

        def dfs(crs):
            if crs in visits:
                return False

            if not pre_map[crs]:
                return True

            visits.add(crs)
            for c in pre_map[crs]:
                if not dfs(c):
                    return False

            visits.remove(crs)
            pre_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



numCourses = 2
prerequisites = [[1,0],[0,1]]

solution = Solution()
print(solution.canFinish(numCourses, prerequisites))
