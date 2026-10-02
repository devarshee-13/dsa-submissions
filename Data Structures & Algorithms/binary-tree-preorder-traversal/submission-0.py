# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.right = None
#         self.left = None

class Solution:
    def preorderTraversal(self, root) -> List[int]:
        res = []

        def preorder(root):

            if root is None: return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return res