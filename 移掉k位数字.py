class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) < 2:
            return "0"
        if len(num) <= k:
            return "0"
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


s = Solution()
num = "10200"
removeKdigits(num, 1)