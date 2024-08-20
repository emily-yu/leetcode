#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        CAP_OCCURANCE = len(nums) / 2
        print(CAP_OCCURANCE)

        left = 0
        right = len(nums) - 1
        print(left, right)

        track = {}

        while (left <= right):
            # if (left == right): # only performance check on one
                # pass
            leftVal = nums[left]
            if leftVal in track: # check if key in
                track[leftVal] += 1
            else:
                track[leftVal] = 1

            if track[leftVal] >= CAP_OCCURANCE:
                return leftVal

            left += 1

            if (left != right): # need to check the other side too
                # leftVal = nums[left]
                # if leftVal in track: # check if key in
                #     track[leftVal] += 1
                # else:
                #     track[leftVal] = 1

                rightVal = nums[right]
                if rightVal in track:
                    track[rightVal] += 1
                else:
                    track[rightVal] = 1
                
                # if track[leftVal] >= CAP_OCCURANCE:
                #     return leftVal
                # elif track[rightVal] >= CAP_OCCURANCE:
                if track[rightVal] >= CAP_OCCURANCE:
                    return rightVal
                
                # left += 1
                right -= 1
                

# @lc code=end

