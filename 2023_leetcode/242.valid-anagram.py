#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # edge cases
        if s == t: return True
        if len(s) == 1: return s == t
        # if len(s) == 1 and s != t: return False
        # no empty strings

        letters = {}
        for letter in s: # create counter
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        for letter in t: # reverse count in anagram
            if letter not in letters:
                return False # auto invalidate
            else:
                letters[letter] -= 1
        
        for key in letters:
            if letters[key] != 0:
                return False
        return True
# @lc code=end

