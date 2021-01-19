#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # nums = [2, 1, 5, 6]

        if len(nums) == 1:
            return True

        q = [0]
        tracking = [True] * len(nums)

        while len(q) > 0:
            idx = q.pop(0)

            # to not repeat indexes that will fail
            if tracking[idx] == False:
                continue
            
            # iterate through
            added = False
            for i in range(0, nums[idx]):
                if idx + i + 1 < len(nums) - 1:
                    q.append(idx + i + 1)
                    if added:
                        added = True
                elif idx + i + 1 == len(nums) - 1:
                    return True

            tracking[idx] = added

        return False
# @lc code=end

