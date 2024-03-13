#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # nums = [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
        # nums = [0, 1]

        # edge cases
        if len(nums) == 0 or len(nums) == 1:
            return 0

        cts = []
        count = 1
        for ind in range(len(nums) - 1):
            if nums[ind] != nums[ind+1]:
                cts.append(count)
                count = 1
            else:
                count += 1
        cts.append(count)

        # edge case
        if len(cts) == 2:
            return min(cts) * 2

        # tracking for comparison
        i = 0
        itermax = 0
        maxmax = 0

        # comparison logic 
        while (i < len(cts) - 1):
            print(cts[i], cts[i+1])

            # consider 2 element case: keep adding equal pairs
            # if not equal pairs, consider a 3 elem window (1, 0, 1 or 0, 1, 0)
                # if leftct < rightct: consider extra right elem
                # if rightct < leftct: consider extra left elem
                
        print(maxmax)
        print(cts)

        return maxmax
        
        
# @lc code=end

