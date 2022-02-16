class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()
        sentence.sort(key=lambda x:int(x[-1]))
        return " ".join([i[:-1] for i in sentence])