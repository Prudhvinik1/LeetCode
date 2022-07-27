class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort(reverse = True)
        minval = arr[-1]
        maxval = arr[0]
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
            
        
        if len(arr) == 0:
            return maxval
        else:
            avg = target/len(arr)
            if avg - int(avg) > 0.5:
                return round(avg)
            else:
                return int(avg)