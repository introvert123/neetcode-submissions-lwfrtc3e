class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        path = set() #we shoudln't be revisiting the same cell again


        def dfs(row,col,k):

            if k == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or word[k] != board[row][col] or (row,col) in path:
                return False

            path.add((row,col))

            res = dfs(row + 1, col, k+1) or dfs(row, col-1, k+1) or dfs(row, col+1, k+1) or dfs(row-1,col, k+1)
            #backtracking comes - reached here meaning we didnt find the word through (row,col) - we are abandoning this path
            path.remove((row,col))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        
        return False