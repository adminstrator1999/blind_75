from typing import Optional

from trees.invert_binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),  self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return res