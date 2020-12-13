#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(root, level):
            if root is None:
                return {} # empty tracking arr
            
            left = traverse(root.left, level + 1)
            right = traverse(root.right, level + 1)
            # print(level, left, right)

            # when finish getting values
            for key in right.keys():
                # print(key, right[key])
                # print(key in left)
                if key in left:
                    left[key] += right[key]
                else:
                    left[key] = right[key]
            # left.update(right)
            # print("updated: ", left)

            if level in left: # add root val to dict
                left[level] += [ root.val ]
            else:
                left[level] = [ root.val ]
            return left # return new dict
        
        tracking = traverse(root, 0)
        # print(tracking)

        # process dict{} format into array format
        result = []

        if len(tracking) > 0:
            deepest = max(tracking.keys())
            for i in range(deepest + 1):
                # print("key: ", i)
                result.append(tracking[i])

        return result
# @lc code=end

