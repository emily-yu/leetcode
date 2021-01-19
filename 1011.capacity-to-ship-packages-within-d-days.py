#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
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

