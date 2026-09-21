class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0 for i in range(9)] 
        cols = [0 for i in range(9)]
        sqs = [0 for i in range(9)]

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue

                bit = 1 << (int(elem) - 1)
                sq = (i // 3) * 3 + (j // 3)
                if (rows[i] & bit or
                    cols[j] & bit or
                    sqs[sq] & bit):
                    return False
                
                rows[i] |= bit
                cols[j] |= bit
                sqs[sq] |= bit
        return True
