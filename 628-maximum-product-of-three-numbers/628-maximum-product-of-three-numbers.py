class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        product = 1
        for i in range(3):
            product *= nums[i]
        return max(product,nums[0] * nums[-1] * nums[-2])
                            