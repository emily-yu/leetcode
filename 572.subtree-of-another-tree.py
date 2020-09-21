#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def foundNode(s: TreeNode, t: TreeNode) -> bool:  
            if s == None and t is not None:
                return False
            if s is not None and t is None:
                return False
            if s is None and t is None:
                return True

            if s.val == t.val:
                # search for next node
                left = foundNode(s.left, t.left) # true or false
                right = foundNode(s.right, t.right) # true or false
                # if left == True or right == True:
                # return True
                return left and right
            # else:
            #     # continue searching for first node
            #     left = self.foundNode(root.left, find_head, find_head) # true or false
            #     right = self.foundNode(root.right, find_head, find_head) # true or false
            return False
        if foundNode(s, t):
            return True
        if s is None:
            return False
        return foundNode(s.left, t) or foundNode(s.right, t)
            
        # return left and right

        
# @lc code=end

