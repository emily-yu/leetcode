#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # brute force o(n)
        start = -1
        end = -1
        ind = 0
        for elem in nums:
            if elem == target:
                if start == -1:
                    start = ind
                else:
                    end = ind
            ind += 1

        if start != -1 and end == -1:
            end = start # only one occurance

        return (start, end)
                
# @lc code=end

