"""
从上向下打印二叉树
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def print_bin_tree(self, root):

        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            node = queue.pop(0)
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res