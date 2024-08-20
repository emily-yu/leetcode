#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    '''
    265/265 cases passed (44 ms)
    Your runtime beats 43.3 % of python3 submissions
    Your memory usage beats 100 % of python3 submissions (14.2 MB)
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return      
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        # check if is already max descending - if yes, reverse all elements
        numsort = sorted(nums) # for utility later
        if sorted(nums, reverse=True) == nums:
            for i in range(len(nums)):
                nums[i] = numsort[i]
            return

        # while the element is not the largest of its "rest", pick the next largest after it and sort rest of eements ascending
        '''
        shorthand: [1, 2, 3] -> [1, 3, 2]: 2 is not the largest of [3, 2]
        [1, 2, 3]
            [1] + [2, 3]=not perfect descent and 1 < 2
            [1] + [2] + [3]=perfect descent and 2 < 3 **swap requires perfect descent**
                (swap in min element greater than 2=3) [1] + [2=3] + [3=2]
                if len > 1: sorted last element: NO
        ======
        [1, 1, 5] -> [1, 5, 1]
            [1] + [1, 5]=not perfect descent and 1 = 1
            [1] + [1] + [5]=perfect descent and 1 < 5
                (swap in min element greater than 1) [1] + [1=5] + [5=1]
                if len > 1: sorted last element: YES         
        ======
        shorthand: [5,4,7,5,3,2] -> [5,5,2,3,4,7]: after 4, rest is perfectly descending, so replace 4 with next greatest element
            [5] + [4]=rest is not perfect descend: [7, 5, 3, 2]=perfect descend
                pick next element gratest element
            if [5] + [7, 5, 4, 3, 2], rest=perfect descend, then need to replace base
                = [5] + [7] + [5, 4, 3, 2]
        [5, 4, 7, 5, 3, 2]
            [5] + [4, 7, 5, 3, 2]=not perfect descent and 5 > 4
            [5] + [4] + [7, 5, 3, 2]= perfect descent and 4 < 7 
                (swap in min element greater than 4=5) [5] + [4=5] + [7, 5=4, 3, 2]
                if len > 1, sorted last element: YES = sorted([7, 5=4, 3, 2]) = [2, 3, 4, 7]
                [5] + [4] + [2, 3, 4, 7]
        =======       
        shorthand[7, 5, 1, 2] -> [7, 5, 2, 1]
            [7] + [5, 1, 2] = [7] + [5] + [1, 2] is not perfect descent
            sort [1, 2] and done
        [7, 5, 1, 2]
            [7] + [5, 1, 2]=not perfect descent and 7 > 5
            [7] + [5] + [1, 2]=not perfect descent and 5 > 1
            [7] + [5] + [1] + [2]= perfect descent and 1 < 2 
                (swap in min elem greater than 1=2) = [7] + [5] + [1=2] + [2=1]
                if len > 1, sorted last element: NO
        =======
        [7, 5, 3, 1, 2] -> [7, 5, 3, 2, 1]
            [7] + [5, 3, 1, 2]=not perfect descent but 7 > 5
            [7] + [5] + [3, 1, 2]= not perfect descent and 5 > 3
            [7] + [5] + [3] + [1, 2]=not perfect descent and 3 > 1
            [7] + [5] + [3] + [1] + [2]=last elem and 1 < 2
                (swap in min elem greater than 1=2) [7] + [5] + [3] + [1=2] + [2=1]
                if len > 1, sorted last element: NO
        =======
        [2,2,0,4,3,1]
        =======
        [1, 3, 2]
            [1] + [3, 2]=perfect descent and 1 > 3
                (swap in min elem greater than 1=2) [1=2] = 
        '''
        
        ind = 0
        while ind != len(nums):
            # base = nums[0:ind]
            # print("base: ", base, nums[ind: len(nums)])
            baseElem = nums[ind]
                    
            perfectDescent = True
            # check if current iteration is not perfect descent for rest of elements
            # print(base, nums[ind:len(nums)])
            for i in range(ind + 1, len(nums)):
                # print(nums[i-1], nums[i])
                if (nums[i-1] < nums[i]): # if len(1), always perfect descent
                    # print("not perfect descent, keep splicing", nums[i: len(nums)])
                    perfectDescent = False
                    break
                # else: perfect descent at the moment
            
            if perfectDescent:
                # print(nums[ind], nums[-1], ind)
                if ind == len(nums) - 1: # last element, just check if need to swap
                    # print("last element")
                    if nums[ind-1] < nums[ind]:
                        nums[ind], nums[ind-1] = nums[ind-1], nums[ind]
                        # print(nums)
                    return

                # print("perfect descent, check if ", nums[ind], " < ", nums[ind+1])

                # find the minimum element greater than the baseElem in rest of indexes
                minDiff = 999
                minInd = ind
                for j in range(ind, len(nums)):
                    diff = nums[ind-1] - nums[j]
                    # print((nums[j], diff))
                    # pick closest diff to 0 that is <0
                    if diff < 0 and abs(minDiff) > abs(diff):
                        minDiff = diff
                        minInd = j
                        # print("selectval: ", nums[j], nums[ind-1], (ind, j))
                        # print((minInd, minDiff))

                # swap
                # print(nums)
                nums[minInd], nums[ind-1] = nums[ind-1], nums[minInd]
                # print("swap ", nums[minInd], nums[i-1])
                # print(nums)

                # sort the rest
                nums[ind:len(nums)] = sorted(nums[ind:len(nums)])
                return
            
            ind += 1

# @lc code=end

