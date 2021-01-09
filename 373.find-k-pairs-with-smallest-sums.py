#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # test cases
        # k = 9

        # nums1 = [1,7,11]
        # nums2 = [2,4,6]
        # k = 3

        # nums1 = [1,1,2]
        # nums2 = [1,2,3]
        # k = 3

        # edge case 1
        if k == 0:
            return []

        # edge case; if either empty
        if nums1 == [] and nums2 == []:
            return []
        # else: # need to pull elements
        #     # pull first (add) elements
        #     tracking = [0] * len(nums1) + [1] * len(nums2)
        #     net = nums1 + nums2

        #     tracking = [x for _,x in sorted(zip(net,tracking))]
        #     net.sort()
        
        # pick elements
        # this shit is bad, makes it n^2
        result = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                rsum = nums1[i] + nums2[j]
                if rsum in result:
                    result[rsum].append([nums1[i], nums2[j]])
                else:
                    result[rsum] = [[nums1[i], nums2[j]]]

        ct = 0
        res = []
        for key in sorted(result):
            if ct > k:
                return res
            res += result[key]

        # if all possible pairs returned
        return res[:k]
        

# @lc code=end

