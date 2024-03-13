#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stk = sorted(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.stk.append(val)
        self.stk.sort()
        return self.stk[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

