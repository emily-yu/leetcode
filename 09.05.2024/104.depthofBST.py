# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def ct(root, depth):
            if root is None:
                return 0 # base count
            
            leftct = 1 + ct(root.left, depth)
            rightct = 1 + ct(root.right, depth)

            if leftct > rightct:
                return leftct
            else:
                return rightct
        
        return ct(root, 0)
