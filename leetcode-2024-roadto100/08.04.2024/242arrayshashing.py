class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # create hashes
        letters = {}
        lettert = {}
        for idx in range(0, len(s)):
            if s[idx] not in letters:
                letters[s[idx]] = 1
            else:
                letters[s[idx]] += 1
            
            if t[idx] not in lettert:
                lettert[t[idx]] = 1
            else:
                lettert[t[idx]] += 1
                
        return letters == lettert
