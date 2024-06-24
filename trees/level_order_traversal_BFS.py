from collections import deque

from trees.invert_binary_tree import TreeNode


def bfs(root: TreeNode):
    if not root:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
