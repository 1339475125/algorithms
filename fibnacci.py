# -*- coding:utf-8 -*-
"""
斐波那契函数
f(n) = 0
f(n) = 1
f(n) = f(n-1) + f(n-2) n >1
动态规划
"""

def fibonacci(n):

    def fn(i):
        if i <2:
            return 1
        else:
            return (fn(i-2)+fn(i-1))

    for i in range(n):
        print(fn(i))


if __name__ == "__main__":
    fibonacci(10)