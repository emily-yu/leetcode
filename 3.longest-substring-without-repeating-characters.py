#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        track = [0] * len(s)
        letters = list() # (index, letter)

        for i in range(len(s)):
            if s[i] in letters:
                
                # print("popping", s[i], " from ", letters)
                # fuuuck, .pop(0) is o(n), .pop() for last elem is o(1)
                while (letters.pop(0) != s[i]): # pop all the elements in back until dup
                    # print(letters)
                    pass

                track[i] = len(letters)
                # print("done popping")
            if s[i] not in letters:
                letters.append(s[i])
                track[i] = len(letters)
                # print(letters, track)

        # print(track)
        return max(track)

        # if len(s) == 0:
        #     return 0

        # track = [0] * len(s)
        # letters = {} # {index: letter}
        # start = 0
        # for i in range(len(s)):
        #     print(i, s[i])
        #     if s[i] in letters.values():
        #         # print("popping", letters[start], s[i], " from ", letters)
        #         # print(letters[start] != s[i])
        #         while letters[start] != s[i]:
        #             del letters[start]
        #             start += 1
        #             # print("start", start, letters, track)
        #         del letters[start]
        #         start += 1

        #         track[i] = len(letters)
        #         letters[i] = s[i]
        #         # print("done popping")
        #     elif s[i] not in letters:
        #         letters[i] = s[i]
        #         track[i] = len(letters)
        #         # print('not in, ', letters, track)

        # # print(track)
        # return max(track)

# @lc code=end

