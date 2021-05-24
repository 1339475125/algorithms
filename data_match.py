"""
表示数值的字符串
"""
import re
is_number = False
a = "a12e+4"
res = re.match("[+-]?\d*(\.\d+)?([eE][+-]?\d+)?", a)
if res.span()[1] == len(a):
    is_number = True
print(is_number)
