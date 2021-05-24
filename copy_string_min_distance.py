# -*- coding:utf-8 -*-

def min_distance(a, b): 
    """
    将字符串 B 转换为字符串 A
    """
    distance = 0
    if a==b:
        return distance

    if not len(b):
        return distance  

    if not len(a):  # 删除所有元素
        return len(b)
    
    lista = list(a)
    listb = list(b)
    for i in range(len(lista)):
        if i > len(listb) -1:
            distance = distance + (len(lista) - len(listb)) # 之后每一次做插入
            break
        if lista[i] == listb[i]:
            pass
        else:
            listb[i]=lista[i]
            distance += 1
    return distance



if __name__ == "__main__":
    a = "123r6u5u"
    b = "dwfwfe"
    print(min_distance(a, b) )