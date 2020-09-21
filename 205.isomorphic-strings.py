#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # charify, index list
        charcount = 0

        schar = {}
        slist = list(s)
        for char in slist:
            if char not in schar:
                schar[char] = charcount
                charcount += 1

        charcount = 0 # reset for next counting

        tchar = {}
        tlist = list(t)
        for char in tlist:
            if char not in tchar:
                tchar[char] = charcount
                charcount += 1

        # replace letters with numbers
        for i in range(len(s)):
            slist[i] = schar[s[i]]
            tlist[i] = tchar[t[i]]

        if slist == tlist:
            return True
        return False
    
# @lc code=end

