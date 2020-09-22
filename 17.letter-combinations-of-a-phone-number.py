#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs',
            '8': 'tuv', 
            '9': 'wxyz'
        }
        
        res = []
        totalNum = 1
        for digit in digits:
            totalNum *= len(mapping[digit])
        # print('totalNum ', totalNum)

        cycle = 0
        totalCycle = totalNum
        for digit in digits:
            if digit == 1:
                pass
            else:
                # print(totalCycle, " for ", digit)
                if len(res) == 0: # need to init the base
                    totalCycle = totalCycle // len(mapping[digit])
                    for i in range(0, len(mapping[digit])):
                        res += [mapping[digit][i]] * totalCycle
                else:
                    cycle = totalCycle // len(mapping[digit])
                    # print("cycle ", cycle, cycle * len(mapping[digit]))
                    ind = 0

                    # every cycle elements, need to switch characters - otherwise, just keep appending same
                    while (ind < totalNum):
                        for char in mapping[digit]:
                            for i in range(cycle): # 9 additions
                                res[ind] += char
                                ind += 1
                            # mapping_digit += 1 # next char after cycle completed
                    
                    totalCycle = cycle
            # print(res)
            
        return sorted(res)

# @lc code=end

