from typing import List, Optional

from trees.invert_binary_tree import TreeNode

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

pre = [1, 2, 4, 5, 3, 6]
ino = [4, 2, 5, 1, 3, 6]


def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def inOrderIterative(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        stack.pop()
        curr = curr.right

class Solution:
    """
    approach 1. I can determine head, i can use is_left, is_right functions to help me
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        head = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        left_side_inorder = inorder[:i]
        right_side_inorder = inorder[i+1:]
        left_side_preorder = preorder[1:i+1]
        right_side_preorder = preorder[i+1:]
        head.left = self.buildTree(left_side_preorder, left_side_inorder)
        head.right = self.buildTree(right_side_preorder, right_side_inorder)

        return head


