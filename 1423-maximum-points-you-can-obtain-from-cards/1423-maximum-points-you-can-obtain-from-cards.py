import sys
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = 0
        n = len(cardPoints)
        for i in range(1,n):
            cardPoints[i] += cardPoints[i-1]
        
        window_size = n - k
        left = 0
        right = window_size - 1
        min_size = sys.maxsize
        while right < n:
            if left == 0:
                min_size = min(min_size,cardPoints[right])
                
            else:
                min_size = min(min_size,cardPoints[right] - cardPoints[left - 1])
            left += 1
            right += 1
        return cardPoints[n-1] - min_size
            