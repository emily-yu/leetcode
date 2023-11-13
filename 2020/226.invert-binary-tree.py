#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case, when root.right/root.left are null / reached leaf node
        if root is None:
            return None
        
        # if assigned while inverting, then it 
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        # after the recursion happens (left/right are the return values)
        # when done traversing (returned), then swap
        root.right = left
        root.left = right
        return root
# @lc code=end

