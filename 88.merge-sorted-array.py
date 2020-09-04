#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # edge case, nothing to add
        if (m == 0):
            # nums1 = nums2
            i = 0
            while (i != len(nums2)):
                if nums1[i] == 0:
                    nums1[i] = nums2[i]
                else:
                    nums1.append(nums2[i])
                i += 1
            # print(nums1, nums2)
            return
        elif (n == 0):
            # print(nums1, nums2)
            return

        ind1 = 0
        ind2 = 0
        nums2_remaining = n
        stack = list()

        # while there are remaining elements in stack to add
        while len(stack) > 0:
            # compare where stack elements go to nums2 only
            if nums2_remaining > 0 and nums2[ind2] <= stack[len(stack) - 1]:
                # swap (top of stack) into place of num1
                nums1[ind1] = nums2[ind2]
                nums2_remaining -= 1
                ind2 += 1
            elif ind1 <= m and nums1[ind1] > stack[len(stack) - 1]:
                    stack.append(nums1[ind1])
                    nums1[ind1] = stack.pop(0)
            else:
                ind = 0
                for elem in nums1:
                    if (elem == 0):
                        if len(stack) == 0:
                            break
                        nums1[ind] = stack.pop(0)  
                    ind += 1        
            # ind1++
            ind1 += 1
        
        # if there is left nums2 elems
        while ind2 < n:
            ind = 0
            for elem in nums1:
                if (elem == 0):
                    if ind2 == n:
                        break
                    nums1[ind] = nums2[ind2]
                    ind2 += 1 
                ind += 1   

# @lc code=end

