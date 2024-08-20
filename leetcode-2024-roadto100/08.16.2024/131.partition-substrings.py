class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # q = s.split() # split into chars

        # visited = []


        # def bfs(visited, q, )
        #     visited.append(node)

        #     # clear level
        #     while q is not empty: 
        #         nextElem = q.pop() # first node


        #     bfs(visited, )
        #     q.pop()
        #     bfs(q)

        # need to do dfs - best explanation. https://www.youtube.com/watch?v=UP3dOYJa05s
        def dfs(i): 
            if i == len(nums): # reached end
                results.append(current[:]) # copy current subset
                return

            current.append(nums[i]) # add new element - decision to include
            dfs(i+1) # decision to not include current element to add
            current.pop() # remove the temp variable
            dfs(i+1) # run with current state
        
        nums = list(s)
        results = []
        current = []
        dfs(0)

        # palindrome check
        i = 0
        asdf = results
        toremove = []
        for result in asdf: 
            start = 0
            end = len(result) - 1
            while start < end:
                if result[start] != result[end]:
                    start = 99
                    break
                start += 1
                end -= 1
            if start == 99:
                toremove.append(i)
            i += 1

        res = []
        for elem in range(0, len(asdf)):
            if elem not in toremove:
                res.append(asdf[elem])

        return res
        # # nums = s.split('')
        # nums = list(s)
        # print(nums)
        # res = []
        # subset = []
        # def dfs(i):
        #     if i == len(nums):
        #         res.append(subset[:])
        #         return
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # return res

# this above solved the wrong problem: check which subsets are palindromes