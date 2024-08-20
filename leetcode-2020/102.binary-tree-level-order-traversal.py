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

        # q = []
        # if root is None:
        #     return q

        # q.append(root) # base
        # if root.left is None and root.right is None:
        #     return [[q[0].val]]
            
        # complete = []

        # while len(q) > 0:
        #     curr = q.pop(0)

        #     if curr is not None:
        #         q += [curr.left]
        #         q += [curr.right]
        #         complete.append(curr)
        #     else:
        #         complete.append(-999)
        
        # for elem in complete:
        #     if type(elem) == int:
        #         print(elem)
        #     else:
        #         print(elem.val)
        # # [root.left, root.right] [root]
        # # [root.left.left, root.left.right] [root.left, root.right, root]

        # result = [] # return array
        # level = 0 #2^0 = 1 node, 2^1 = 2 nodes
        # level_count = 2**level
        # start = 0
        # node_left = len(complete) # 5 -> 4 -> 2 -> look for 4, only 2 left; node(left) < level_count
        # for node in complete:
        #     level_result = []
        #     print("compare: ", level_count, node_left)
        #     # if level_count < node_left: # full amount of nodes
        #     print(complete[start:start+level_count])
        #     for elem in complete[start:start+level_count]:
        #         if elem != -999:
        #             level_result.append(elem.val)
        #         else:
        #             level_result.append(-999)
        #     start += level_count
        #     level += 1
        #     level_count = 2**(level)
        #     print(level_result)
        #     if level_result != []:
        #         result.append(level_result)
        # return result
        


        


# @lc code=end

