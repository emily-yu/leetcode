#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: 
            return True
        
        digits = str(n) 
        seen = set()
        seen.add(n)
        sum = 0
        while sum != 1: 
            sum = 0
            for num in digits: #1, 9
                sum += int(num)*int(num)
            digits = str(sum)

            # read problem wrong: looping endlessly but needs to return False
            if digits in seen: return False
            seen.add(digits)
        return True
            

# @lc code=end

