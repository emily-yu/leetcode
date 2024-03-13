#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # create hashmap
        mapping = {
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = None # char
        res = 0
        curr = 0

        # split string into char arr
        if (len(s) == 1): # edge case
            # print(len(s))
            return mapping[s]
        if (len(s) == 0):
            return 0

        chars = list(s)
        # print(chars)

        # iterate
        for curr in chars:
            if (prev == None): # skip rest of iteration
                prev = curr
                continue

            left = mapping[prev]
            right = mapping[curr]
            # print('compare: ', left, prev, " and ", right, curr)

            if (left < right):
                res -= left
            elif (left >= right):
                res += left
            
            prev = curr
            # print("result:", res)

        # print("result:", res + right)
        # return res + right
        return res + mapping[curr]

# @lc code=end

