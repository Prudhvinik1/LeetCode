from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        cnt = Counter(arr)
        cnt = list(cnt.values())
        cnt.sort()
        
        ans, size, half = 0,0,len(arr)//2
        while size < half:
            ans += 1
            size += cnt.pop()
        return ans