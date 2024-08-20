#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # index tracking
        start = 0
        end = -1

        maximum = 0 # overall maximum
        curr = 0 # current total

        ind = 0
        for elem in nums:
            if (elem >= maximum): # create a new arr
                start = ind # index tracking
                end = -1
                maximum = elem # value tracking
                curr = elem

            # creates a new maximum and is not overwhelmingly strong
            # cannot start a new array max on own
            elif (curr > maximum and elem < maximum):
                end += 1 # index updating
                curr += elem # value updating
                maximum = curr

            ind += 1
            

# @lc code=end

