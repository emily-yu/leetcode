#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        final = []
        for i in range(len(nums)):
            # baseElem = nums.pop(i) - doesn't work because pop gets RID of the index
            # would work if keep popping and use a while loop until len(nums) == 0
            # remainingNums = nums
            baseElem = nums[i]
            remainingNums = nums[:i]  + nums[i+1:]
            print(baseElem, remainingNums)

            # for each of the remainingNums, iterate through.
            # ex) [3, 2] = asdf(3), asdf(2)
            for numRes in self.permute(remainingNums):
                # build baseElem onto numRes
                print([baseElem], numRes)
                final.append([baseElem] + numRes)

        return final
# @lc code=end

