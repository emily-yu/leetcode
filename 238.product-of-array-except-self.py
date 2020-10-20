#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # coding after seeing solution
        prod = [1]* len(nums)

        for i in range(1, len(nums)): # go right
            # print(i)
            prod[i] *= prod[i-1] * nums[i-1]
        # print(prod)
        
        curr = 1
        for i in reversed(range(len(nums) - 1)): # go left
            # print(i, prod[i], nums[i])
            curr *= nums[i+1] # curr = curr * nums[i+1]
            prod[i] *= curr
        #     print(curr)

        # print(prod)
        return prod

# @lc code=end

