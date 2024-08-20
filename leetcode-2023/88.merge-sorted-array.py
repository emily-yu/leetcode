#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        curr = 0
        j = 0
        i = m # start at first nonzero
        while curr != n: 
            jelem = nums2[j]
            print(curr, n, i, j, jelem)
            print(nums1)

            if jelem > nums1[i]:
                nums1[len(nums1)-curr-1] = jelem
                j += 1
            else:
                nums1[len(nums1)-curr-1] = nums1[i]
            
            nums1[i] = 0 # reset current for shifts
            i -= 1
            curr += 1







        
# @lc code=end

