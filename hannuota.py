#!/usr/bin/env python
#coding:utf-8
 
import sys
 
global a
a =0


def fun():
    global a
    a = a+1
 

def hannuoyi(n,A,B,C):
    if n==1:
        move(1,A,C)
    else:
        hannuoyi(n-1,A,C,B)
        move(n,A,C)
        hannuoyi(n-1,B,A,C)

 
def move(n,tempA,tempB):
    print ("move plate %d from column %s to column %s" %(n,tempA,tempB))
    fun()


if __name__=="__main__":
    hannuoyi(3,'A','B','C')
    print ("total:we need %d steps"%(a) )