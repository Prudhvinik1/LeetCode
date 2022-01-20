class Solution:
    
    
    def dpSolution(self,s,wordDict):
        
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if(i+len(word) <= len(s) and word == s[i:i + len(word)]):
                    dp[i] = dp[i+len(word)]
                
                if(dp[i]):
                    break
        return dp[0]
    
    
    def helper(self,s,wordDict,i):
      
        #Base Condition
        if(i == len(s)):
            return True
        
        #Decision
        for j in wordDict:
            if j == s[i:i+len(j)]:
                return self.helper(s,wordDict,i+len(j))
        
        return False
        
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #return self.helper(s,wordDict,0)
        return self.dpSolution(s,wordDict)