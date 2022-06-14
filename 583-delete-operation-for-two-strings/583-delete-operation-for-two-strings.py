class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m=len(word1)
        n=len(word2)
        DP = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            DP[i][0]=0
            
        for j in range(n+1):
            DP[0][j]=0
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(word1[i-1]==word2[j-1]):
                    DP[i][j] = DP[i-1][j-1]+1
                    
                else:
                    DP[i][j] = max(DP[i-1][j],DP[i][j-1])
        
        return m+n-(2*DP[i][j])
            