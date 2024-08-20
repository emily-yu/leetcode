#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    '''
    Your runtime beats 91.91 % of python3 submissions
    Your memory usage beats 94.85 % of python3 submissions (15.8 MB)
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        result = []
        left = None
        right = None
        for i in range(len(intervals)):
            if left is None: # first range
                left = intervals[i][0]
                right = intervals[i][1]
            else: # compare to first range
                new = intervals[i]
                # print(new, (left, right))

                # not overlapping: (reset)
                # print(new[0], ">", left)
                # print(new[1], "<", right)
                if new[0] > right or new[1] < left:
                    # print("add")
                    # add to result
                    result.append([left, right])
                    # reset
                    left = new[0]
                    right = new[1]
                else:
                    # if overlapping (merge)
                    if new[1] > right: # right boundary greater than current right
                        right = new[1]
                        # print("new right: ", right)
                    if new[0] < left: # left boundary less than current left
                        left = new[0]
                        # print("new left: ", right)
        # print(left, right)
        if [left, right] not in result:
            result.append([left, right])
        return result
# @lc code=end

