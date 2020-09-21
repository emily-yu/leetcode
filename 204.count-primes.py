#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0

        tracking = [0] * n
        tracking[0] = -1 # 0 is not prime
        tracking[1] = -1 # 1 is not prime
        # print(tracking)

        # find square root
        root = 1
        squared = 1
        while (squared < n):
            squared = root * root
            root += 1
        root = root - 1 # lower it to the square that's under n

        # mark all multiples of these
        multiplier = 2
        for i in range(2, root): # start from 2, first prime
            # print(i)
            multiplier = 2
            while (multiplier * i < n):
                tracking[multiplier * i] = 1
                multiplier += 1

        # print(tracking)

        # count primes (above 2) that are marked as 0(prime) still
        count = 0
        for elem in tracking:
            if elem == 0:
                count += 1
        return count
# @lc code=end

