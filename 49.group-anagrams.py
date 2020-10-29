#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge cases
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]

        '''
        ["eat", "tea", "tan", "ate", "nat", "bat"]

        sort each O(m*n)
        ["ate", "ate", "ant", "ate", "ant", "abt"]

        want to create this structure
        {
            "ate": [0, 1, 3]
            "ant": [2, 4]
            "abt": [5]
        }
            get unique keys
            ("ate", "ant", "abt")

            iterate through and add to counts

        iterate through hashmap and add by index
        "ate"
            wordArr = []
            wordArr.append(strs[0])
            wordArr.append(strs[1])
            wordArr.append(strs[3])
        '''
        # convert into sorted words
        new = []
        for i in range(len(strs)):
            data = list(strs[i])
            data = sorted(data)
            data = ''.join(data)
            new.append(data)
        # print(new)

        tracking = dict()
        for ind, word in enumerate(new):
            if word in tracking:
                tracking[word].append(ind)
            else:
                tracking[word] = [ind]
        # print(tracking)

        result = []
        for key,val in tracking.items():
            # print(key,val)
            wordInd = []
            for ind in val: 
                wordInd.append(strs[ind])
            result.append(wordInd)
        # print(result)

        return result

        
# @lc code=end

