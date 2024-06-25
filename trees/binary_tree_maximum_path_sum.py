from typing import Optional

from trees.invert_binary_tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(root):
            nonlocal result
            if not root: return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            result = max(left_max + right_max + root.val, result)
            return max(left_max, right_max) + root.val

        dfs(root)
        return result

