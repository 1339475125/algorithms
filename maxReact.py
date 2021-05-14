# -*- coding:utf-8 -*-
"""
给定一个整型矩阵map， 其中的值只有0 和 1 两种， 求其中全是1 的所有矩形区域中， 最大的矩形区域为1的数量。
"""


def maxRecFromBotton(arr):
    if arr == None or len(arr) == 0:
        return 0
    stack = []
    n = len(arr)
    maxArea = 0
    leftFirstmin = [-1]*n
    rightFirstmin = [n]*n
    for i in range(n):
        samei = []
        while len(stack)!=0 and arr[i]<=arr[stack[-1]]:
            m = stack.pop()
            
            if arr[i]<arr[m]:
                rightFirstmin[m] = i
            else:
                samei.append(m)
        if len(stack) != 0:
            leftFirstmin[i] = stack[-1]
        while len(samei)!=0:
            stack.append(samei.pop())
        stack.append(i)
    for p in range(n):
        curArea = arr[p]*((rightFirstmin[p] - leftFirstmin[p]) -1)
        maxArea = max(curArea, maxArea)
    print(leftFirstmin)
    print(rightFirstmin)

    return maxArea

 
if __name__ == "__main__":
    arr = [[1,1,0,1],
        [1,1,1,1],
        [1,1,1,0],
        [1,1,1,1]]
    maxArea = 0
    height = [0]*len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            height[j] = 0 if(arr[i][j]==0) else height[j]+1
        # print(height)
        maxArea = max(maxRecFromBotton(height), maxArea)
    print(maxArea)