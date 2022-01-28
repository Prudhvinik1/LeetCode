class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for sentence in sentences:
            max_len = max(max_len,len(sentence.split()))
        
        return max_len