# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        level = []
        while len(q) > 0:
            base = q.pop(0) # construct new level
            if base is not None:
                if base.left:
                    level += [base.left]
                if base.right:
                    level += [base.right]
                # level += [base.left, base.right]

                if base.left and base.right: # check not same parent
                    if base.left.val == x and base.right.val == y:
                        return False
                    if base.right.val == x and base.left.val == y:
                        return False

            # print("level:")
            test = []
            for elem in level: 
                if elem:
                    test.append(elem.val)
                if x in test and y in test:
                    # print("found")
                    return True
            # print(test)
            if len(q) == 0:
                q += level # append to q
                level = []
                # print("append")

        return False