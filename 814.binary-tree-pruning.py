#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        print(root)
        if root == None:
            return None
                
        # left = right = False
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        root.left = left # set to new roots
        root.right = right
        
        # if left and right:
        #     print('left ', left)
        #     print('right ', right)
        #     if right.val == 0:
        #         root.right = None
        #     if left.val == 0:
        #         root.left == None
        #     if right.val == 1 or left.val == 1: 
        #         return root
        # if left:
        #     left = self.pruneTree(root.left)
        #     if left.val == 1:
        #         return root
        # if right:
        #     right = self.pruneTree(root.right)
        #     if right.val == 1:
        #         return root

        # if root.val == 1:
        #     if right and right.val == 0:
        #         root.right = None
        #     if left and left.val == 0:
        #         root.left = None
        #     return root

        # left and right have failed - if root.val = 0 then whole subtree is doomed
        if root.val == 0 and root.left == None and root.right == None:
            root = None

        return root

# @lc code=end

