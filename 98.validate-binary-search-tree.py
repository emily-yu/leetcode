#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    
        # def checkBranch(root, minval, maxval):
        #     if root == None: # reached leaf, satisfied all
        #         return True

        #     print(root.val, root.left, root.right)
        #     left = right = False
        #     if root.left and root.right: # both exists
        #         print(1)
        #         if root.left.val < root.val and root.left.val > minval and root.right.val > root.val and root.right.val < maxval:
        #             left = checkBranch(root.left, min(minval, root.left.val), maxval)
        #         # if root.right.val > root.val and root.right.val < maxval:
        #             right = checkBranch(root.right, minval, max(maxval, root.right.val))
        #         else:
        #             return False
            
        #     elif root.left or root.right: # one exists
        #         print(2)
        #         # check if left exists then if valid
        #         if root.left and root.left.val < root.val and root.left.val > minval:
        #             left = checkBranch(root.left, min(minval, root.left.val), maxval)
        #             right = True
        #         # check if right exists then if valid
        #         elif root.right and root.right.val > root.val and root.right.val < maxval:
        #             right = checkBranch(root.right, minval, max(maxval, root.right.val))
        #             left = True
        #         else:
        #             return False

        #     else: # neither exist, just finish the branch
        #         print(3)
        #         return True

        #     print(left, right)
        #     # if left and right: # left and right nodes are ok
        #     #     return True
        #     # return False
        #     # return left and right
    
        # if root == None:
        #     return True
        # return checkBranch(root, root.val, root.val)

        def checkBranch(root, minval, maxval):
            if root == None:
                return True
            
            # print(root, minval, maxval)
            # # check if left subtree is valid
            # left = right = True
            # if root.right:
            #     if root.right.val < maxval and root.right.val >= root.val:
            #         maxval = root.right.val
            #         right = checkBranch(root.right, minval, maxval)
            #         # left = True
            #     else: # if existing node doesnt's atisfy condition
            #         right = False
            # else: # doesn't exist auto valid
            #     right = True

            # # check if right subtree is valid
            # if root.left:
            #     if minval > root.left.val and root.right.val < root.val:
            #         minval = root.left.val
            #         left = checkBranch(root.left, minval, maxval)
            #         # right = True
            #     else: # if existing node doesnt's atisfy condition
            #         left = False
            # else: # doesn't exist auto valid
            #     left = True

            # return right and left

            # # fits in the range
            # if root.val > minval and root.val < maxval: # fits the appropriate constraints
            # # if root.val > minval and root.val > maxval:
            #     # tighten constraints

            #     # must be less than root.val (curr val/root creates upper bound)
            #     left = checkBranch(root.left, minval, root.val-1)

            #     # must be greater than root.val (curr val/root creates lower bound)
            #     right = checkBranch(root.right, root.val+1, maxval)

            #     return left and right

            # # if not in range, doesn't create upper bound/lower bound, violates
            # return False

            if root is None:
                return True
            
            if fits current constraints values: (check if less than max, greater than min)
                set the root into the apprppriate place
                - check for left node/subtree, root.left must be smaller than root.
                    when going to left, set the new min as left, will be smaller than current min
                - check for right node/subtree, root.right must be larger than root.
                    when going to right, set the new min as right, will be larger than the current min

                check if both left and right subtrees are True
            return False # if there is bad




            GOOD PSEUDOCODE: 

            1. if root is null, return true
            2. if doesn't fit min or max constraints (depending on which side, doesn't matter), return false

            else return if the right and left subtrees are satisfactory
            

        
        return checkBranch(root, -999, 999)
# @lc code=end

