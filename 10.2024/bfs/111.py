# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = [root]
        depth = 1

        level = []
        while len(q) > 0: 
            base = q.pop(0)
            if base.left is None and base.right is None: 
                return depth
            else: 
                if base.left: 
                    level.append(base.left)
                if base.right: 
                    level.append(base.right)

                if len(q) == 0: 
                    q += level
                    level = []
                    depth += 1
        return -1 

