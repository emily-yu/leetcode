#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Accepted
        21/21 cases passed (96 ms)
        Your runtime beats 83.3 % of python3 submissions
        Your memory usage beats 20.92 % of python3 submissions (18.8 MB)
        '''
        
        if k == 0:
            return []
            
        tracking = {}
        # maxcount = -999
        # rankcount = 0

        # lastrank = None
        # lastrankcount = 1
        for elem in nums:
            if elem in tracking:
                tracking[elem] += 1
            else:
                tracking[elem] = 1
        # print(tracking)
        asdf = sorted(tracking.items(), key=lambda x: x[1])
        # print(asdf)
        
        result = []
        for i in range(k):
            result.append(asdf.pop()[0])
        return result
            

        
        

        
# @lc code=end

