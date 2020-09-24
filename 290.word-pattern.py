#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        count = 0
        pattern_res = str()
        mapping = dict()
        for i in range(len(pattern)):
            word = pattern[i]
            if word not in mapping.values():
                mapping[word] = count
                count += 1
        # print(mapping)
        for word in pattern:
            pattern_res += str(mapping[word])
        # print(pattern_res)

        count = 0
        s_res = str()
        mapping = dict()
        for i in range(len(s)):
            word = s[i]
            if word not in mapping.values():
                mapping[word] = count
                count += 1
        # print(mapping)
        for word in s:
            s_res += str(mapping[word])
        # print(s_res)

        if s_res == pattern_res:
            return True
        return False
            
# @lc code=end

