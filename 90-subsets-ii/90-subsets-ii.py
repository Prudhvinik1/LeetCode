class Solution:
    
    def subsets(self,nums,result,curr,i):
        
        if(len(nums)==i):
            temp = sorted(curr)
            if temp not in result:
                result.append(temp)
            return
        
        self.subsets(nums,result,curr,i+1)
        self.subsets(nums,result,curr[:] + [nums[i]],i+1)
        
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsets(nums,result,[],0)
        return result
        