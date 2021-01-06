#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:

        # S = "aabbcccbddddd"
        
        tracking = {}
        for elem in S:
            if elem in tracking:
                tracking[elem] += 1
            else:
                tracking[elem] = 1
        print(tracking)

        choices = list(tracking.keys())
        print(choices)

        result = ""

        while len(choices) > 1:
            print('1: ', tracking, choices)
            minkey = min(tracking, key=tracking.get)
            result += ''.join(choices) * tracking[minkey]

            print('2: ', minkey)
            
            # subtract
            temp = list(choices)
            subtract = tracking[minkey]
            for elem in choices:
                tracking[elem] -= subtract
                print('3: ', elem, tracking[elem], choices, temp)

                # remove if null
                if tracking[elem] <= 0:
                    idx = temp.index(elem)
                    temp.pop(idx)
                    tracking[elem] = 9999

            choices = temp
            print('4: ', result, tracking, choices)

        print(choices)
        for elem in choices: # place the rest of elements
            for iter in range(tracking[elem]):
                print("elem to search: ", elem, iter)
                for i in range(len(result)-1):
                    # print(i, i+1)
                    if result[i] != elem and result[i-1] != elem:
                        print(result[i], result[i+1])

                        tracking[elem] -= 1
                        if tracking[elem] == 0:
                            print("done")
                            print(result)
                            result = result[:i] + str(elem) + result[i:]
                            print(result)
                            break
            print('after: ', result)
        
        for elem in choices:
            print(elem, tracking[elem])
            if tracking[elem] > 0 and tracking[elem] != 9999:
                return ""
        return result
                # if won't work
                # return ""

# @lc code=end

