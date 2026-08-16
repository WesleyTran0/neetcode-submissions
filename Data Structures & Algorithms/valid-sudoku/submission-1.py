class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0 for i in range(9)]
        cols = [0 for i in range(9)]
        squares = [0 for i in range(9)]

        for i, row in enumerate(board):
            for j, elem in enumerate(row):

                if elem == ".":
                    continue

                square = (i // 3)  * 3 + (j // 3)

                if ((1 << int(elem)) & cols[j] or 
                    (1 << int(elem)) & rows[i] or
                    (1 << int(elem)) & squares[square]):
                    return False
                
                cols[j] |= 1 << int(elem)
                rows[i] |= 1 << int(elem)
                squares[square] |= 1 << int(elem)

        return True