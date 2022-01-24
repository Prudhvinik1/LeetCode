class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if(word.upper() == word): return True
        if(word.lower() == word): return True
        if(word.lower().capitalize() == word): return True
        
        return False