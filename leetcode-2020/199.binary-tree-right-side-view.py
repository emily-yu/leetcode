#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # edge cases
        if root is None:
            return []

        def helper(root, arr):
            if root is None:
                return []
            
            # create recursive calls
            right = helper(root.right, arr) # [x, x, ...]
            left = helper(root.left, arr) # [x, x ...]

            # process data
            # do array replacement
            if len(left) == 0:
                arr = right
            elif len(right) == 0:
                arr = left
            elif len(left) > len(right):
                # replace all left elements not deeper than right
                print(left, right)
                for i in range(len(right)):
                    left[i] = right[i]
                arr = left
            else: # just return len(left) < len(left)
                arr = right

            # add new data
            arr = [root.val] + arr
            
            # return arr for root
            return arr
        
        result = helper(root, [])
        return result
# @lc code=end

