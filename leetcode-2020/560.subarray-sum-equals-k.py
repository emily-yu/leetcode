#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            if k == nums[0]:
                return 1

        # nums = [-1, 5, -6, 1, 2, 3]
        # k = 5

        # nums = [1, 1, 1]
        # k = 2

        # nums = [0,0,0,0,0,0,0,0,0,0]
        # nums = [0, 0, 0]
        # nums = [0, 0, 0, 0]
        # k = 0
        # answer = 55
        
        count = 0
        # prefix = []
        # sums = []
        # sums = set()
        sums = dict()
        for num in nums:
            # print(num)
            # print(prefix)

            # if k - num == 0:
            #     count += 1
            # if len(sums) == 0:
            #     sums[num] = 1
            # calculate sums
            # net = 0
            # if len(sums) == 0:
            #     sums = [num]
            # else:
            if len(sums) > 0:
                # get count to find
                # if k-num in sums:
                #     # cnt = sums.count(k - num)
                #     # count += cnt
                #     count += sums[k-num]
                #     print(sums[k-num])
                #     print('count', count)
                #     # print(cnt)

                # sums = set(x + num for x in sums)
                # i = len(sums)

                print('list of keys: ', sums.keys())
                print('current number: ', num)

                # number equal to the search target
                if k-num in sums:
                    toadd = sums[k-num]
                else:
                    toadd = 0
                # if the main element is to be added 
                if k-num == 0:
                    toadd += 1
                    print('adding 1.')

                print('adding', count)
                count += toadd

                # construct new sum dict
                print(sums)
                if num == 0: # the other sums will not change, just need to add a 0 to the count of elements
                    if 0 in sums:
                        sums[0] += 1
                    else:
                        sums[0] = 1
                else:
                    for elem in list(sums.items()):
                        print(elem)
                        sums[elem[0] + num] = elem[1]
                print(sums)

            # sums.append(num)
            if num not in sums:
            #     sums[num] += 1
            # else:
                sums[num] = 1

            print(sums, count)
            # prefix.append(num)
            # print('count', count)
            # print()

        return count
        
# @lc code=end

