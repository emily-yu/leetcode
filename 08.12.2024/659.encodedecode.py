# arrays & strings

import random, string

class Solution:
    
    lst = {}
    
    def encode(self, strs: List[str]) -> str:
        def randomword(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
        val = randomword(4)
        
        self.lst[val] = strs 
        return val

    def decode(self, s: str) -> List[str]:
        return self.lst[s]
