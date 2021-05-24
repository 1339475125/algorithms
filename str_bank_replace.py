"""
替换空格
"""

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s == None:
            return None
        l1 = len(s)  # 原字符串的长度
        spaceNumber = 0   # 用来记录空格的数目
        for i in range(len(s)):
            if s[i] == " ":
                spaceNumber += 1
        l2 = l1 + 2*spaceNumber 
        # 因为一个空格要用% 2 0三个字符来替换，因此也就是原字符串有一个空格，新字符串的长度就要加2
        str = [1] * l2  # 生成一个长度为l2的列表，用来填充
        # 设置两个指针，分别指向s和str的尾部
        p1 = l1 - 1
        p2 = l2 - 1
        while p1 >= 0:# 设置循环终止条件
            if s[p1] != " ":  # 如果s当前的空格不为空，直接落下即可。
                str[p2] = s[p1]
                p1 -= 1     # 更新p1和p2
                p2 -= 1
            else:             # 如果为空，那么就要用%20来替换了
                str[p2] = "0"
                str[p2-1] = "2"
                str[p2-2] = "%"
                p1 -= 1
                p2 -= 3
        print( "".join(str))    # 连接str列表，生成字符串

s = Solution()
s.replaceSpace("a b  c")