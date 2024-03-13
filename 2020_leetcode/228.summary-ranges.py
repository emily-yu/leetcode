#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        # solution 1
        # '''
        curr = nums[0]
        start = nums[0]
        i = nums[0]

        res = []
        ind = 0
        while (i <= nums[len(nums) - 1]):
            if curr == i:
                if start == None:
                    start = i
                i += 1
                # print(nums, i, nums[-1])
                if i <= nums[-1]:
                    curr = nums[ind + 1]
                    ind += 1
                    # print(curr)
            elif curr != i:
                if start == None:
                    i = curr
                elif start != None: # need to append, the current i is not found
                    # if the start element == the previous element
                    if start != i - 1: # other len
                        res.append(str(start)+ "->" + str(i - 1))
                    elif start == (i-1): # len 1
                        res.append(str(start))
                    start = None
                    i = curr

        # deal with last element
        if (start is None and curr is not None) or start == curr:
            res.append(str(curr))
        else:
            res.append(str(start)+ "->" + str(curr))

        # print(res)
        return res
        # '''

        # solution 2
        '''
        start_ind = 0
        left = nums[0]
        end_ind = len(nums) - 1
        right = nums[-1]
        # append (min, start_end) (end_ind, max)

        res = []
        while (start_ind <= end_ind):
            print(start_ind, end_ind)
            if start_ind == end_ind: # odd
                if abs(nums[start_ind] - nums[end_ind]) == 0: # combine ranges
                    print('append(left, right')
                    pass
            else: # even
                if abs(nums[start_ind] - nums[start_ind + 1]):
                    # next number
                    start_ind += 1
                else:
                    print('append (', left, start_ind, ')')
                    left = start_ind
                    start_ind += 1

                if (abs(nums[end_ind] - nums[end_ind - 1])) == 1:
                    end_ind -= 1
                else:
                    print('append(', end_ind, right, ')')
                    right = end_ind
                    end_ind -= 1

            print('(', left, start_ind, ')', '(', end_ind, right, ')')
        '''     

# @lc code=end

