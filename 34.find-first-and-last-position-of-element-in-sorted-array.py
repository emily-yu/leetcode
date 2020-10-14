#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # brute force o(n)
        '''
        start = -1
        end = -1
        ind = 0
        for elem in nums:
            if elem == target:
                if start == -1:
                    start = ind
                else:
                    end = ind
            ind += 1

        if start != -1 and end == -1:
            end = start # only one occurance

        return (start, end)
        '''

        def binarySearchHelper(elem, arr, start, end):
            if start > end:
                return -1
            mid = (start + end)//2
            if arr[mid] == elem:
                return mid
            elif arr[mid] > elem:
                # recurse to the left of mid
                return binarySearchHelper(elem, arr, start, mid - 1)
            else:
                # recurse to the right of mid
                return binarySearchHelper(elem, arr, mid + 1, end)

    
        mdpt = len(nums) // 2
        print("search ", nums, mdpt)

        ind = binarySearchHelper(target, nums, 0, len(nums) - 1)
        print(ind)
        right = ind

        if ind is not None:
            while ind > 0 and nums[ind - 1] == target:
                print(nums[ind])
                ind -= 1
            
            while right < len(nums) - 1 and nums[right + 1] == target:
                print(nums[ind])
                right += 1
            return (ind, right)
        
        # if ind is not found
        return (-1, -1)
# @lc code=end

