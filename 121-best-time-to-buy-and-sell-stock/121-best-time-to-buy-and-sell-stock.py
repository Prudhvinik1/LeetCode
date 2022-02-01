from sys import maxsize 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = maxsize
        maximum = 0
        
        for i in range(len(prices)):
            if(prices[i] < minimum):
                minimum = prices[i]
            if(prices[i]>minimum):
                profit = prices[i] - minimum
                if(profit>maximum):
                    maximum = profit
        
        return maximum