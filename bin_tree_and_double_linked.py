"""
二叉树转换成双向链表
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def in_order(root):
    pre = TreeNode()
    head = TreeNode()
    if not root:
        return 
    if root.left:
        in_order(root.left)
    root.left = pre
    if pre:
        pre.right = root
    pre = root
    if not head:
        head = root
    in_order(root.right)
