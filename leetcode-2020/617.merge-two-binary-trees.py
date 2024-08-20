#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # def insertNodes(t1: TreeNode, t2: TreeNode, root):
        #     if (t1 is not None) and (t2 is not None):
        #         left = insertNodes(t1.left, t2.left, root)
        #         right = insertNodes(t1.right, t2.right, root)
        #         root.left = left
        #         root.right = right
        #         return root

        #     if (t1 is None) and (t2 is not None):
        #         root.right = TreeNode(t2.val)
        #         return root
        #     if (t1 is not None) and (t2 is None):
        #         root.left = TreeNode(t1.val)
        #         return root

        #     if (t1 is None) and (t2 is None):
        #         return TreeNode(None)

        # return insertNodes(t1, t2, TreeNode(None))
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
            
# @lc code=end

