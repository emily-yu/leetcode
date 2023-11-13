#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for elem in nums:
            ind = abs(elem) - 1 # even if negative, doesn't correspond to the place. still need to take the index for that value and turn negative
            # print(ind)
            if nums[ind] > 0:
                nums[ind] = nums[ind] * -1 # mark as visited
            # print(ind, nums)

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
# @lc code=end

