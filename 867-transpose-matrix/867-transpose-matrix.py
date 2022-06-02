class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #print(list(zip(*matrix)))
        return zip(*matrix)
            