import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = -sys.maxsize
        sumUntilHere = 0

        for i in nums:
            sumUntilHere += i
            maxSum = max(maxSum,sumUntilHere)

            if(sumUntilHere < 0):
                sumUntilHere = 0
            
        return maxSum

