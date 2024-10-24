class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0

        def dfs(x, y, visited):
            # print(visited)
            # base = (x, y)
            q = [(x, y)]
            visited.add((x, y))

            while len(q) > 0: 
                # print(x, y)
                x, y = q.pop(0) 
                left, right, up, down = None, None, None, None
                # left (x - 1)
                if x - 1 >= 0: 
                    left = (x - 1, y)
                # right (x + 1)
                if x + 1 < len(grid[0]):
                    right = (x + 1, y)
                # up (y - 1)
                if y - 1 >= 0: 
                    up = (x, y - 1)
                # down (y + 1)
                if y + 1 < len(grid):
                    down = (x, y + 1)
                
                for elem in [left, right, up, down]:
                    if elem not in visited and elem is not None and grid[y][x] == "1":
                        visited.add(elem)
                        q.append(elem)

                # print(left, right, up, down)

            # print(visited)
            return visited

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # print(x, y)

                # if (x, y) in visited:
                #     print("already explored")
                if (x, y) not in visited and grid[y][x] == "1":
                    # start a new dfs to explore all connected sq's from the node
                    seen = dfs(x, y, visited)
                    # add seen to visited
                    # (todo)
                    # for elem in seen:
                    #     visited.add(elem)
                    # print(seen)
                    count += 1

        return count
