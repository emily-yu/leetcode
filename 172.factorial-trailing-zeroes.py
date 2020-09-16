#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # looped solution
        if n == 0:
            return 0

        total = 1
        for i in range(2, n+1):
            total = total * i

        total = list(str(total))

        if len(total) > 1:
            trailing = 0
            i = len(total) - 1
            while (total[i] == '0'):
                trailing += 1
                i -= 1
        elif len(total) == 1:
            if total != 0:
                return 0
            return 1

        return trailing

        # logical solution
        
# @lc code=end

