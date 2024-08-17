# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxs = 0
        for sent in sentences:
            sents = sent.count(' ') # apparently split is faster than count
            if sents > maxs:
                maxs = sents
        return maxs + 1