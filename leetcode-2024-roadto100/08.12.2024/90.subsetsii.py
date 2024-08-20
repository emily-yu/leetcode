# https://www.youtube.com/watch?v=qGyyzpNlMDU
# backtracking

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # valnums = [i for i in range(0, len(nums))]

        res = []
        subset = []

        def dfs(i):
            # if i >= len(valnums):
            if i >= len(nums):
                res.append(subset.copy())
                print("res:", res)
                return # when returning, what variables if any are maintained? how is res holding this
            # subset.append(valnums[i])
            subset.append(nums[i])u
            
            dfs(i + 1)
            print("subset1:", subset)
            subset.pop()
            print("subset2:", subset)
            dfs(i + 1)

        dfs(0)

        # after
        print(res)
        items = []
        for i in range(len(res)):
            result = sorted(res[i])
            if result not in items:
                items.append(result)
                
        return items