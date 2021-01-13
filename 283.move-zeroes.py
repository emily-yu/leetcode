#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        0 1 0 3 12
        pointer = 0; val=0
            lastzero = 0
            pointer += 1
        pointer = 1; val=1
            lastzero > 1, swap nums[0] and nums[1] (this)
                1 0 0 3 12
            pointer = lastzero + 1 = 1
            lastzero = -1
        pointer = 1; val = 0
            lastzero = 1
            pointer += 1
        pointer = 2; val = 0
            lastzero > 1; already set, do nothing
            pointer += 1
        pointer = 3; val = 3
            lastzero > 1; swap nums[1] and nums[3] (this)
                1 3 0 0 12
            pointer = lastzero + 1 = 2
            lastzero = -1
        pointer = 2; val = 0
            lastzero = 2
            pointer += 1
        pointer = 3; val = 0
            lastzero > 1; already set, do nothing
            pointer += 1
        pointer = 4; val = 12
            lastzero > 1; swap nums[2] and nums[4] (this)
                1 3 12 0 0
            pointer = lastzero + 1 = 3
            lastzero = -1
        pointer = 3; val = 0
            lastzero = 3
            pointer += 1
        pointer = 4; val = 0
            lastzero = 3
            pointer += 1
        pointer = 5; val = nulloutofbounds
        """
        # nums = [3, 0, 1, 2, 0, 2]
        last_zero = -1
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == 0:
                if last_zero >= 0:
                    pass # do nothing
                else:
                    last_zero = pointer
            else:
                if last_zero >= 0:
                    nums[last_zero], nums[pointer] = nums[pointer], nums[last_zero]
                    pointer = last_zero
                    last_zero = -1
                    # print(nums)
                else:
                    pass # do nothing
            pointer += 1
        # print(nums)
        
# @lc code=end

