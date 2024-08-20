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
        ### bfs
        # q = [root]
        # explored = set()
        # while len(q) > 0:
        #     root = q.pop()
        #     explored.add(root.val)

        #     if root.left:
        #         q.append(root.left)
        #     if root.right:
        #         q.append(root.right)
        
        # result = []
        # for i in range(k):
        #     min_elem = min(explored)
        #     result.append(min_elem)
        #     explored.remove(min_elem)
    
        # return result[-1]

        ### standard inorder; after reading solution
        q = []        
        def f(root):
            if root is None:
                return []
            # left smaller than middle smaller than right side
            result = f(root.left) + [root.val] + f(root.right)
            return result
        
        return f(root)[k-1]
        
        




# @lc code=end

