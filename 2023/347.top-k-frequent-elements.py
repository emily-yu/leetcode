#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        letters = {}
        for elem in nums:
            if elem in letters:
                letters[elem] += 1
            else:
                letters[elem] = 1
        # print("letters:", letters)
        # print("letterstup: ", list(letters.items()))
        # print("sortedletterstup:", sorted(list(letters.items()), key=lambda x: x[1], reverse=True))
        result = []
        for elem in sorted(list(letters.items()), key=lambda x: x[1], reverse=True):
            result.append(elem[0])
        return result[0:k]
        '''
        res = list(letters.values())
        print("res:", res)
        res.sort()
        print("res:", res)
        res = res[-k:]
        print("res:", res)
        # rev2 = []
        count = 0
        rev = {}
        # count = 0
        for (key, val) in letters.items():
            rev[val] = key # swap
        print("rev:", rev)

        # result = []
        # for val in res:
        #     result.append(res[val])# = rev[val] # swap
        #     # count += 1
        #     # print(count)
        # # print(res)
        # return result
        for i in range(len(res)):
            res[i] = rev[res[i]]
        return res
        '''

        
# @lc code=end

