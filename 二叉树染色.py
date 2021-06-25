# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxValue(self, root: TreeNode, k: int) -> int:
        def dfs(node) -> list[int]:
            dp = [0] * (k + 1)
            if not node:
                return dp
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 不涂色
            dp[0] = max(left) + max(right)
            #涂色
            for i in range(1, k + 1):
                dp[i] = max(left[l] + right[i - 1 - l] for l in range(i)) + node.val
            
            return dp
        return max(dfs(root))



        
        
        