# two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # edge case
        if len(s) == 1:
            return True

        # perform string filter
        s = s.lower() # lowercase
        s = "".join(filter(str.isalnum, s)) # alphanumeric
        
        # perform check
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True


    