# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depthf(root, depth):
            if root is None:
                return 0
            
            left = depthf(root.left, depth) 
            right = depthf(root.right, depth)

            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1 # don't need depth just pick larger one

        return depthf(root, 0) != -1