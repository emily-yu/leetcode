#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        tracking = [0]*len(prices)
        # tracking[0] = 0
        minval = prices[0]
        # maxprofit = -999

        # for elem in prices:
        for i in range(1, len(prices)):
            elem = prices[i]
            if elem < minval:
                minval = elem
            if elem - minval > tracking[i-1]:
                tracking[i] = elem - minval
        # print(tracking)
        return max(tracking)

# @lc code=end

