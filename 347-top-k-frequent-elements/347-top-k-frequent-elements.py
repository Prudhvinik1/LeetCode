from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        
        heap = []
        for key,value in d.items():
            heapq.heappush(heap,(value,key))
            
        x = [x[1] for x in heapq.nlargest(k,heap) ] 
   
        return x