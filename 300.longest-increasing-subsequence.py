#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        '''
        Accepted
        54/54 cases passed (9212 ms)
        Your runtime beats 5 % of python3 submissions
        Your memory usage beats 63.95 % of python3 submissions (14.6 MB)
        '''
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        # nums = [0,1,0,3,2,3]
        # nums = [7,7,7,7,7,7,7]

        tracking = len(nums) * [1]
        start = 0
        end = 1
        while end < len(nums):
            if start == end: # done
                start = 0
                end += 1
            
            # check all subarrays
            else:
                if nums[start] < nums[end]:
                    tracking[end] = max(tracking[end], tracking[start] + 1)
                start += 1
        
        # print(tracking)
        return max(tracking)
            
            
# @lc code=end

