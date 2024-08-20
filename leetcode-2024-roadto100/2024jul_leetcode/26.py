class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 1
        
        m = {}
        for elem in nums:
            if elem not in m:
                m[elem] = 0 #filler

        i = 0
        for elem in m.keys(): 
            nums[i] = elem
            i+=1 
    
        return len(m)
        
        