class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                rowBy3 = row // 3
                colBy3 = col // 3

                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in cols[col]:
                    return False
                if board[row][col] in squares[(rowBy3, colBy3)]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(rowBy3, colBy3)].add(board[row][col])
        return True