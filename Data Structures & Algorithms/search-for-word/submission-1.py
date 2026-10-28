class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (min(row, col) < 0 or 
                row >= len(board) or 
                col >= len(board[0]) or 
                word[i] != board[row][col] or 
                (row, col) in seen):
                return False

            seen.add((row, col))
            res = (dfs(row + 1, col, i + 1) or 
                   dfs(row, col + 1, i + 1) or 
                   dfs(row - 1, col, i + 1) or 
                   dfs(row, col - 1, i + 1))
            seen.remove((row, col))
            return res
            
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

