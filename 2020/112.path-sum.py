#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        # edge case
        if root is None:
            return False
            
        def f(root):
            if root.left is None and root.right is None: # leaf
                return [root.val]
            
            # create joint left and right array
            left, right = [], []
            if root.left:
                left = f(root.left)
            if root.right:
                right = f(root.right)
            net = left + right

            # add root.val to all values
            net = [elem + root.val for elem in net]
            return net

        result = f(root)
        if targetSum in result:
            return True
        return False


            
# @lc code=end

