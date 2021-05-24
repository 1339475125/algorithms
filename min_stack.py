"""
包含min函数的栈
"""


class stack(object):

    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, data):
        self.data_stack.append(data)
        self.min_stack.append(
            data if not self.min_stack else min(self.min(), data))

    def pop(self):
        self.data_stack.pop()
        self.min_stack.pop()

    def min(self):
        return self.min_stack[-1]

    def top(self):
        return self.data_stack[-1]


if __name__ == "__main__":
    s = stack()
    s.push(10)
    s.push(11)
    s.push(8)
    s.push(7)
    print(s.top, s.min)
    print(s.data_stack, s.min_stack)
