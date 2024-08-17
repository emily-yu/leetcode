class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        i = 0
        result = []
        for word in words: 
            if x in str(word): 
                result.append(i)
            i += 1
        return result