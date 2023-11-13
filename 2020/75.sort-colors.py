#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    '''
    48/87 cases passed (N/A)
    '''
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        
        '''
        (2) (0) 2 1 1 0 0 1 2
            i = 2, i+1 = 0

            check for 1 or 2 values
                i == 2: 2s = 0, 2e = 0
                i == 0: none

            2 > 0 = swap i, i+1 = i+1, i
            (0) (2) 2 1 1 0 0 1 2

        0 (2) (2) 1 1 0 0 1 2 
            i = 2, i+1 = 2
            check for 1 or 2 values
                i == 2 and i+1 == 2: 2s = 0, 2e = 1
                equal, no swap
            2 == 2: continue

        0 2 (2) (1) 1 0 0 1 2  
            i = 2, i+1 = 1
            check for 1 or 2 values
                i   == 2
                i+1 == 1

            2 > 1: swap with 2s, reset 2s/2e and 1s/1e
            0 (1) 2 (2) 1 0 0 1 2  

        0 1 2 (2) (1) 0 0 1 2  
            i = 2, i+1 = 1
            check for 1 or 2 values
                i   == 2
                i+1 == 1
            2 > 1: swap
            0 1 (1) 2 (2) 0 0 1 2

        0 1 1 2 (2) (0) 0 1 2
            2 > 0: swap with 2s
            0 1 1 (0) (2) (2) 0 1 2

        0 1 1 0 2 (2) (0) 1 2
            2 > 0: swap with 2s
            0 1 1 0 (0) 2 (2) 1 2
        
        0 1 1 0 0 2 (2) (1) 2 [key]
            i = 2, swap = i+1 = 1                           ind = 6, swapInd = 6+1 = 7
            2 > 1: swap with 2s                             swap values nums[swapInd], nums[2s=5]... swap indexes swapInd, 2s
            0 1 1 0 0 (1) 2 (2) 2

            swap = 1, swap-1 = 0 != 1; swap 1e+1            if nums[swapInd] != nums[swapInd - 1], not adjacent to own kind, swap again with 1e
            0 1 1 (0) 0 (1) 2 2 2 = 0 1 1 (1) 0 (0) 2 2 2   

        at the end, deal with the 0's
        0 1 1 1 0 0 2 2 2
            2 will always be at end because comparing 2 > 1
            for 1s=3 to 1e=1: 
                2s=6 to 2e=8:
                1startInd = 6 - 1 - (3-1) = start -> prevSpace -> spaceFor1's
                for 1s to 1e, set to 0

        ex) start with 1
        (1) 0 2 2 0 1
        0 (1) 2 2 0 1 
        0 1 (2) 2 0 1
        0 1 2 (2) 0 1
        0 1 0 2 (2) 1
        0 1 0 1 2 (2) + swap 1 to 1's
        '''

        s2 = None # start 2
        e2 = None

        if nums[0] == 2: # found first 2
            s2 = 0
            e2 = 0

        for i in range(len(nums) - 1):
            # else: 
            first = nums[i]
            second = nums[i+1]
            print("elements: ", first, second)
            print((s2, e2))
            
            if second == 2 and e2 is None:
                s2 = i+1
                e2 = i+1

            if first == 2 and second == 1:
                print(nums)
                nums[s2], nums[i+1] = nums[i+1], nums[s2] # values
                print(nums)

                # shift the 2's over right
                s2 += 1 # indexes
                e2 += 1
            
            if first == second:
                if first == 2:
                    e2 += 1

            # simple swap
            if second == 0: 
                if first == 1:
                    nums[i], nums[i+1] = nums[i+1], nums[i] # values
                if first == 2:
                    nums[s2], nums[i+1] = nums[i+1], nums[s2] # values
                    s2 += 1
                    e2 += 1
            print(nums)

        if 1 not in nums:
            return

        startInd = nums.index(1)
        endInd = len(nums) - 1 - nums[::-1].index(1)

        # if 0, 1
        if s2 is None: # no 2's
            s2 = len(nums)

        # if 0, 1, 2
        numbOnes = endInd - startInd + 1
        numbZero = s2-1-endInd
        # numbOnes = endInd - startInd + 1
        print("zeros to right: ", s2 - 1 - endInd)
        print("ones: ", numbOnes)

        # if numbOnes % 2 == 1:
        #     nums[endInd] = 1

        # for i in range(0, s2-1-endInd):
        #     print(endInd - i - 1, endInd + i + 1)
        #     if endInd - i - 1 >= 0: # process
        #         nums[endInd - i - 1] = 0
        #         print("1")
        #     nums[endInd + i + 1] = 1
        #     print("2")

        for i in range(s2 - 1, -1, -1):
            if numbOnes > 0:
                nums[i] = 1
                numbOnes -= 1
            # if nums[i] == 0: 
            #     break
            # print(i)
            else:
                nums[i] = 0
            

        # if 0, 2: nothing
        # if 1, 2: nothing
            
            
            # if more than one element
        # no blank spaces to the right
        print("=================================================NUMS: ", nums)

        
        
        
        

        



# @lc code=end

