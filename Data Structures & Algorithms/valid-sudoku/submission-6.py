class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are given a list of lists
        # the first part of the list is each row.
        # the nested part of the list is the col 

        rows = defaultdict(set)

        cols = defaultdict(set)

        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3,col//3]:
                    return False
        
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[row//3,col//3].add(board[row][col])
        return True
        

