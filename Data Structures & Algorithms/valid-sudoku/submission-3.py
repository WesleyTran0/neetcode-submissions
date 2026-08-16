class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0] * 9
        cols = [0] * 9
        sqs = [0] * 9

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue
                
                sq = (i // 3) * 3 + (j // 3)
                rep = 1 << int(elem) - 1

                if (rows[i] & rep
                    or cols[j] & rep
                    or sqs[sq] & rep):
                    return False
                
                rows[i] |= rep
                cols[j] |= rep
                sqs[sq] |= rep
        
        return True

