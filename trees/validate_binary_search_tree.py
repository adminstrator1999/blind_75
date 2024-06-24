from typing import Optional

from trees.invert_binary_tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))
