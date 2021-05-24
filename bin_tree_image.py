"""
二叉树镜像
"""

def mirror(root):
    if not root:
        return root
    swap(root)
    mirror(root.left)
    mirror(root.right)
    return root

def swap(root):
    root.left, root.right = root.right, root.left