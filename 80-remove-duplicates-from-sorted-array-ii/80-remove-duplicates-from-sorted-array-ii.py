class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        count = 0
        popcount = 0
        for i in range(len(nums)):
            if(nums[i] != prev):
                count = 0
                prev = nums[i]
            
            if nums[i] == prev and count==2:
                # print(nums[i])
                nums[i] = (10**4 + 1)
                
                popcount += 1
                
            elif nums[i] == prev and count < 2:
                count += 1
        nums.sort()
        return len(nums) - popcount
                