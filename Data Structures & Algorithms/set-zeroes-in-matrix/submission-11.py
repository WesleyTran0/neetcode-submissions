class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # two loops

        # first look through the matrix for row, col
            # matrix[0][0] represents 0th column is zeros
            # if found zero, set matrix[row][0] = 0 && matrix[col][0]
            # to account for overlap, if row = 0 && col = 0, set zero_col = True

        # second iteration check for markers
        # for matrix[x][y] if matrix[x][0] or matrix[0][y] = 0 then matrix[x][y] = 0
        zeroth_row = False

        for row_idx, row in enumerate(matrix):
            for col_idx, _ in enumerate(row):

                if matrix[row_idx][col_idx] == 0:
                    matrix[0][col_idx] = 0 # col will all be 0
                    if row_idx == 0:
                        zeroth_row = True
                    else:
                        matrix[row_idx][0] = 0 # row will all be 0
                    
        
        print("mid")
        print(matrix)
        # start from second row and check first row using zeroth_row independently
        for row_idx, row in enumerate(matrix):
            for col_idx in range(len(row) - 1, -1, -1):
                if row_idx == 0:
                    # skip first row at first
                    continue
                
                elif matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0

        for col_idx in range(len(matrix[0]) - 1, -1, -1):
            if zeroth_row:
                matrix[0][col_idx] = 0
        
        
        