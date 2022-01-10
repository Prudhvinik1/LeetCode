
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for i in matrix:
            for j in i:
                heapq.heappush(l,j)
        
       
        p = heapq.nsmallest(k,l)
        return p[-1]
        