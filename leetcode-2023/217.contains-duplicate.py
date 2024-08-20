#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        uniq = set()
        for val in nums: 
            if val in uniq:
                return True
            else:
                uniq.add(val)
        
# @lc code=end

