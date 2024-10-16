# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 0

        # q = [[root, root.val]] # (node, value)
        q = [(root, True)] # (node, value)
        visited = set()
        result = 0

        levelq = []
        while len(q) > 0:
            # base, total = q.pop(0)
            base, left = q.pop(0)
            if base not in visited: 
                visited.add(base)

                if base.left is None and base.right is None and left:
                    result += base.val
                if base.right: 
                    levelq.append((base.right, False))
                if base.left:
                    levelq.append((base.left, True))

                # print(levelq)
                # levelqres = [(elem.val, bool) for (elem, bool) in levelq]
                # print(levelqres)
                
                if len(q) == 0:
                    q += levelq 
                    levelq = []
                    
        return result

