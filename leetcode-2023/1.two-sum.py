#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        
        alts = []
        for num in nums:
            alts.append(target-num)
        for i in range(len(alts)):
            if alts[i] in nums and i != nums.index(alts[i]): 
                return (i, nums.index(alts[i]))
            
        
# @lc code=end

