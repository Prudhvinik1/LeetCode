import math
def findMSB(n):

    # Not leetcode but coding Ninjas
    # Write your code here.
    k = int(math.log2(n))
    
    return (1<<k)