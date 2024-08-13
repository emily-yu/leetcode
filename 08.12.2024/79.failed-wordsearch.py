class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        idxs = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]: #start
                    idxs.add((row, col))
        print(idxs)

        def neighbors(start):
            result = []
            print(len(board[0]))
            # up
            if start[1] - 1 >= 0:
                result.append((start[0], start[1] - 1))
            # down
            if start[1] + 1 < len(board[1]) - 1:
                result.append((start[0], start[1] + 1))
            # left
            if start[0] - 1 >= 0:
                result.append((start[0] - 1, start[1]))
            # right
            if start[0] + 1 < len(board[0]) - 1:
                result.append((start[0] + 1, start[1]))
            return result

        def search(coord, ind, state):
            avail = neighbors(coord)
            print("neighbors to search ", avail)
            for idx in avail:
                row = idx[0]
                col = idx[1]
                print('neighbor is ', idx, board[row][col])
                if board[row][col] == word[ind] and (row, col) != coord:
                    print("searching: ", (row, col), " for char at ", ind)                    
                    if ind == len(word) - 1: # finished
                        return True

                    return search(idx, ind + 1, True) # continue

        for coord in idxs:
            print(coord, neighbors(coord))
            boop = search(coord, 1, False) # will keep searching through full tree
            if boop: 
                return True
        return False

            