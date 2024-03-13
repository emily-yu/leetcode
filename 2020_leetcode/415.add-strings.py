#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # print(num1, num2)
        # print(len(num1), len(num2))
        diff = len(num1) - len(num2)
        if diff > 0:
            # print("1")
            num1, num2 = num2, num1 # swap if in assumptions

        # make shorter one equal length
        num1 = ("0" * (abs(diff))) + num1
        # print(":diff", diff, shorter, longer)

        carry = 0
        result_str = ""
        for i in range(len(num2), 0, -1): # assume num2 is the longer1
            # print(int(shorter[i-1]), int(longer[i-1]))
            result = int(num1[i-1]) + int(num2[i-1])
            if carry:
                result += 1
                carry = 0
            
            if result > 9: # not end
                carry = 1
                result -= 10

            result_str = str(result) + result_str

        if carry: # last element
            result_str = "1" + result_str
        
        # print(result_str)
        return result_str

# @lc code=end

