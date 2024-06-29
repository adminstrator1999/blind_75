from collections import deque

from trees.invert_binary_tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''

        def dfs(root):
            nonlocal res
            if not root:
                res += '*#None'
            else:
                res += str(len(str(root.val))) + '#' + str(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper():
            nonlocal data
            if data[0] == "*":
                data = data[6:]
                return None
            for i in range(len(data)):
                if data[i] == '#':
                    steps = int(data[0: i])
                    val = int(data[i + 1: i + 1 + steps])
                    node = TreeNode(val)
                    data = data[i + 1 + steps:]
                    node.left = helper()
                    node.right = helper()
                    return node

        node = helper()
        return node