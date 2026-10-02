# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,left,right):

            if not root: return True

            if not (left<root.val<right): return False

            validLeftSubTree = dfs(root.left,left,root.val)
            validRightSubTree = dfs(root.right,root.val,right)

            return validLeftSubTree and validRightSubTree
        
        return dfs(root,float("-inf"), float("inf"))