#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def oneWordApart(base, target):
            ## replacement - aab, aac
            found = False
            if len(base) == len(target):
                for i in range(len(target)):
                    if target[i] != base[i]:
                        if found == True:
                            return False
                        else:
                            found = True
                return True # if not more than one difference

            ## if not equal, increment the shorter one
            # addition - aa_a, aaba
            # deletion - aab, aa_
            if abs(len(target) - len(base)) == 1:
                # pick shorter string
                if len(target) <= len(base):
                    shorter = target
                    longer = base
                else:
                    shorter = base
                    longer = target
                # print(shorter, longer)

                for i in range(len(shorter)):
                    if found == True:
                        if shorter[i] != longer[i+1]: # aaba, aac
                            return False
                    elif found == False and shorter[i] != longer[i]:
                        found = True

                return True # if not more than one difference
            
            # didn't trigger a correct condition
            return False
        
        # create one word mappings
        tracking = dict.fromkeys([beginWord] + wordList, None) # { key: [] }
        for base in tracking:
            result = []
            for elem in wordList:
                if oneWordApart(base, elem) and base != elem:
                    result.append(elem)
            tracking[base] = result
        # print(tracking)
            
        # dfs (find shortest path) search with levels from start -> end
        def dfs(node, minlength):
            paths = []
            resultpath = None
            
            def search(path, node):
                children = tracking[node]
                # print(path, node, children)

                ### prune out the already visited nodes
                for child in children:
                    if child not in path: # don't revisit any nodes
                        # print(path + [child])
                        if child == endWord:
                            paths.append(path + [child])
                            # return len(path + [child])
                        else:
                            search(path + [child], child)

            search([], beginWord)
            
            # pick min of results that returns a proper results
            minlength = float('inf')
            for combo in paths:
                if len(combo) < minlength:
                    minlength = len(combo)
            
            if minlength == float('inf'):
                return 0
            return minlength + 1

        return dfs(beginWord, 1)

# @lc code=end

