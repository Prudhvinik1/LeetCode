class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1

        penultimate = 1
        ultimate = 1
        for i in range(2,n+1):
            temp = ultimate + penultimate
            penultimate = ultimate
            ultimate = temp

        return ultimate