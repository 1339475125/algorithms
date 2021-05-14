# -*- coding:utf-8 -*-
# 用递归/非递归的方式实现树的前序、中序和后序遍历
# 先序遍历顺序为根、左、右；中序遍历顺序为左、根、右；后序遍历顺序为左、右、根。


# 创建树
class Tree:

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class BinTree:

    # 前序遍历树
    def pre_order_by_no_recursive(self, T):
        if not T:
          return
        stack = []
        result = []
        while T or len(stack)>0:
            if T:
                stack.append(T)
                result.append(T.root)
                T = T.left
            else:
                T = stack[-1]
                stack.pop()
                T = T.right
        return result

    def pre_order_by_recursive(self, T, result=[]):
        if not T:
            return result
        result.append(T.root)
        self.pre_order_by_recursive(T.left, result)
        self.pre_order_by_recursive(T.right, result)
        return result
        
    # 后序遍历树
    def post_order_no_recursive(self, T):
        result = []
        if not T:
            return result
        stack1 = []
        stack2 = []
        stack1.append(T)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            result.append(stack2.pop().root)
        return result

    def post_order_recursive(self, T, result=[]):
        if not T:
            return result
        self.post_order_recursive(T.left)
        self.post_order_recursive(T.right)
        result.append(T.root)
        return result

    # 中序遍历树
    def mid_order_non_recurisve(self, T):
        result = []
        if not T:
            return result 
        stack = []
        while T or len(stack) > 0:
            if T:
                stack.append(T)
                T = T.left
            else:
                T = stack.pop()
                result.append(T.root)
                T = T.right
        return result

    def mid_order_recurisve(self, T, result=[]):
        if not T:
            return result
        self.mid_order_recurisve(T.left)
        result.append(T.root)
        self.mid_order_recurisve(T.right)
        return result


if __name__ == "__main__":
    nodeTree = Tree(1, left=Tree(2,left=Tree(4, right=Tree(7))), right=Tree(3, left=Tree(5), right=Tree(6)))
    T = BinTree()
    # pre_no_result = T.pre_order_by_no_recursive(nodeTree)
    # print(pre_no_result)
    # pre_result = T.pre_order_by_recursive(nodeTree)
    # print(pre_result)

    # post_result = T.post_order_no_recursive(nodeTree)
    # print(post_result)

    # post_result = T.post_order_recursive(nodeTree)
    # print(post_result)
    # mid_result = T.mid_order_non_recurisve(nodeTree)
    # print(mid_result)

    mid_result = T.mid_order_recurisve(nodeTree)
    print(mid_result)
