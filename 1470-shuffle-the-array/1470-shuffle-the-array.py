class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p = []
        for i in range(n):
            p.append(nums[i])
            p.append(nums[i+n])
        
        return p