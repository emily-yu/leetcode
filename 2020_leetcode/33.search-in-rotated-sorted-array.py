#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 0:
        #     return -1

        # ind = 0
        # if target >= nums[ind]:
        #     ind = 0
        #     while nums[ind] <= nums[ind+1] and ind != len(nums) - 1:
        #         ind += 1
        # else:
        #     ind = len(nums) - 1
        #     while (nums[ind] > nums[ind-1] and ind != 0):
        #         ind -= 1

        # if nums[ind] != target:
        #     return -1       
        # return ind
        if target in nums:
            return nums.index(target)
        return -1
# @lc code=end

