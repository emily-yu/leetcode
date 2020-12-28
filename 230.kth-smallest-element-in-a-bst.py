#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        q = [root]
        explored = set()
        while len(q) > 0:
            root = q.pop()
            explored.add(root.val)

            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        
        # print(explored)
        result = []
        for i in range(k):
            min_elem = min(explored)
            result.append(min_elem)
            explored.remove(min_elem)
    
        # print(result)
        return result[-1]




# @lc code=end

