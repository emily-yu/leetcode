#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # for optimization
        memo = dict()

        # test case
        # weights = [1, 2, 3, 1, 1]
        # D = 3

        # weights = [3, 2, 2, 4, 1, 4]
        # D = 3

        result = []

        # init bfs
        q = []
        q.append(([], weights, 0))

        # create all combinations possible bfs
        while len(q) > 0:
            root = q.pop(0) # [result, remaining, level]
            if root[2] == D: # done, reached level
                if root[1] == []: # touched all
                    result.append(root[0] + [root[1][0:i+1]])
                    # print('appending: ', root)
                else:
                    pass
            else: # generate the rest of the combinations
                for i in range(len(root[1])):
                    # print(root[0], root[1][0:i+1])
                    # print('level', root[2] + 1)

                    # amount of children validation
                    if root[1][i+1:] == [] and root[2] != D-1:
                        # print('omit')
                        pass
                    else: # enough children for next level
                        # print(root[0] + [root[1][0:i+1]])
                        q.append((root[0] + [root[1][0:i+1]], root[1][i+1:], root[2] + 1))
                        # break
            # print(q)
        # print(result)

        # pick out smallest value
        minval = float('inf')
        for item in result:
            # print(item)
            sections = [sum(part) for part in item]
            # print(max(sections))
            if max(sections) < minval:
                minval = max(sections)

        return minval
        '''
        [3, 2, 2, 4, 1, 4]
        days = 4

        base = [3]
        children = [2, 2, 4, 1, 4]
        level = 0
        @ [3]
            base [2]
            children = [2, 4, 1, 4]
            level = 1
            @ [3][2]
                base [2]
                children = [4, 1, 4]
                level = 2
                @ [3][2][2]
                    @[3][2][2][4, 1, 4] ==========DONE==========
                base [2, 4]
                children = [1, 4]
                level = 2
                @ [3][2][2, 4]
                    @[3][2][2, 4][1,4] ==========DONE==========
                base [2, 4, 1]
                children = [4]
                level = 2
                @ [3][2][2, 4, 1]
                    @ [3][2][2, 4, 1][4] ==========DONE==========
                base [2, 4, 1, 4]
                children = []
                level = 2
                    ; empty set
                    ; level != 3, len(children)=0 < 3(days) - level = 1 *at least one child per level
            base [2, 2]
            children = [4, 1, 4]
            level = 1
                base [4]
                children = [1, 4]
                @ [3][2, 2][4]
                    @[3][2, 2][4][1, 4] ==========DONE==========
                base [4, 1]
                children = [4]
                level = 2
                @ [3][2, 2][4, 1]
                    level = 3 @ [3][2, 2][4, 1][4] ==========DONE==========
                base [4, 1, 4]
                children = []
                level = 2
                    ; empty set
                    ;level doom, requires at least 1
            base [2, 2, 4]
            children = [1, 4]
            level = 1
            @ [3][2, 2, 4]
                base [1]
                children = [4]
                level = 2
                @[3][2, 2, 4][1]
                    level = 3 @ [3][2, 2, 4][1][4] ==========DONE==========
                base [1, 4]
                children = []
                @[3][2, 2, 4][1, 4]
                    ; empty set
                    ; level doom, requires at least 1
            base [2, 2, 4, 1]
            children = [4]
            level = 1
            @ [3][2, 2, 4, 1]
                ### LOGIC FOR INVALIDATION
                ; not enough elements in children for 2 more separation
                ; level = 1 and nextlevel=2, target = 4 days -> 3 level
                ; nextlevel requires at least 3(level) - 1(currlevel) = 2 elements
            base [2, 2, 4, 1, 4]
            children = []
            level = 1
                ; not enough elements
        '''
# @lc code=end

