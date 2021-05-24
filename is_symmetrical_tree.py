"""
对称二叉树
如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


def is_symmetrical(root):
    if not root:
        return True
    return is_symmetrical_tree(root.left, root.right)


def is_symmetrical_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return is_symmetrical_tree(t1.left, t2.right) or is_symmetrical_tree(t1.right, t1.left)