#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # def diffsub(root):
        #     diffleft = diffright = 999
        #     left = right = 999

        #     # return values
        #     if root.left == 999: # set left val
        #         left = diffsub(root.left)
        #     elif root.left:
        #         diffleft = abs(root.val - root.left.val)
        #         left = diffsub(root.left)



        #     if root.right == -1:
        #         right = diffsub(root.right)
        #     elif root.right:
        #         diffright = abs(root.val - root.right.val)
        #         right = diffsub(root.right)

        #     # comparison
        #     if root.left and root.right:
        #         return min(diffleft, diffright, left, right)
        #     elif not(root.left and root.right):
        #         return 999
        #     elif root.left:
        #         return min(diffleft, left)
        #     elif root.right:
        #         return min(diffright, right)

        # if diffsub(root) == -1:
        #     return 0
        # return diffsub(root)

        # get minimums and maximums for a tree
        def minmaxtree(root, minval, maxval):
            
            if not (root.left and root.right):
                # don't call again
                return (root.val, root.val) # (min=3, max=3)
            

            left = right = None
            # left and right node stuff
            if root.left and root.right:
                # call both sides
                left = minmaxtree(root.left, minval, maxval) # (min, max)
                right = minmaxtree(root.right, minval, maxval)
            
            if root.left:
                # call left side
                left = minmaxtree(root.left, minval, maxval)
            if root.right:
                # call right side
                right = minmaxtree(root.right, minval, maxval)

            # compare results
            # get overall min
            print(left, right)
            minval = min(left[1], minval)
            maxval = min(right[0], maxval)
            print(minval, maxval)
            return (minval, maxval)
            
        # res = minmaxtree(root, root.val, root.val)
        # return abs(res[0] - res[1])

        # def rawdistdiff(root, mindist):

        #     if root.left is None and root.right is None:
        #         return mindist
            
        #     # for root node
        #     print(root.val, mindist)
        #     if root.left and root.right: # root=4, left=2, right=6
        #         # left = abs(root.left.val - root.val) # 2 - 4 = 2
        #         # right = abs(root.right.val - root.val) # 6 - 4 = 2
        #         mindist1 = abs(root.left.val - root.val)
        #         mindist2 = abs(root.right.val - root.val)
        #         mindist = min(mindist1, mindist2)
        #     if root.left:
        #         mindist = abs(root.left.val - root.val)
        #     if root.right:
        #         mindist = abs(root.right.val - root.val)

        #     print(mindist)

        #     # set up left and right nodes
        #     left = right = 999
        #     if root.left:
        #         left = rawdistdiff(root.left, mindist)
        #     if root.right:
        #         right = rawdistdiff(root.right, mindist)

        #     return min(mindist, left, right)


        # return rawdistdiff(root, 999)

        def again(root, diff):
            if root.left is None and root.right is None:
                return diff

            left = right = 999
            if root.left:
                root_to_left = abs(root.val - root.left.val) # if exists
                left = again(root.left, min(root_to_left, diff))
            if root.right:
                root_to_right = abs(root.val - root.right.val)
                right = again(root.right, min(root_to_right, diff))

            return min(left, right)

        return again(root, 999)
# @lc code=end

