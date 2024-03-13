#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
import collections
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    # https://leetcode.com/problems/01-matrix/discuss/101080/Python-Simple-with-Explanation/572411 

    # self explanation/annotation
    # so each element in the queue is a neighbor of something, and that neighbor will always be positive, so it increments one from the parent and "increases" the distance of the path
    # and then when it goes onto the next level, it pops out / increments all the neighbors based on the value of the parent of the next level 

    # for shortest path: 
    # oh i guess for the reconstruction of the path from the target node e, which is given; in the beginning and not modified; the initial reconstruction assumes it exists somewhere in the prev array, and if it doesn't then path will just be empty
    # ALTERNATE: so you run bfs until you hit it basically right, holding the parent nodes for each node so when hit it, trace back the previous nodes
  
  # def updateMatrix(self, matrix):
        
        # So this problem asks us to find the minimum distance of 0  from every cell with value 1, 
        # BFS should ring in your mind and instead of our single-source BFS, we 
        # Apply multiple source BFS.
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        m, n = len(matrix), len(matrix[0])
        
        queue = collections.deque()
        
        res = [[-1 for _ in range(n)] for _ in range(m)]
        
        print(res)
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j] == 0:
                    # The distance to itself is 0 and add all sources here to queue
                    res[i][j] = 0
                    queue.append((i, j))
                    
        print(res)
        # Now we start our BFS
        
        while queue:
            
            curI, curJ = queue.popleft()
            print("curr: ", curI, curJ)
            for i, j in dirs:
                neighBorI, neighBorJ = curI + i, curJ + j
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    print("neighbor: ", neighBorI, neighBorJ)
                    res[neighBorI][neighBorJ] = res[curI][curJ] + 1
                    queue.append((neighBorI, neighBorJ))
                    print(queue)
                    print(res)
                    print("...")
        
        print(res)
        return res  
# @lc code=end

