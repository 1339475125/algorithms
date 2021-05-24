"""
按照之字形打印二叉树
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 

class Solution:

    def print_bin_tree(self, root):
        res = []
        queue = []
        reverse = False
        if not root:
            return res
        queue.append(root)
        while queue:
            vals = [i.val for i in queue]
            if reverse:
                vals.reverse()
            reverse = not reverse
            res.append(vals)
            tmp_nodes = []
            for node in queue:
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)

            queue = tmp_nodes[:]
        return dict_values
