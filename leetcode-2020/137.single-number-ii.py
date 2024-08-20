#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        # print(nums)

        # nums[0] = 0
        while len(nums) > 0:
            # print('----', nums[0:3])
            if len(nums[0:3]) == 1:
                return nums[0]
            if nums[0] != nums[1] or nums[1] != nums[2]:
                return nums[0]

            nums = nums[3:len(nums)]
            # print(nums)

            
# @lc code=end

