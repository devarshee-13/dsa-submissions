# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:

            # go to the left most node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # process the most recent node
            cur = stack.pop()
            res.append(cur.val)

            # now explore the right subtree
            cur = cur.right
      
        return res

# empty stack -> append all left nodes in the stack from top to bottom order (becuase stack follows LIFO), 
# then pop one at a time and then check it's right subtree