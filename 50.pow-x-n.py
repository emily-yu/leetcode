#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # # edge cases
        # if n == 0:
        #     return 1

        # # divide powers by 2 by squaring res
        # # (x^2)^5 = x^10
        # # (2^4)^5 = 2^20
        # # cases
        # basen = n
        # negative = False
        # if n < 0:
        #     n = -n
        #     negative = True

        # i = 1
        # base = abs(x)
        
        # while (n >= 1): # n = 1, n = 0
        #     n = n // 2
        #     base = base * base

        
        # # if negative
        # if negative:
        #     x = 1 / x

        # print(x)

        # return float('%6f'%x)

        # edge case 
        if n == 0: return 1 # zero exponent
        if  n < 0: return 1.0 / self.myPow(x, -n) # negative - recurse with fractional conversion -1/n, with a negative n instead in parameter (x, -n)

        if n % 2 == 0: # even scenario
            # split x^4 = recurse(x^(4//2) = x^2) * recurse(x^(4//2))
            return  self.myPow(x, n // 2) *  self.myPow(x, n // 2)
        else: # odd scenario
            # split x^5 = recurse(x^(5//2) = x^2) * recurse(x^(5//2) = x^2) * x (last one is because odd, need to add the difference)
            return  self.myPow(x, n // 2) *  self.myPow(x, n // 2) * x

# @lc code=end

