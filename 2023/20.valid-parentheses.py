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
        print(l)
        if l == 0: #empty (valid) 
            return True
        if l == 1: #too short (invalid)
            return False
        if l % 2 == 1: #odd (invalid)
            return False
        
        #space
        left_keys = ["[", "{", "("]
        left = {
            '[': [],
            '{': [],
            '(': []
        }
        match = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        i = 0
        
        # iterate through
        while i < l: # end after last char
            char = s[i]
            print(char)
            # if left, add to list
            if char in left_keys: 
                left[char].append(i)

            # if right, check for match
            else:
                pool = left[match[char]]
                if len(pool) > 0:
                    pool.pop()
                # note: if right and no left then too many right chars
                else:
                    return False
            
            i += 1 # inc

        print(left)
        # check all empty
        for ind in left:
            if len(left[ind]) > 0:
                return False
        
        return True
        
        
# @lc code=end

