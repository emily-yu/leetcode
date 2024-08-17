# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s = sorted(nums)[-k:]
        res = []
        for num in nums:
            if num in s: 
                res.append(num)
                s.remove(num)
        return res
