#
# @lc app=leetcode id=1160 lang=python
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # edge cases
        if len(chars) == 0: return 0

        count = 0
        # count chars map
        base = {}
        for char in chars:
            if char in base:
                base[char] += 1
            else:
                base[char] = 1

        # count chars map for each word
        for word in words:
            # if len of word > chars then it's doomed
            map = dict(base)
            valid = True

            # char types
            for char in word:
                if char in map:
                    map[char] -= 1
                else:
                    valid = False

            # any negative
            # print(map)
            for elem in map:
                if map[elem] < 0:
                    valid = False

            if valid:
                # print(word)
                count += len(word)
                
        
            
        return count
        # alt, sort each and if they match then ya
# @lc code=end

