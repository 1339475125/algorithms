"""
正则表达式匹配
. 任意一个字符
* n个前面的字符 包括0
"""

def match(str, pattern):
    m  = len(str)
    n = len(pattern)
    dp = [[False] * (m+1)]*(n+1)
    dp[0][0] = True
    for i in range(n+1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == "*":
                if pattern[j-2] == str[i -1]  or pattern[j-2]== '.':
                    dp[i][j] = dp[i][j-1]
                    dp[i][j] = dp[i-1][j]
                    dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = dp[i][j-2]
    print(dp)
    return dp[m][n]


if __name__ == "__main__":
    print(match("aaaa", "aa*"))

