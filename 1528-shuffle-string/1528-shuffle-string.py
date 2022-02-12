class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ['a' for i in range(len(s))]
        for i in range(len(s)):
            output[indices[i]] = s[i]
        
        return "".join(output)