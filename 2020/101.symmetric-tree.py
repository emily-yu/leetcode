#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode):
            # no nodes
            if (t1 == None) and (t2 == None):
                return True # both are None
            if (t1 == None) or (t2 == None):
                return False # one is not None, one is None
            
            # if there are two not None values
            if (t1.val == t2.val):
                return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            return False

        return isMirror(root, root)
        
# @lc code=end

