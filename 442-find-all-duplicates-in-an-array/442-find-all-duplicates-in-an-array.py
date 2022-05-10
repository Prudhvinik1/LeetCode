from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n):
            if(nums[abs(nums[i])-1] > 0):
                nums[abs(nums[i])-1] *= -1 
            else:
                output.append(abs(nums[i]))
        
        return output
                