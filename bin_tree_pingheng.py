"""
平衡二叉树
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bin_tree_is_ph(root, is_balance=True):
    if not root or not is_balance:
        return 0
    left = bin_tree_is_ph(root.left, is_balance)
    right = bin_tree_is_ph(root.right, is_balance)
    if abs(left - right) > 1:
        is_balance = False
    print(is_balance)
    return  1+ max(left, right)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t4.left = t6
t4.right = t7

print(bin_tree_is_ph(t1))

