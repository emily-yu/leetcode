#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # # Function to print binary tree in 2D  
        # def traverse(root):
        #     current_level = [root]
        #     while current_level:
        #         print(' '.join(str(node) for node in current_level))
        #         next_level = list()
        #         for n in current_level:
        #             if n.left:
        #                 next_level.append(n.left)
        #             if n.right:
        #                 next_level.append(n.right)
        #         current_level = next_level

        def subtree(root, nums, arr):
            if len(nums) == 0:
                return None

            max_val = max(nums)
            max_ind = nums.index(max_val)
            print(max_val, max_ind, nums)
            
            arr.append(max_val)
            print(arr)
            left = subtree(root, nums[0:max_ind], arr)
            right = subtree(root, nums[max_ind+1:len(nums)], arr)
            
            root.left = left
            root.right = right

            return TreeNode(root.val)
        
        res = subtree(TreeNode(nums[0]), nums, [])
        return res
# @lc code=end

