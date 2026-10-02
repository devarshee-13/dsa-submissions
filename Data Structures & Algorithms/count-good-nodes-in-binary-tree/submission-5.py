# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # maxVal = float("-inf")
        count = 0

        def dfs(root,maxVal):
            if not root: return 0
            # nonlocal maxVal,count
            
            if root.val >= maxVal: count = 1
            else: count = 0
            
            maxVal = max(maxVal, root.val)
            
            if root.left: count += dfs(root.left,maxVal)
            if root.right: count += dfs(root.right,maxVal)
        
            return count

        return dfs(root,root.val)     