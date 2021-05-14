# —*- coding:utf-8 -*-
"""
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
栈的特点：先进后出，实现功能入栈和出栈
设计两个栈，一个保存正常的栈，一个保存最小值
"""

class getMinStack:

    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self,num):
        if not self.stackMin:
            self.stackMin.append(num)
        elif num <= self.getMin():
            self.stackMin.append(num)
        self.stackData.append(num)

    def pop(self):
        if not self.stackData:
            return "Your stack is empty."
        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value

    def getMin(self):
        if not self.stackMin:
            return "Your stack is empty."
        return self.stackMin[-1]

if __name__ == "__main__":
    stack = getMinStack()
    import random
    for i in range(10):
        j = random.randint(1, 100)
        stack.push(j)
    print(stack.stackData, stack.stackMin) # ([43, 69, 17, 86, 68, 8, 12, 22, 65, 61], [43, 17, 8])
    # stack.push(1)