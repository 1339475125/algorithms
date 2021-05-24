"""
二叉树查找第k个节点
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.cnt = 0

def get_k_node(root, k, cnt=0):
    if not root or cnt >= k:
        return None
    value = root.val
    if root.left:
        get_k_node(root.left, k, cnt)
    cnt = cnt + 1
    if cnt == k:
        ret = root
    get_k_node(root.right, k, cnt)
    return ret


t1 = TreeNode(1)
t2 = TreeNode(2)  
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3
t2.left =  t4
t2.right = t5

print(get_k_node(t1, 3))