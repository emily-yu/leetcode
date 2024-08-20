#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        def add(first, second, third, ind):
            nextres = first + second + third
            if ind == n:
                return nextres
            return add(second, third, nextres, ind+1)

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return add(0, 1, 1, 3)

# @lc code=end

