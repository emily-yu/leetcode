class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        # edge cases 
        if len(nums) == 0 or len(nums) == 1:
            return False
        
        # loop
        tracking = set()
        for elem in nums:
            if elem in tracking:
                return True
            else:
                tracking.add(elem)
        
        # if all good
        return False
        