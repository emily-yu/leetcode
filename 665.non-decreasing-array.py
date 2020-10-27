#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        prev = None
        flipped = None
        removeFirst = False
        removePrev = False
        for i in range(len(nums)):
            if prev == None:
                prev = nums[i]
            elif prev > nums[i] and flipped == None:
                # print("1")
                flipped = True

                removeFirst = nums[:i] + nums[i+1:]
                # print(removeFirst, sorted(removeFirst))
                if sorted(removeFirst) == removeFirst:
                    # print("isSorted removeFirst")
                    removeFirst = True
                    break

                removePrev = nums[:i-1] + nums[i:]
                # print(removePrev, sorted(removePrev))
                if sorted(removePrev) == removePrev:
                    # print("isSorted removePrev")
                    removePrev = True
                    break

                # print(removeFirst, removePrev)
                if removeFirst == True or removePrev == True:
                    return True
                return False
            prev = nums[i]

        # at least one must be sorted
        # iterate through rest of elements
        # print(removeFirst, sorted(removeFirst))
        if flipped is None:
            return True
        # print("end", removeFirst, removePrev)
        if removeFirst or removePrev:
            return True
        return False


# @lc code=end

