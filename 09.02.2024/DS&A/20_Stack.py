class Solution:
    def isValid(self, s: str) -> bool:
        
        # edge case
        if len(s) < 2:
            return False

        # tracking
        stack = []
        idx = 0
        found = False
        pairs = { # checked when right one
            ']': '[', 
            ')': '(',
            '}': '{'
        }
        # loop through
        while (idx < len(s)):
            char = s[idx]

            # check if left or right
            if char in ('[', '(', '{'): #L
                stack.append(char)
            if char in (']', ')', '}'): #R
                if len(stack) == 0:
                    return False
                    
                pop = stack.pop()
                if pop != pairs[char]:
                    return False
            idx += 1

        # if at end - if leftover R then false
        if len(stack) > 0:
            return False
        return True 