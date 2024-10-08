# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(root1, root2):
            if root1 is None and root2 is None: # not equal already, one has excess 
                return True
            if root1 is None or root2 is None: 
                return False
            if root1.val == root2.val:
                # return True
                return compare(root1.left, root2.left) and compare(root1.right, root2.right)
            else:
                return False
        
        return compare(p, q)

            
            