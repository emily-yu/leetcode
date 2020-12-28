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

        
        # prerequisites = [[2, 3], [3, 4], [1, 4], [4, 5]] # good
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
# @lc code=end

