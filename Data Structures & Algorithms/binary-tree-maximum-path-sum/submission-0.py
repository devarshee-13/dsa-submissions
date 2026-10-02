# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node: return 0

            maxDownwardSumLeft = dfs(node.left)
            maxDownwardSumLeft = max(maxDownwardSumLeft, 0)
            maxDownwardSumRight = dfs(node.right)
            maxDownwardSumRight = max(maxDownwardSumRight,0)

            maxDownwardSum = max(maxDownwardSumRight, maxDownwardSumLeft) + node.val

            res = max(res, node.val + maxDownwardSumRight + maxDownwardSumLeft)

            return maxDownwardSum
        
        dfs(root)

        return res



        