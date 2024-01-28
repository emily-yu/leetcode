#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # trimming
        s = list(s)
        for i in range(len(s)):
            s[i] = s[i].lower()
            if s[i] not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                s[i] = ""
        s = ''.join(s)

        if len(s) < 1: return True

        last = len(s) - 1
        first = 0
        while first < last:
            if s[first] != s[last]:
                print(s[first], s[last])
                return False
            first += 1
            last -= 1
        return True

# @lc code=end

