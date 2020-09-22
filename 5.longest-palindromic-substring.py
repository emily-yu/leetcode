#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindromeFromPivot(left, right, s):
            if (s == None):
                return 0
            if left > right:
                return 0

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right-left-1 # length of string

        curr_max = 0

        pivot1 = 0
        pivot2 = 0

        case1, case2 = 0, 0
        for i in range(0, len(s)):
            # if midpoint % 1 == 0: #even case
            case1 = findPalindromeFromPivot(i, i, s)
            # else: # odd case
            case2 = findPalindromeFromPivot(i, i+1, s)
            # pick new case if its better
            if case1 > curr_max:
                curr_max = case1
                pivot1 = i
                pivot2 = i
            if case2 > curr_max:
                curr_max = case2
                pivot1 = i
                pivot2 = i+1
        
        lnmax = findPalindromeFromPivot(pivot1, pivot2, s)
        print(lnmax, pivot1, pivot2)
        if pivot1 != pivot2: # even case
            lnmax = lnmax - 2 # remove the two indexes core
            expansion = lnmax // 2 # guarenteed whole number
            for i in range(expansion):
                pivot1 -= 1
                pivot2 += 1
            print(pivot1, pivot2)
        elif pivot1 == pivot2: # odd case
            lnmax = lnmax - 1 # remove the one index core
            expansion = lnmax // 2 # guarenteed whole number
            for i in range(expansion):
                pivot1 -= 1
                pivot2 += 1
            print(pivot1, pivot2)

        return s[pivot1:pivot2+1]

# @lc code=end

