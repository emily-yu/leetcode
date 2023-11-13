#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # # edge cases
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]

        # # create sorted list = nlogn
        # sort = sorted(nums)

        # # index hashmap of original list for indexes key=sorted, val=orignianl
        # indexes = dict()
        # for i in range(0, len(sort)):
        #     print(i, sort[i], nums[i])
        #     indexes[i] = nums[i]
        
        # print(indexes) # indexes of nums in elems (0=index, 1=value)

        # # return

        # print(sort, indexes)
        # # add in descending order in sorted list items that don't violate adjacency
        # total = None
        # ind = len(sort) - 1
        # for elem in reversed(sort):
        #     print("-----------------")
        #     print("elem ", elem)
        #     print("true index: get index in nums of elem", indexes[ind])
            
        #     # if no start value yet (no adjacents to check)
        #     if total == None:
        #         # add elem value
        #         total = elem
        #         # remove index from dictionary
        #         indexes.pop(ind)
        #         print(sort, ind, indexes)
            
        #     else:
        #         # check if any items are adjacent

        #         print(ind, indexes)
        #         # if end element
        #         if ind == len(sort) - 1:
        #             if ind-1 not in indexes:
        #                 print(ind-1, "not in indexes")

        #                 ind -= 1
        #                 print("new ind", ind)
        #                 continue
        #             else:
        #                 total += elem
        #                 indexes.pop(ind)
        #                 print("new total: ", total)

        #         # if start element
        #         if ind == 0:
        #             if ind+1 not in indexes:
        #                 print(ind+1, "not in indexes")
        #                 ind -= 1
        #                 print("new ind", ind)
        #                 continue
        #             else:
        #                 total += elem
        #                 indexes.pop(ind)
        #                 print("new total: ", total)
        #         else:
        #             if ind+1 not in indexes or ind-1 not in indexes:
        #                 print(ind+1, ind-1, "not in indexes")
        #                 ind -= 1
        #                 print("new ind", ind)
        #                 continue # don't add
        #             else:
        #                 total += elem
        #                 indexes.pop(ind)
        #                 print("new total: ", total)

        #         print('asdf')
        #         # if none:
        #         # add elem value
        #         # remove index from dictionary
        #     # next element in sorted
        #     ind -= 1
        #     print("new ind", ind)
            
        # return total

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        maxes = [0] * len(nums)

        # case n = 1
        maxes[0] = nums[0]
        maxes[1] = max(maxes[0], nums[1])
        for i in range(2, len(nums)):
            # (i-1) means set up a new maximum chain because (i-1) overwhelms it all
            # (i-2) + nums[i] adds nums[i] on to the previous valid adjacent maxes
            maxes[i] = max(nums[i] + maxes[i - 2], maxes[i - 1])
            print(i, maxes)

        return maxes[-1]





# @lc code=end

