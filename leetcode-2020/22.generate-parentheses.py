#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def permutations(curr: str, opened: int, closed: int):
            if len(curr) == n*2:
                return [curr]

            # recurse
            open_bracket = close_bracket = []
            if opened < n:
                open_bracket = permutations(curr + '(', opened + 1, closed)
            if closed < opened:
                close_bracket = permutations(curr + ')', opened, closed + 1)

            # return logic
            if open_bracket is not None and close_bracket is not None:
                return open_bracket + close_bracket
            elif open_bracket is not None and close_bracket is None:
                return open_bracket
            elif open_bracket is None and close_bracket is not None:
                return close_bracket
            return [] # if both null
        
        return permutations('', 0, 0)
            
            
# @lc code=end

