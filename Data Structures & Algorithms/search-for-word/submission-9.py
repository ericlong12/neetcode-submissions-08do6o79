class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(row, column, letterIndex):
            # look for base case

            # have found the letter
            if letterIndex >= len(word):
                return True

            # if we don't match the letter. 
            # if we are out of index
            if (
                row < 0 # left out of bounds
                or row >= ROWS # right out of bounds
                or column < 0 # bottom out of bounds
                or column >= COLS # top out of bounds
                or board[row][column] != word[letterIndex] # not correct letter
                or (row,column) in visited
            ):
                return False

            # base case done

            # now we have to implement the recursion here to search
            
            # run dfs on each angle
            visited.add((row,column))

            result = (
                dfs(row-1, column, letterIndex + 1) #search left
                or
                dfs(row+1, column, letterIndex + 1) #search right
                or
                dfs(row, column + 1, letterIndex + 1) #search top
                or
                dfs(row, column -1, letterIndex + 1) # search bottom
            )

            visited.remove((row, column))

            return result
        # now we run this function dfs on every element in the word search
        #aka board
 

        for rowIndex in range(len(board)):
            for columnIndex in range(len(board[0])):
                if dfs(rowIndex, columnIndex, 0):
                    return True
        
        return False















