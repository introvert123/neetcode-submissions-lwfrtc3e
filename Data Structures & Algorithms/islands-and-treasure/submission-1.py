class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        #multi-source bfs - we start from all the treasure chests
        
        def addDist(row,col,val):
            if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 2147483647:
                grid[row][col] = 1 + val
                queue.append([row,col])




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: 
                    queue.append([i,j])
        
        while queue:
            [row,col] = queue.popleft()
            addDist(row+1,col,grid[row][col])
            addDist(row-1,col,grid[row][col])
            addDist(row,col+1,grid[row][col])
            addDist(row,col-1,grid[row][col])