# —*- coding:utf-8 -*-
"""
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
栈的特点：先进后出，实现功能入栈和出栈
设计两个栈，一个保存正常的栈，一个保存最小值
"""

class getMinStack1:

    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, newNum):
        # 判断stackMin是否为空
        if not self.stackMin:
            self.stackMin.append(newNum)
        elif newNum < self.getMin():
            self.stackMin.append(newNum)
        else:
            self.stackMin.append(self.getMin())
        self.stackData.append(newNum)
        return

    def pop(self):
        if not self.stackData:
            print("该栈为空")
            return
        self.stackData.pop()
        self.stackMin.pop()
        return

    def getMin(self):
        if not self.stackMin:
            print("该栈为空")
        value = self.stackMin[-1]
        return value

    
if __name__ == "__main__":
    stack = getMinStack1()
    import random
    for i in range(10):
        j = random.randint(1, 100)
        stack.push(j)
    print(stack.stackData, stack.stackMin) # ([81, 27, 61, 7, 57, 45, 29, 98, 95, 93], [81, 27, 27, 7, 7, 7, 7, 7, 7, 7])
    # stack.push(1)