#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None: # both none
            return True
        if root.left is not None and root.right is not None and root.right.val == root.left.val: # both equal
            return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
        if root.right is None and root.left.val == root.val: # one equal
            return self.isUnivalTree(root.left)
        if root.left is None and root.right.val == root.val:
            return self.isUnivalTree(root.right)
        
        # not equal
        else: # root.left.val != root.val
            return False

        #         # no nodes
        # if (root.left == None) and (root.right == None):
        #     return True
        
        # left = False
        # right = False
        # # print(root.val, root.left.val)
        # if (root.left is not None) and (root.left.val == root.val):
        #     print("1")
        #     left = True
        # if (root.right is not None) and (root.right.val == root.val):
        #     print("2")
        #     right = True

        # print(left, right)
        # if left and right:
        #     return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        # return False
# @lc code=end

