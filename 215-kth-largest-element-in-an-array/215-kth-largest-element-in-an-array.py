import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*i for i in nums]
        heapq.heapify(nums)
        
        while k>0:
            num = heapq.heappop(nums)
            #print(num,k)
            k -= 1
        
        return -num