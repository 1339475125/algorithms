# -*- coding:utf-8 -*-
"""
变态跳台阶，青蛙可以跳一级也可以跳两阶，也可以跳n阶，属于动态规划
f(n) = f(n-1)+ f(n-2) + ...+f(0)瑟吉欧一个等比数列
动态规划
"""

def jump_floor(n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            dp[i] += dp[j]
        print(dp[i])
    return dp[n-1]
    

if __name__ == "__main__":
    jump_floor(10)