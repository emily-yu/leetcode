#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #### bfs - time exceeded
        # q = [(0, 0)] # (n, m)
        # count = 0

        # while len(q) > 0:
        #     root = q.pop(0)
            
        #     if root[0] == n-1 and root[1] == m-1:
        #         count += 1
        #     # else:
        #     else:
        #         if root[0] < n-1:
        #             right = (root[0] + 1, root[1])
        #             q.append(right)

        #         if root[1] < m-1:
        #             down = (root[0], root[1] + 1)
        #             q.append(down)

        # return count

        #### dp - post looking at solutions
        # edge case - no extra paths
        if m == 1 and n == 1:
            return 1

        tracking = [[0] * n] * m
        # print(tracking)

        # edges are always one path
        for i in range(1, m):
            tracking[i][0] = 1
        tracking[0] = [1] * n
        tracking[0][0] = 0
        # print(tracking)

        # set the corner element to be max of diagonals
        for i in range(1, m):
            for j in range(1, n):
                print((i, j-1), (i-1, j), (i,j))
                tracking[i][j] = tracking[i][j-1] + tracking[i-1][j]
        # print(tracking)
        return max(max(tracking))
# @lc code=end

