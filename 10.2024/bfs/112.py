# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        # if root.left is None: 
        #     return root.right.val + root.val == targetSum
        # if root.right is None: 
        #     return root.left.val + root.val == targetSum

        q = [[root,root.val]]
        visited = []
        levelq = []

        def isLeaf(base):
            return base.right is None and base.left is None

        while len(q) > 0:

            base, prevtotal = q.pop(0)
            # print(base.val, prevtotal)
            if base not in visited:
                visited.append(base)
                # L = base.left
                # R = base.right

                if base.left:
                    totalleft = prevtotal + base.left.val
                    if totalleft == targetSum and isLeaf(base.left):
                        # print(totalleft, base)
                        return True
                    else: 
                        levelq.append([base.left, totalleft])
                if base.right:
                    totalright = prevtotal + base.right.val
                    if totalright == targetSum and isLeaf(base.right):
                        # print(totalright, base)
                        return True
                    else: 
                        levelq.append([base.right, totalright])

            if len(q) == 0:
                q += levelq
                levelq = []
            
            # print(base.val, q, levelq)

        # else
        return False


