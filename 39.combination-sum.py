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

        res = list()
        # def asdf(l):
        #     return dict((x,l.count(x)) for x in set(l))
        def helper(curr, res):
            complement = target - sum(curr)

            # if hits target
            if complement == 0:
                # print("DONE: ", curr)
                # compare against every other element to make sure doesn't exist
                for elem in res: 
                    if sorted(elem) == sorted(curr):
                        return []
                res.append(curr)
                # print(res)
                return curr

            # if beyond target
            # if complement < 0:
            #     return []

            # if still has room to add elements
            # print("helper(",curr, ")", "total: ", total, " complement: ", complement)
            if complement > 0:
                for elem in candidates:
                    asdf = helper(curr + [elem], res)

            return res

        permutations = helper(res, list())
        return permutations

# @lc code=end

