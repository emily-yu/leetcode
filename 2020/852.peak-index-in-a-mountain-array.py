#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev = -1
        for i in range(0, len(arr)):
            print(i, arr[i], prev)
            if arr[i] > prev:
                prev = arr[i]
                i += 1
            else:
                return i - 1
        return len(arr) - 1
# @lc code=end

