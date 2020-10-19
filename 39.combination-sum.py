#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return []
        if len(candidates) == 0 and target > 0: 
            return []

        # def asdf(l):
        #     return dict((x,l.count(x)) for x in set(l))
        def helper(curr, res):
            complement = target - sum(curr)

            # if hits target
            if complement == 0:
                # compare against every other element to make sure doesn't exist
                for elem in res: 
                    if sorted(elem) == sorted(curr):
                        return []
                res.append(curr)
                return curr

            # if still has room to add elements
            # print("helper(",curr, ")", "total: ", sum(curr), " complement: ", complement)
            # if complement > 0:
            for elem in candidates:
                # print(elem - sum(curr))
                if elem + sum(curr) <= target:
                    # print("helper(", curr + [elem], ")")
                    helper(curr + [elem], res)

            return res

        permutations = helper([], [])
        return permutations

# @lc code=end

