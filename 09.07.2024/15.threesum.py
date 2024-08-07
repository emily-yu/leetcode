class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        exists = set()
        for elem in nums:
            exists.add(elem)

        result = list()
        start, end = 0, len(nums) - 1
        for i in range(start, len(nums) - 1): 
            for j in range(i, len(nums)):
                if i != j:
                    # check if 3rd element exists
                    tofind = 0 - (nums[i] + nums[j])
                    print(tofind)
                    if tofind in exists:
                        for n in range(j, len(nums)):
                            val = sorted([nums[i], nums[j], nums[n]])
                            if nums[n] == tofind and n != i and n != j and val not in result:
                                result.append(val)
        return result