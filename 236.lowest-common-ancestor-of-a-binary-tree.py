#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # i wrote a whole ass algo for a normal tree, not a binary tree

        # def f(root, p, q, LCA): # returns (p=TreeNode, q=TreeNode)
        #     # if root is leaf (left=None, right=None)
        #     # check root.val if found: root.val == p or root.val = q, return (p=None, q) or (p, q=None)
        #     if root.left is None and root.right is None:
        #         if root.val == p:
        #             return (root.val, None, False) # (p, q, LCAfound)
        #         if root.val == q:
        #             return (None, root.val, False)

        #     # check if LCA already found, if its already found, just return sth...
        #     # if LCA is not None:
        #     #     pass # TODO

        #     # time to recurse, with p and q values filled in
        #     left = f(root.left, p, q, LCA) # returns (p, q, LCAfound)
        #     right = f(root.right, p, q, LCA)

        #     # check if root val completes the set, using p,q as local variables
        #     # if p is None and root.val == p and q is not None: # done
        #     # if p is None and root.val == target_p and target_q is not None: # done
        #     #     print("p is ", root.val)
        #     #     p = root.val
        #     # elif q is None and root.val == target_q and target_p is not None: # done
        #     #     print("q is ", root.val)
        #     #     q = root.val
        #     # # check if set is completed for p and q at that space
        #     # if p is not None and q is not None and LCA is None:
        #     #     LCA = root.val
        #     # if p is not None and q is not None and (LCA is not None):
        #     #     pass
        #     return root
        
        # p, q = f(root.val, None, None, None)
        # return p
        # iterate down

        # def asdf(root):
        # print(root.val, p, q)
        if root == None:
            return None
            
        print(root)
        if root:
            if root.val > p.val and root.val < q.val:
                return root
            if root.val > p.val or root.val > q.val: # recurse on the left
                return self.lowestCommonAncestor(root.right, p, q)
            if root.val < p.val or root.val < q.val: # recurse to the right
                return self.lowestCommonAncestor(root.left, p, q)
        # else:
            # root.val < p and root.val > q
            # root.val = p and root.val < q, >q
        return root

        # return asdf(root)
# @lc code=end

