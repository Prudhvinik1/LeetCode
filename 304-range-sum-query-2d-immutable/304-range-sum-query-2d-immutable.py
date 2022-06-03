class NumMatrix:
    

    def __init__(self, matrix: List[List[int]]):
        self.dp=[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
		# calculate prefix sum
        for r in range(len(self.dp)-1):
            for c in range(len(self.dp[0])-1):
                self.dp[r+1][c+1]=matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#         self.rows = len(matrix)
#         self.columns = len(matrix[0])
        
#         self.DP = [[0 for i in range(self.columns  + 1)] for j in range(self.rows + 1)]
        
#         self.DP[0][0] = self.matrix[0][0]
        
#         #Alng Column
#         for i in range(1,self.rows):
#             self.DP[i][0] = self.DP[i-1][0] + self.matrix[i][0]
        
#         #Along Row
#         for i in range(1,self.columns):
#             self.DP[0][i] = self.DP[0][i-1] + self.matrix[0][i]
        
#         for i in range(1,self.rows):
#             for j in range(1,self.columns):
#                 self.DP[i][j] = self.matrix[i][j] + self.DP[i-1][j] + self.DP[i][j-1] - self.DP[i-1][j-1] 
                
#         print(self.DP)
    
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
# #         verticalSum = 0
# #         horizontalSum = 0
# #         diagonalSum = 0
        
# #         if(row1-1 >= 0):
# #             verticalSum = self.DP[row1-1][col2] 
# #         if(col1-1 >= 0):
# #             horizontalSum = self.DP[row2][col1-1]
# #         if(col1 -1 >=0 and col2 -1 >= 0):
# #             diagonalSum = self.DP[row1-1][col1-1]
# #         #regionSum =  self.DP[row1-1][col1-1] - (self.DP[row1-1][col2]) - self.DP[row2][col1-1]
# #         print(diagonalSum,verticalSum,horizontalSum)
# #         areaSum = self.DP[row2][col2] + diagonalSum - verticalSum - horizontalSum
# #         return areaSum
#         return self.DP[row2 + 1][col2 + 1] - self.DP[row1][col2 + 1] - self.DP[row2 + 1][col1] + self.DP[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)