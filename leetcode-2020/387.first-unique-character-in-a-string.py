#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        tracking = {}
        for char in s:
            if char in tracking:
                tracking[char] += 1
            else:
                tracking[char] = 1
        
        for key in tracking:
            if tracking[key] == 1:
                return s.index(key) # dict maintains insertion order
        return -1 # if all keys not unique
# @lc code=end

