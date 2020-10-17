#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1


        start = -1
        letterind = 0
        hayind = 0
        while hayind < len(haystack):
        
            '''
            22% runtime beat
            7.86% memory beat
            '''
            # if start == -1:
            #     if haystack[hayind] == needle[letterind]:
            #         start = hayind
            #         hayind += 1
            #         letterind += 1
            #         if len(needle) == letterind:
            #             return start
            #     else: # not equal
            #         hayind += 1
            # else: # iterating
            #     if haystack[hayind] == needle[letterind]:
            #         letterind += 1
            #         hayind += 1
            #         if len(needle) == letterind:
            #             return start
            #     else: # not equal
            #         letterind = 0
            #         hayind = start + 1
            #         start = -1

            '''
            37.59% runtime beat
            7.86% memory beat
            '''
            if haystack[hayind] == needle[letterind]:
                if start == -1:
                    start = hayind
                hayind += 1
                letterind += 1
                if len(needle) == letterind:
                    return start
            else:
                if start != -1:
                    letterind = 0
                    hayind = start + 1
                    start = -1
                else:
                    hayind += 1

        return -1
        


# @lc code=end

