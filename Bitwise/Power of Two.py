class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        #Check if n is 0
        if(n == 0): return False
        
        # Brian Kernighan's Algorithm
        return (n&(n-1) == 0 )
        
