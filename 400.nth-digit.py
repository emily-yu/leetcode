#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    '''
    Accepted
    70/70 cases passed (28 ms)
    Your runtime beats 73.27 % of python3 submissions
    Your memory usage beats 100 % of python3 submissions (14 MB)
    '''
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
            
        power = 0
        tens = 10**power
        val = len(str(tens)) # length value of each in power
        valLimit = val * tens * 9 # if exceeds, subtract and go onto next power

        # find range to search
        while (valLimit < n):
            print(valLimit, n)
            n -= valLimit

            # next level
            power += 1
            tens = 10 ** power
            val = len(str(tens))
            valLimit = val * tens * 9

        remainder = n % val
        completedNum = n // val # index in the range

        # search for the number in the range; completedNum = 1 is first number
        # find actual value of the number
        actual = tens + completedNum

        # corrections if index is 0, need to subtract 1 but would make it -1 so go to previous number
        if remainder == 0:
            actual -= 1
            return str(actual)[-1]
        else:
            strNum = str(actual)[remainder - 1]

        return strNum

        # (99-9)/2 = 90/2 = 45+10 = 55 - 1 = 54... if len(actual)=3 > len(completedNubmer)=2: add tens
        # (291-189)/3 = 30/3 = 10+100 = 110 - 1 = 109

# @lc code=end

