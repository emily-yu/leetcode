#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        left = 0
        right = len(height) - 1
        while left <= right: 
            # print(height[left], height[right])
            # if height[left] < height[right]:
            dist = abs(right - left)
            if height[left] <= height[right]:
                # larger one * smaller one will be greatest
                # so smaller one adjust to see if will be larger than larger one
                # so if they are equal, what happens? should be either
                box = height[left] * dist
                left += 1
            else:
                box = height[right] * dist
                right -= 1
            if maxarea < box:
                maxarea = box
        return maxarea
# @lc code=end

