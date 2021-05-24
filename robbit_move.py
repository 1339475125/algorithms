# -*- coding:utf-8 -*-
"""
机器人的运动范围
使用深度优先搜索（Depth First Search，DFS）方法进行求解。回溯是深度优先搜索的一种特例，它在一次搜索过程中需要设置一些本次搜索过程的局部状态，并在本次搜索结束之后清除状态。而普通的深度优先搜索并不需要使用这些局部状态，虽然还是有可能设置一些全局状态。
""" 


def moving(m,n,i,j,threshold):
    global vector
    global sum
    if i>=0 and i<m and j>=0 and j<n and getsum(i)+getsum(j)<threshold and vector[i*n+j]==0 :
        sum +=1
        vector[i*n+j]=1
        moving(m,n,i-1,j,threshold)
        moving(m,n,i+1,j,threshold)
        moving(m,n,i,j-1,threshold)
        moving(m,n,i,j+1,threshold)
    return sum
 
def getsum(n):
    sum = 0
    while n>0:
        sum=sum+n%10
        n=n/10
    return sum
 
m = 50
n = 50
threshold = 18
vector = [0 for index in range(m*n)]
sum = 0
num = moving(m,n,0,0,threshold)
print(num)