class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()

        def dfs(row,col,visit,prevHeight):
            if row < 0 or row > rows-1 or col < 0 or col > cols-1 or (row,col) in visit or heights[row][col] < prevHeight:
                return

            visit.add((row,col))
            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col])
            dfs(row,col+1,visit,heights[row][col])
            dfs(row,col-1,visit,heights[row][col])


        #boundary rows and cols
        #top and bottom row
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        #left and right col
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

        