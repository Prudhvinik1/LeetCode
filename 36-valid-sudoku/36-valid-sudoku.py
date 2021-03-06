class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_grid_valid(board) 
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    def is_col_valid(self,board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    def is_grid_valid(self,board):
        for i in (0,3,6):
            for j in(0,3,6):
                unit=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.is_unit_valid(unit):
                    return False
        return True
            
    def is_unit_valid(self,unit):
        unit_list=[i for i in unit if i!='.']
        return len(set(unit_list))== len(unit_list)