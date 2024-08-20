#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # edge cases
        # 1. empty arr nums
        if len(nums) == 0:
            return []
        # 4. if len(nums) == multiple of len(nums) == len(nums) * n, return original array
        elif k % len(nums) == 0: 
            print("edge case 4")
            print(k, len(nums), k % len(nums))
            return nums

        # 2. len(nums) < k
        # 3. len(nums) == k
        while (len(nums) <= k):
            print("edge case 2 or 3")
            k = k - len(nums)
            print("new k is ", k)

        sp = len(nums) - k # start pivot (k)
        ss = sp - k # start swap
        print("index: ", sp, ss, " element: ", nums[sp], nums[ss])

        # while (sp != 0):
        print("swapping")
        for i in range(0, k):
            print(nums)
            nums[sp + i], nums[ss + i] = nums[ss + i], nums[sp + i]
            print(nums)
            print()

        # swap to index starts
        print(sp, ss)
        sp, ss = ss, sp
        print(sp, ss)

        # if not k elements left 
        # if sp - k < 0:
        print(sp - k)
        # ex [2, 1, 3, 4, 5], k = 3. sp = 2, nums[sp] = 3. ss = 2 - 3 = -1, less than 0. need to select abs(sp - 3) number of elements
        # ex [1, 2, 6, 7, 8, 3, 4, 5], k = 3. sp = ind 2, val 6, ss = ind 5, val 3

        # ex [1, 2, 3, 4, 8, 9, 10, 5, 6, 7], k = 3. sp = ind 4, val 6, ss = ind 7, val 3
        # ex [1, 2, 3, 4, 8(sp), 9, 10, 5(ss), 6, 7]
        # ex [1, 2(ss), 3, 4, 8(sp), 9, 10, 5, 6, 7]
        ss = sp - k
        print("ss: ", ss)
        if ss < 0: # overgone
            print("ss over")
            sp = k - abs(ss)
            ss = 0
            print(ss, sp)
        # if select > 0:
        #     print("select > 1")
        #     print(ss)
        #     print(sp - select)
        #     ss = sp - select
        for i in range(0, k):
            print(nums)
            print("swap ", nums[sp + i], nums[ss + i])
            nums[sp + i], nums[ss + i] = nums[ss + i], nums[sp + i]
            print(nums)
            print()
        # else:
        #     print("select <= 1")
        #     print(nums)
        #     nums[sp], nums[ss] = nums[ss], nums[sp]
        #     print(nums)
        #     print()
        # if not perfectly divided
        print("-------------done---------------")

        
# @lc code=end

