#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        sort = sorted(nums) # leave nums unaffected for converting

        # assign indexes: 0(n/2)
        search = True
        while (search):
            res = sort[start] + sort[end]
            if (res == target):
                search = False
            
            elif (res > target):
                end -= 1
            elif (res < target):
                start += 1
        
        # convert back
        ind = 0
        res = [-1, -1]
        for elem in nums:
            # print(elem, ind, sort[start], sort[end])
            if elem == sort[start] and res[0] < 0: # start index found, start ind not assigned
                # print("assign start")
                res[0] = ind
            elif elem == sort[end] and res[0] != ind and res[1] < 0: # end index found, not dupicate from start, and end is unassigned
                # print("assign end")
                res[1] = ind
            ind += 1

        return res

# @lc code=end

