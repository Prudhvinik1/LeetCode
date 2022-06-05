class Solution:
    def isSafe(self,board,row,column,n):
        #Check along the rows
        for i in range(n):
            if(board[row][i] == "Q"):
                return False
        
        #Check Upper Diagonal
        i,j = row,column
        while i>=0 and j >=0:
            if(board[i][j] == "Q"):
                return False
            i -= 1
            j -= 1
        
        #Check Lower Diagonal
        i,j = row,column
        while i<n and j >= 0:
            if(board[i][j] == "Q"):
                return False
            i += 1
            j -= 1
        
        return True
        
    
    def solveQueensRec(self,board,n,output,column):
        if(column == n):
            output[0] += 1 #.append(["".join(i) for i in board])
            return 
        
        for row in range(n):
            if(self.isSafe(board,row,column,n)):
                board[row][column] = "Q"
                self.solveQueensRec(board,n,output,column+1)
                board[row][column] = "."
        
        return
    
   
        return output
    def totalNQueens(self, n: int) -> int:
        board = [["." for i in range(n)] for i in range(n)]
        output = [0]
        column = 0
        row = 0
        self.solveQueensRec(board,n,output,column)
        return output[0]