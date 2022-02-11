class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            max_candy = max(candies)
            if(candies.index(max_candy) == i or candies[i] == max_candy ):
                output.append(True)
            else:
                output.append(False)
            candies[i] -= extraCandies
            
        return output