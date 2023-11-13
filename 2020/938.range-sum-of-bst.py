#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def bstsum(root):
            if root == None:
                return 0
            elif root.val <= R and root.val >= L:
                # print(bstsum(root.left), bstsum(root.right), root.val)
                return bstsum(root.left) + bstsum(root.right) + root.val
            elif root.val > R or root.val < L:
                return 0 + bstsum(root.left) + bstsum(root.right)
        
        return bstsum(root)
# @lc code=end

