#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        q = [(0, 0)] # (n, m)
        count = 0

        while len(q) > 0:
            root = q.pop(0)
            
            if root[0] == n-1 and root[1] == m-1:
                count += 1
            # else:
            else:
                if root[0] < n-1:
                    right = (root[0] + 1, root[1])
                    q.append(right)

                if root[1] < m-1:
                    down = (root[0], root[1] + 1)
                    q.append(down)

        return count

# @lc code=end

