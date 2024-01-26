#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        letters = {}
        i = 0
        s = None
        for word in strs: 
            s = ''.join(sorted(word)) #o(letters)^2
            if s in letters:
                letters[s].append(strs[i])
            else:
                letters[s] = [strs[i]]
            i+=1

        res = []
        for ana in letters: 
            res.append(letters[ana])
        
        return res
        
# @lc code=end

