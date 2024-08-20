#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        print(lst)
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        print(' '.join(lst))
        return ' '.join(lst)
# @lc code=end

