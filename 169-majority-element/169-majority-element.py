from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        coun = Counter(nums)
        return coun.most_common(1)[0][0]
        