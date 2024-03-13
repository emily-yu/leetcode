#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # time limit exceeded
        if len(height) == 0 or len(height) == 1:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])

        def getMaxWater(ind):
            track = []
            for i in range(ind, 0, -1):
                track.append(i)
            track.append(0)
            for i in range(1, len(height) - ind):
                track.append(i)

            for i in range(len(track)):
                track[i] = track[i] * min(height[i], height[ind])

            return max(track)

        curr_max = 0
        i = 0
        for num in height:
            val = getMaxWater(i)
            if val > curr_max: 
                curr_max = val
            i += 1

        return curr_max
# @lc code=end

