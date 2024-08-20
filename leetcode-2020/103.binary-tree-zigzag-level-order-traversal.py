#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # root = [1, 2, 3, 4, null, null, 5]

        if root == None:
            return []

        # q = [[root]]
        q = [root]
        result = []
        reverse = True # L->R default

        while len(q) > 0:
            # level = q.pop(0) # [ child, child, child ]
            # print('level', [node.val for node in level])
            # print(reverse)
            # if not reverse:
            # level.reverse()
            # reverse = not reverse
            # result.append(level.val)
            # print('level', [node.val for node in level])

            next_level = []
            # for child in q:
            for i in range(len(q)):
                node = q.pop(0)
                next_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    

            # if len(next_level) > 0:
            if not reverse:
                result.append(next_level[::-1])
                print(next_level)
            else:
                result.append(next_level)
                print(next_level)
            reverse = not reverse
        
        print(result)
        return result

# @lc code=end

