class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_len = len(pattern)
        s = s.split(" ")
        s_len = len(s)
        
        if p_len != s_len:
            return False
        
        d = {}
        for i in range(len(s)):
            if pattern[i] in d:
                if(d[pattern[i]] != s[i]):
                    return False
            else:
                if(s[i] in d.values()):
                    return False
                d[pattern[i]] = s[i]
        
        return True