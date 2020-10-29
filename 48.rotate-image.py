#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # note: coded up logic after looking at discussion board

        # 1 - swap symmetrically across diagonal so that 123 becomes the first column
        # leftIndent = 0
        n = len(matrix)
        # for i in range(len(matrix)):
        for i in range(n):
            # indent (to only iterate top side of diagonal) adds 1 per line, so same as i
            # for j in range(i, len(matrix[i])):
            for j in range(i, n):
                # print(matrix[i][j], matrix[j][i])
                # print()
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # print(matrix)
        # 2 - swap elements in individual rows to swap order of columns (since 123 should be last column)
        # for i in range(len(matrix)):
        for i in range(n):
            # for j in range(len(matrix)):
            # print("new row: ", matrix[i])
            left = 0
            right = len(matrix[i]) - 1
            while (left <= right):
                # print("left: ", left, " right: ", right, matrix[i][left], matrix[i][right])
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
                # print(matrix)
            # print()
# @lc code=end

