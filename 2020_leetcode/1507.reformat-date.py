#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        res = date[2] + '-'
        if months.index(date[1]) + 1 < 10:
            res += '0' + str(months.index(date[1]) + 1) + '-'
        else:
            res += str(months.index(date[1]) + 1) + '-'
        
        num = ''
        for letter in date[0]:
            if letter.isdigit():
                num += letter

        if len(num) == 1:
            num = '0' + num

        res += num  
        return res

 # @lc code=end

