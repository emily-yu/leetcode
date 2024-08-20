#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # print(strs)
        max_prefix = None

        for i in range(len(strs) - 1):
            # print(strs[i], strs[i+1])
            curr_prefix = ""

            if len(strs[i]) < len(strs[i+1]):
                to_use = strs[i]
            else:
                to_use = strs[i+1]

            for j in range(len(to_use)):
                if strs[i][j] == strs[i+1][j]:
                    curr_prefix += strs[i][j]
                else:
                    break
                
            # print("currpref: ", curr_prefix)
            if max_prefix is None or len(curr_prefix) < len(max_prefix):
                max_prefix = curr_prefix

        if max_prefix == None:
            return ""
        return max_prefix
# @lc code=end

