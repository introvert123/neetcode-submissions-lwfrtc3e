class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        path = set()


        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 1

            if row >= 0 and row < rows and col >=0 and col < cols:
                if (row,col) in path:  
                    return 0 
                if grid[row][col] == 0:
                    return 1
                path.add((row,col))
                

            return dfs(row-1,col) + dfs(row+1,col) + dfs(row,col+1) + dfs(row,col-1)



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
        