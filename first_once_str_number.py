"""
只出现一次的字符
"""


def get_first_once_str(s):
    if not s:
        return -1
    if len(s) == 1:
        return s
    dic = {}
    res = []
    for i in range(len(s)):
        num = dic.get(s[i], 0)
        if num == 0:
            dic[s[i]] = num + 1
            res.append(s[i])
        if num > 0:
            dic[s[i]] = num + 1
            res.remove(s[i])
    return res[0]


print(get_first_once_str("abaccbdeffh"))