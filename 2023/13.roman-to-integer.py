#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # static
        map = {
            "I": 1,
            "V" : 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        #edge
        if len(s) == 0: return 0
        if len(s) == 1: return map[s[0]]

        #checks
        prev = 0 #ind
        next = 1
        net = 0
        subtract = 0
        # running = True

        while (next < len(s)):
            prev_val = map[s[prev]]
            next_val = map[s[next]]

            # print("hello bitch", prev, next, net, subtract)
            # if next >= len(s):
            #     running = False
            #     if prev < len(s): # prev in range
            #         net += map[s[prev]]
            #     net += subtract # add any excess

            #condition
            if prev_val >= next_val: 
                #add
                net += prev_val
                #increment idx
                prev = next
                next += 1
            elif prev_val < next_val: 
                #sub
                subtract += prev_val
                net += next_val - subtract 
                subtract = 0
                #inc
                prev = next + 1
                next = prev + 1
            
        if prev < len(s): # prev in range
            net += map[s[prev]]
        net += subtract # add any excess
        return net

        
# @lc code=end