class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    '''
    Short Explanation: To not over-complicate, here is a simple explanation. 
    A naive method here is to repeatedly subtract divisor from dividend, until there is none enough left.
    Then the count of subtractions will be the answer. Yet this takes linear time and is thus slow. 
    A better method is to subtract divisor in a more efficient way. 
    We can subtract divisor, 2divisor, 4divisor, 8*divisor... as is implemented above.
     Now the subtracting process only takes log-time.


    '''

        
        # Store the number if it is positive or negative
        isNegative = ( dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        
        
        # Dividing 2 numbers is equivalent to removing divisor from dividend repatedly until we get 0.  
        #The count is quotient
        
        dividend,divisor = abs(dividend),abs(divisor)
        
        quotient = 0
        while(dividend >= divisor):
            
            curr_divisor,num_divisor = divisor,1   #num divisor is like number of times we incremented divisor
            
            #Inner While loop subtracts in the 2 powers of divisors. If, there is more dividend ledt, it restarts by exiting inner while 
            while dividend >= curr_divisor:
            
                dividend -= curr_divisor
                quotient += num_divisor
                
                curr_divisor <<= 1
                num_divisor <<= 1  #number of times incremented divisor
        
        
        if isNegative == True:
            quotient = -quotient
        
        return min(max(-(1<<31),quotient),(1<<31)-1)