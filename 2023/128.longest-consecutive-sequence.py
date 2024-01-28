#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)

        # hashmapify for tracking 
        mapify = {}
        for num in nums: 
            # mapify[num] = 1
            if num not in mapify:
                mapify[num] = 1 # account for doubles

        # globalmax
        globalmax = 1
        # if next elem exists, +1 for currmax & update in hashmap
        for num in mapify:
            print(num)
            print(mapify)
            if num+1 in mapify: 
                # mapify[num] += mapify[num+1]
                mapify[num+1] += mapify[num] # update for consecutive next
                if mapify[num+1] > globalmax:
                    globalmax = mapify[num+1] # update if new globalmax
                    print("globo: ", globalmax)
            else: 
                mapify[num] = 1
        print(mapify)
        return globalmax
        # return globalmax
    
# @lc code=end

