from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        frequency = defaultdict(int)
        for i in words:
            frequency[i] += 1
        
        heap = []
        for key,value in frequency.items():
            heapq.heappush(heap,(-value,key))
            
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer
        
        