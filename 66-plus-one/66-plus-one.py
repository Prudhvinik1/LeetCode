class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = int("".join(list(map(str,digits)))) + 1
        return [int(i) for i in str(p)]
        