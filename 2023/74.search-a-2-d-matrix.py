#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
                
        # condense together
        rows = [] 
        for row in matrix: 
            rows += row
        # print(rows)
        
        # edge case
        if len(rows) <= 3:
            for elem in rows:
                if elem == target:
                    return True

        left = 0
        right = len(rows) - 1
        # print(left, right)
        while left < right:
            if rows[left] == target or rows[right] == target: 
                return True
            
            mid = (left + right) // 2 # rounding op 
            if rows[mid] == target: 
                return True
            
            if target < rows[mid]: # use left 
                right = mid
            else: # use right
                left = mid + 1

            # print(left, right, mid) 
        return False

# @lc code=end

