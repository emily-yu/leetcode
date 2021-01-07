#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Accepted
        46/46 cases passed (136 ms)
        Your runtime beats 76.81 % of python3 submissions
        Your memory usage beats 46.61 % of python3 submissions (15.4 MB)
        '''
        
        # grid = [
        #     ['0', '0', '0', '0'],
        #     ['0', '1', '0', '0'],
        #     ['1', '1', '0', '1']
        # ]

        # grid = [
        # ["1","1","0","0","0"],
        # ["1","1","0","0","0"],
        # ["0","0","1","0","0"],
        # ["0","0","0","1","1"]
        # ]
        # grid = [
        # ["1","1","1","1","0"],
        # ["1","1","0","1","0"],
        # ["1","1","0","0","0"],
        # ["0","0","0","0","0"]
        # ]

        def dfs(grid, row, col):
            # validate
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = '0'
                dfs(grid, row + 1, col)
                dfs(grid, row - 1, col)
                dfs(grid, row, col + 1)
                dfs(grid, row, col - 1)
            else:
                return

        # go through to find island lands
        # land = []
        count = 0
        for row in range(len(grid)): # row
            for col in range(len(grid[row])): # col
                if grid[row][col] == '1': # land
                    dfs(grid, row, col)
                    # land.append((row, col))
                    count += 1
        # print(land)
        # print(count)
        return count



        '''
        [ 1,1 2,0, 2,1 2,3]
        root = 1,1
        count = 1
        children = 2,1 0,1 1,2 1,0
        2,1 exists, its part of the same island; remove (2,1)
            children = 3,1 1,1 2,2 2,0
            2,0 exists, its part of same island; remove(2,0)
                children = 1,0 3,0 2,1, 2,-1IV
                no children in land; stop
            len(q) = 0
        
        [ 2,3 ]
        root = 2,3
        count = 2
        children = 1,3 3,3 2,2 2,4
        no children in land; stop
        
        '''
        # import numpy as np

        # print(np.matrix(grid))
        # removed = set()
        # for elem in land:
        #     print(elem)
        #     row = elem[0]
        #     col = elem[1]
        #     children = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        #     # validate children
        #     valid = []
        #     for child in children: 
        #         if child[0] >= 0 and child[0] < len(grid) and child[1] >= 0 and child[1] < len(grid[0]):
        #             if grid[child[0]][child[1]] == '1':
        #                 valid.append(child)
        #                 if child not in removed and child != elem:
        #                     removed.add(child)     
        #     print('children = ', children)
        #     print('valid = ', valid)
        #     print('removed = ', removed)



        # import copy
        # count = 0
        # base = copy.deepcopy(land)
        # removed = set()
        # visited = set()
        # # while len(land) > 0:
        # for elem in base:
            
        #     # check if is part of another island already
        #     if elem in removed:
        #         print('is_removed')
        #         continue

        #     print('land = ', land)
        #     root = land.pop(0)
        #     print('root = ', root)
        #     print('count = ', count)

        #     # select neighbors
        #     row = root[0]
        #     col = root[1]
        #     children = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        #     # validate children
        #     for child in children: 
        #         if child[0] >= 0 and child[0] < len(grid) and child[1] >= 0 and child[1] <= len(grid[0]):
        #             continue
        #         else:
        #             idx = children.index(child)
        #             children.pop(idx)
        #             continue

        #         if grid[child[0]][child[1]] == '0':
        #             idx = children.index(child)
        #             children.pop(idx)
        #             continue
        #     print('children = ', children)

        #     while len(children) > 0:
        #         croot = children.pop()
        #         print('croot = ', croot)
        #         crow = root[0]
        #         ccol = root[1]
        #         cchildren = [(crow + 1, ccol), (crow - 1, ccol), (crow, ccol + 1), (crow, ccol - 1)]

        #         # validate children
        #         for child in cchildren: 
        #             if child[0] >= 0 and child[0] < len(grid) and child[1] >= 0 and child[1] <= len(grid[0]):
        #                 continue
        #             else:
        #                 idx = cchildren.index(child)
        #                 cchildren.pop(idx)
        #         print('cchildren = ', cchildren)

        #         # check if has any children to explore
        #         isolated = True
        #         to_explore = []
        #         for child in cchildren:
                        
        #             # if child is one of base elements, remove em
        #             if child in base:
        #                 if child not in removed and child != elem:
        #                     removed.add(child)
                    
        #             # add to the front of the queue to explore (dfs)
        #             if crow >= 0 and crow < len(grid) and ccol >= 0 and ccol <= len(grid[0]):
        #                 if (crow, ccol) not in visited:
        #                     visited.add((crow, ccol))

        #                     if grid[crow][ccol] == '1':
        #                         children = [child] + children
                
        # print(base)
        # print(removed)
        # print(count)
        # return count

        
# @lc code=end

