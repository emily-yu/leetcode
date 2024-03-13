#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        # generate letters
        for letter in s:
            # print(letter)
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        # print(letters)

        # removing for t
        for letter in t:
            # print(letter)
            if letter in letters:
                if letters[letter] == 1:
                    letters.pop(letter)
                else:
                    letters[letter] -= 1
            else:
                return False

        # check if len(letters) == 0 (meaning equal)
        # print(letters)
        if len(letters) == 0:
            return True
        return False
# @lc code=end

