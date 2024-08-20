class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        for item in tokens:
            if item.lstrip("-").isdigit(): 
                stk.append(int(item))
            else:
                second = stk.pop()
                first = stk.pop()
                if item == '+':
                    stk.append(first + second)
                if item == '*':
                    # order don't matter
                    stk.append(first * second)
                if item == '-':
                    stk.append(first - second)
                if item == '/':
                    # order matters
                    stk.append(int(float(first) // second))
            print(stk, item)
        return stk[0]