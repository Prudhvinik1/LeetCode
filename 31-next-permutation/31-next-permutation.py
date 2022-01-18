from itertools import permutations
class Solution:
    
    def reverser(self,nums,breakpoint,n):
        #reverse the breakpoint + 1 till the end
        left = breakpoint + 1
        right = n-1
        
        while left <= right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
        return 
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #Find Break Point
        prev = nums[n-1]
        breakpoint = -1
        for i in range(n-2,-1,-1):
            if(nums[i]<prev):
                breakpoint = i
                break
            prev = nums[i]
        
        if(breakpoint==-1):
            self.reverser(nums,breakpoint,n)
            return
            
        
        #Find Swap Point
        for i in range(n-1,breakpoint,-1):
            if(nums[i]>nums[breakpoint]):
                nums[breakpoint],nums[i] = nums[i],nums[breakpoint]
                break
        
        #reverse the breakpoint + 1 till the end
        self.reverser(nums,breakpoint,n)
        return
        
        
                
                