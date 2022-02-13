class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def helper(subset,i=0):
            
            if(i == len(nums)):
                output.append(subset)
                return



            helper(subset,i+1)
            helper(subset +[nums[i]],i+1)
            return
        helper([],0)
        return output