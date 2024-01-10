#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def f(head):
            if head is None:
                return head
            if head.left==None and head.right==None: 
                return head #leaf

            head.left, head.right = f(head.right), f(head.left)
            return head
        
        return f(root)

        
# @lc code=end

