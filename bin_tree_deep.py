"""
二叉树深度
"""

def get_bin_tree_deepth(root):
    if not root:
        return 0
    return 1 + max(
        get_bin_tree_deepth(root.left),
        get_bin_tree_deepth(root.right))
    