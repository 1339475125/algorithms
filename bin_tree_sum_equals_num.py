"""
二叉树中和为某一值的路径
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree_path(root, num, one_path, res):
    if not root:
        return res
    one_path.append(root.val)
    num = num - root.val
    if num==0 and not root.left and not root.right:
        res.append(one_path[:])
    elif num >0:
        get_tree_path(root.left, num, one_path, res)
        get_tree_path(root.right, num, one_path, res)
    one_path.pop()
    return res


t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(12)
t4 = TreeNode(4)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

one_path = []
res = []
print(get_tree_path(t1, 22, one_path, res))
