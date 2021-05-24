"""
二叉树后序遍历 左右根
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bin_tree_houxu(root):
    if not root:
        return None
    bin_tree_houxu(root.left)
    bin_tree_houxu(root.right)
    print(root.val)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
bin_tree_houxu(t1)