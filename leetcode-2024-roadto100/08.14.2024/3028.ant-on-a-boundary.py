# arrays & hashing

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        base = nums[0]
        count = 0
        for i in range(1, len(nums)):
            base += nums[i]
            if base == 0: 
                count += 1
        return count