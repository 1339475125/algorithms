"""
树的子结构
"""

def has_sub_tree(root1, root2):
    if not root1 or not root2:
        return False
    return is_sub_tree(root1, root2) or has_sub_tree(root1.left, root2) or has_sub_tree(root1.right, root2)


def is_sub_tree(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.val != root2.val:
        return False
    return is_sub_tree(root1.left, root2.left) and is_sub_tree(root1.right, root2.right)