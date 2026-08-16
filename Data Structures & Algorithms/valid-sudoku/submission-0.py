class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for row in range(9):
            for col in range(9):
                curNum = board[row][col]
                if curNum == ".": 
                    continue

                square = (row // 3, col // 3)
                if curNum in rows[row] or curNum in cols[col] or curNum in sqs[square]:
                    return False
                    
                rows[row].add(curNum)
                cols[col].add(curNum)
                sqs[square].add(curNum)
        
        return True