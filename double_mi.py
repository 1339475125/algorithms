# -*- coding:utf-8 -*-
"""
数值的整数次方
double 浮点类型的 int 幂次方
用分治也就是动态规划的方式
x(n) = x(n/2) * x(n/2)   n%2=0
x(n) = x * (x(n/2) * x(n/2)) n%2=1
通过递归求解
O(log(n))
"""


def power(x, n):
    # 是否为负数
    is_negative = False
    if(n < 0):
        n = -n
        is_negative = True
    res = pow(x, n)
    return 1/res if is_negative else res


def pow(x, n):
    if(n==0):
        return 1
    if(n==1):
        return x
    res = pow(x, int(n/2))
    res = res * res
    if n %2:
        res = res * x
    return res
    

if __name__ == "__main__":
    x = 3.1214141
    n = 10
    print(power(x, n))





