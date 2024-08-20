#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # create dict
        coords = {}
        for i in range(len(board)): # rows
            for j in range(len(board[i])): # cols
                elem = board[i][j]
                if elem == ".": # valid #'s
                    continue
                
                # elem: {(x, y)}
                if elem not in coords:
                    coords[elem] = []
                coords[elem].append((i, j))
        print(coords)

        # create coords
        for number in coords:
            print("numbbb: ", number) 
            xcoords = set()
            ycoords = set()
            for coord in coords[number]:
                if coord[0] in xcoords: # dup check
                    return False
                if coord[1] in ycoords:
                    return False
                
                # calculate base node
                if coord[0] - 1 in xcoords or coord[0] + 1 in xcoords or coord[1] - 1 in ycoords or coord[1] + 1 in ycoords:
                    pos = coord[1] % 3 # row in box
                    firstrow = coord[1] - pos
                    ypos = coord[0] % 3 # row in box
                    yfirstrow = coord[0] - ypos
                    print("pos, firstrow: ", pos, firstrow)
                    print("ypos, firstrow: ", ypos, yfirstrow)
                    print("base coordinate: ", (yfirstrow, firstrow))
                    
                    for i in range(0, 3):
                        for j in range(0, 3):
                            print("check coordinate: ", (yfirstrow + i, firstrow + j))
                            
                            # not the original
                            if coord != (yfirstrow + i, firstrow + j):
                                if board[yfirstrow + i][firstrow + j] == number:
                                    print("asjdklfjdkasl, val: ", board[yfirstrow + i][firstrow + j])
                                    return False
                # for checking dups
                xcoords.add(coord[0])
                ycoords.add(coord[1])
            print(xcoords, ycoords)

        # no invalid
        return True
            
            
            
                




        
# @lc code=end

