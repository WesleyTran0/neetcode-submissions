class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0] * 9
        cols = [0] * 9
        sqs = [0] * 9

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue
            
                binRep = 1 << (int(elem) - 1)
                sq = (i // 3) * 3 + (j // 3)

                if (rows[i] & binRep or
                    cols[j] & binRep or
                    sqs[sq] & binRep):
                    return False
                
                rows[i] |= binRep
                cols[j] |= binRep
                sqs[sq] |= binRep
        
        return True