"""
1、暴力解法，拉倒最大的值以此往下推到
2、动态规划
3、栈方式
"""


class Solution:

    def dongtaiguihua(self, s:str) -> int:
        n = len(s)
        if n==0:
            return 0
        dp = [0]*n
        for i in range(s):
            dp[i] = i - dp[i-1] -1
            if s[i] == ")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == "(":
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)

    def stack(self, s):
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i -stack[-1]
                    max_length = max(max_length, length)
        return max_length


    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*len(s)
        for i in range(1, len(s)):
            print(i, s[i], dp)
            if s[i]==")":
                pre = i - dp[i-1] -1
                print(pre)
                if pre >= 0 and s[pre] == "(":
                    dp[i] =dp[i-1] +2
                    if pre > 0:
                        dp[i] += dp[pre-1]
        return max(dp)

s = Solution()
string = "(())"
print(s.longestValidParentheses(string))