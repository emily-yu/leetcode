import collections
from typing import List

# Load the grid from a file
grid = None
with open('/Users/emilyyu/Desktop/leetcode/maestroai/data_small.txt') as file:
    grid = [list(line.rstrip()) for line in file]

if len(grid) == 0:
    print('Files are empty.')
else:
    visit = set()  # Keep track of visited cells
    count = 0      # To count the number of connected components
    q = []         # Queue for BFS

    def bfs(r, c):
        # BFS function to explore all cells in the same component
        q.append((r, c))
        visit.add((r, c))
        while q:
            row, col = q.pop(0)  # Remove the first element of the queue
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Directions: Down, Up, Right, Left

            for dx, dy in dirs:
                nr, nc = row + dx, col + dy
                if 0 <= nr < n and 0 <= nc < m:  # Check boundaries
                    if grid[nr][nc] == "1" and (nr, nc) not in visit:  # Check if cell is '1' and not visited
                        q.append((nr, nc))
                        visit.add((nr, nc))

    n = len(grid)  # Number of rows
    m = len(grid[0])  # Number of columns

    for r in range(n):
        for c in range(m):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                count += 1

    print('The count is', count)