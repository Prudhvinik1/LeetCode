class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        
        tab = [[0]*n for i in range(n)]
        ans = ""
        
        for i in range(n):
            tab[i][i] = 1
            ans = s[i]
        for i in range(n-1):
            if(s[i]==s[i+1]):
                tab[i][i+1]=1
                ans = s[i:i+2]
        
        for j in range(n):
            for i in range(0,j-1):
            
                if(tab[i+1][j-1]==1 and s[i] == s[j]):
                    tab[i][j] = 1
                    if len(ans) < len(s[i:j+1]):
                        ans = s[i:j+1]
        
        return ans