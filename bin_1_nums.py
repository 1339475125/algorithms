# -*- coding:utf-8 -*-
"""
二进制中1的个数
n&(n-1) 位运算可以将 n 的位级表示中最低的那一位 1 设置为 0。不断将 1 设置为 0，直到 n 为 0。时间复杂度：O(M)，其中 M 表示 1 的个数。
"""

def numer_of_1(n):
    cnt = 0
    while n!=0:
        cnt = cnt + 1
        n = (n-1) & n
    return cnt



if __name__ == "__main__":
    n = 22
    print(numer_of_1(n))