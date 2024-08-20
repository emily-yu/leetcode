#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        tracking = [0] * len(seats)

        if seats[0] == 0: 
            tracking[0] = 0
        elif seats[0] == 1: 
            tracking[0] = -1

        zero_count = 0
        left = None # 1's markers
        right = None
        for i in range(0, len(seats)):
            # print(i, seats[i])

            # if beginning, just count zeros
            # if reached end, just replace zeros
            if seats[i] == 0:
                zero_count += 1

                # if is last element, just replace last element with zero_count because all previous ones will be smaller and not max distance
                if i == len(seats) - 1:
                    tracking[i] = zero_count
                else: # normal element, just pass over
                    tracking[i] = 0
            if seats[i] == 1:
                # if has another marker for 1 (aka not beginning of arr), left != None
                if left is not None:
                    right = i
                    temp = i # to keep place in array

                    # collapse inwards to make dist count
                    dist = 0
                    while (left <= right):
                        tracking[left] = tracking[right] = dist
                        dist += 1
                        left += 1
                        right -= 1

                    # reset left counter as new 1
                    left = temp
                    right = None
                    zero_count = 0

                # no marker for 1 yet (beginning of arr), left == None
                else:
                    left = i
                    if seats[i-1] == 0: # need to set max for previous
                        tracking[i-1] = zero_count
                        zero_count = 0

            # print(seats)
            # print(tracking)
            # print()

        return max(tracking)
# @lc code=end

