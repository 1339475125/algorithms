"""
给定一个数字，按照如下规则翻译成字符串：1 翻译成“a”，2 翻译成“b”... 26 翻译成“z”。一个数字有多种翻译可能，例如 12258 一共有 5 种，分别是 abbeh，lbeh，aveh，abyh，lyh。实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

def translate_num_to_string(s, count=0):
    if not s:
        return 0
    s = str(s)
    size = len(s)
    dp = [0] * (size+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, size+1):
        temp = int(s[i-2] + s[i-1])
        if temp >=10 and temp <= 25:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]

    print(dp[size])

translate_num_to_string("1313131")