from typing import Optional

from trees.invert_binary_tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # to solve this I can just use Inorder Traversal DFS because this is binary search tree
        ans = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans[k - 1]

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right



