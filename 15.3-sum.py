#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Time Limit Exceeded
        # 315/318 cases passed (N/A)
        
        def twoSum(target, data):
            result = []
            compliment = []
            
            for elem in data:
                relative = target - elem
                if relative in data and (elem, relative) not in compliment and (elem, relative) not in result:
                    result.append(sorted([target*-1, elem, relative]))
                    compliment.append(sorted([target*-1, elem, relative], reverse=True))
            
            # print(compliment, result)
            return result

        ### twosum em all
        nums.sort()
        tuples = []
        for ind in range(len(nums)):
            if nums[ind] < 0:
                tuples += twoSum(-1 * nums[ind], nums[ind+1:])
            elif nums[ind] == 0:
                # print("zero case")
                pass
            else:
                tuples += twoSum(-1 * nums[ind], nums[:ind])

        # print(tuples)

        ### uniqueify
        result = []
        for elem in tuples:
            # print(elem)
            if elem not in result:
                result.append(elem)
        # print(result)
        
        ### verify counts
        counting = {}
        for elem in nums:
            if elem in counting:
                counting[elem] += 1
            else:
                counting[elem] = 1
        # print(counting)

        # zero case
        if 0 in counting and counting[0] >= 3:
            result.append([0, 0, 0])

        # compare counts
        ind = 0
        while ind < len(result):
            searching = True
            tup = result[ind]
            tupind = 0
            while searching and tupind < len(tup):
                number = tup[tupind]
                if tup.count(number) > counting[number]:
                    result[ind] = None
                    searching = False
                tupind += 1

            ind += 1
        
        # prune out
        result = [i for i in result if i] 

        # print(result)
        return result
# @lc code=end

