#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True

        
        prerequisites = [[2, 3], [3, 4], [1, 4], [4, 5]] # good
        # prerequisites = [[2, 3], [3, 4], [4, 2]] # bad
        tracking = {}
        for key, value in prerequisites:
            # print(key, value)
            if value in tracking:
                tracking[value].append(key)
            else:
                tracking[value] = [key]
        # print(tracking)
        # print(len(flat_list), flat_list)

        # 43/46
        '''
        flat_list = set(item for sublist in prerequisites for item in sublist)
        for key in tracking.keys():
            explored = set()
            q = [key]
            while len(q) > 0:
                root = q.pop()
                
                # key is addressed
                if root in explored and root in tracking.keys():
                    print("doomed")
                    print(root, q, explored)
                    return False
                # key has values to add
                if root in tracking:
                    q += tracking[root]
                    q = list(set(q))

                explored.add(root)
        return True
        '''

        '''
        40/46
        print(tracking)
        for key, value in tracking.items():
            print("KEY: ", key)
            check = [key]
            explored = set()
            while True:
                # print()
                print('check: ', check, explored)
                result = []

                # for each key
                for elem in check:

                    # get children
                    if elem in tracking:
                        children = tracking[elem]
                    else:
                        children = []

                    # generate new layer; for the child of each children
                    for child in children:
                        if child in explored:
                            return False
                        if child in tracking:
                            result += tracking[child]
                            explored.add(child)

                check = result
                if len(check) == 0:
                    break
            
        return True
        '''

        ### dfs graph
        ### https://leetcode.com/problems/course-schedule/discuss/434263/easy-solution-using-dfs-basically-what-we-have-to-do-is-detect-a-loop-in-directed-graph
        print(tracking)

        # white = []
        white = [] + list(set(item for sublist in prerequisites for item in sublist))
        grey = []
        black = []
        visited = [0] * white
        print(white, black, grey)

        # explore every neighbors
        def dfs(root):
            # if visited[root] == 1: # grey
            if root in grey:
                return False
            
            # explore neighbors
            children = tracking[root]
            if len(children) == 0: # reached end
                return True
            for child in children:
                if child in grey: # currently being visited, bad
                    return False
                
                result = dfs(child) # one of children created cycle
                if not result:
                    return False

                # no children / child creates a cycle
                # valid; black (fully visited end node) or white (not visited)
                ind = root.index(child)
                # visited[ind] = 1 # grey/touched
                white.remove(child) # move around elements
                grey.append(child)
                return True
        
        # run until all nodes have been explored
        while len(white) > 0:
            root = white.pop()
            for child in tracking[root]:
                if child in white and not dfs(child):
                    return False
        return True # ran through every node without triggering a cycle

# @lc code=end

