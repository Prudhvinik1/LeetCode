class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            calc_target = numbers[left] + numbers[right]
            
            if(calc_target == target):
                return [left + 1, right + 1]
            elif(calc_target < target):
                left += 1
            elif(calc_target > target):
                right -= 1
        
        