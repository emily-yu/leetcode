#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False

        track = set()
        total = n # so if 1, it will just end it
        while total != 1:
            print(track)
            track.add(total)
            nums = list(str(total))
            total = 0

            for num in nums:
                total += int(num) * int(num)
                print(total)

            if total in track:
                return False

        return True
# @lc code=end

