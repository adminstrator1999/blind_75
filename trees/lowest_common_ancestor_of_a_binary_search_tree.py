from trees.invert_binary_tree import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val < p.val and root.val < q.val:
            # need to search only right nodes
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            # need to search only left nodes
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val >= root.val >= q.val or p.val <= root.val <= q.val:
            # we found the lowest one
            return root
