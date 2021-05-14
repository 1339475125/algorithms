# -*- coding:utf-8 -*-
"""
最大值减去最小值小于或等于num的子数组数量
给定数组arr和整数num，共返回有多少个子数组满足如下情况
如果数组长度为N，请实现时间复杂度为O（N）的解法。
双端队列结构与解决“生成窗口最大值数组”问题中的双端队列结构含义基本一致
"""

qmin = [] #窗口内的最小值
qmax = [] #窗口内的最大值
L = 0
R = 0
res2 = 0
arr = [1, 4, 5, 2, 3, 6, 7, 8, 4, 5, 6]
num = 3
while L<len(arr):
    while R<len(arr):
        while len(qmin)!=0 and arr[qmin[-1]] >= arr[R]: #更新最小值
            qmin.pop()
        qmin.append(R)
        while len(qmax)!=0 and arr[qmax[-1]] <= arr[R]: 	#更新最大值
            qmax.pop()
        qmax.append(R)
        if arr[qmax[0]] - arr[qmin[0]] > num: #如果不满足了，break，R为X+1了，满足的有R-L个
            break
        R += 1
    print(qmax, qmin)
    res2  += R-L
    if qmin[0] == L:   #L要向右移动了，L位置的值要pop掉
        qmin.pop(0)
    if qmax[0] == L:
        qmax.pop(0)
    L += 1
print(res2)


