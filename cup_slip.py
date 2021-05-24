# -*- coding:utf-8 -*-
"""
拆绳子
动态规划
"""
import math


# 贪婪算法
def get_max_cup(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    times_of_3 = int(n / 3)
    if (n-times_of_3*3 == 1):
        times_of_3 -= 1
    times_of_2 = int((n - times_of_3 * 3) / 2)
    return int(math.pow(3, times_of_3)) * int(math.pow(2, times_of_2))
    
def dfs_max_cup_nums(n):
    # 动态规划
    dp = [0] * (n+1)
    dp[1] =1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], max(j*(i-j), dp[j]*(i-j)))          
    return dp[n]


if __name__ == "__main__":
    print(get_max_cup(10))
    print(dfs_max_cup_nums(10))