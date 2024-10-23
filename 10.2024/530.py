# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = 99999999
        q = [(root, result)]
        visited = set()

        while len(q) > 0:
            base, minval = q.pop(0)
            visited.add(base.val)

            # if base.left is None and base.right is None:
            #     if minval < result:
            #         result = minval
            # else:
            if base.left:
                val = abs(base.left.val - base.val)
                if val < minval: 
                    q.append((base.left, val))
                else:
                    q.append((base.left, minval))
            if base.right:
                val = abs(base.right.val - base.val)
                if val < minval: 
                    q.append((base.right, val))
                else:
                    q.append((base.right, minval))
        
        # lol cheating
        visited = sorted(list(visited))
        print(visited)
        absminval = 999999999999
        if len(visited) == 2:
            return abs(visited[1] - visited[0])
        for i in range(len(visited) - 1):
            print(i, i+1)
            result = abs(visited[i] - visited[i+1])
            if result < absminval:
                absminval = result
        return absminval

        return result
        
