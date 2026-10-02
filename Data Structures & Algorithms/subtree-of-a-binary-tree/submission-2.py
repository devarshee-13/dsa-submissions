# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        valid = False
        def isSameTree(p,q):

            if not p and not q: return True
            if not p or not q: return False

            left = isSameTree(p.left,q.left)
            right = isSameTree(p.right,q.right)

            if left and right and p.val == q.val: return True 
            else: return False
                
        q = deque([root])

        while q:
            node = q.pop()
            if node.val == subRoot.val: 
                if isSameTree(node,subRoot): return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)    
        
        return False  