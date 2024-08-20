#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # edge cases
        l = len(s) 
        if l == 0: #empty (valid) 
            return True
        if l == 1: #too short (invalid)
            return False
        if l % 2 == 1: #odd (invalid)
            return False
        
        #space
        stk = []
        i = 0
        match = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        # iterate through
        while i < l: # end after last char
            char = s[i]
            # if left, add to list
            if char in ['(', '[', '{']: 
                stk.append(char)

            # if right, check for possible match
            else:
                # left chars exist?
                if len(stk) > 0: 
                    left = stk.pop()
                else:
                    return False
                
                # match?
                if match[char] != left:
                    return False
            
            i += 1 # inc

        # if still left chars then doom
        if len(stk) > 0:
            return False
        return True
        
        
# @lc code=end

