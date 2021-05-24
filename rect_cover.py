# -*- coding:utf-8 -*-
"""
矩形覆盖 用2*1的矩形去覆盖2*n的大矩形（青蛙跳台阶）
f(n) = 1 n=1
f(n) = 2 n=2
f(n) = f(n-1) +f(n-2)
"""


def react_cover(n):

    def react(n):
        if n <=2:
            return n
        return react(n-2) + react(n-1)

    for i in range(n):
        print(react(i))


def jump_floor(n):
    if(n<=2):
        return n
    pre2, pre1 = 1, 2
    result = 0
    for i in range(2, n):
        result = pre2 + pre1
        pre2 = pre1
        pre1 = result
        print(result)
    return result

if __name__ == "__main__":
    react_cover(10)
    jump_floor(10)
