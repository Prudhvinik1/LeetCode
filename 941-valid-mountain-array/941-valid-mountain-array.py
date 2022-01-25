class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if(n <= 2): return False 
        
        i = 1
        mountain = 0
        while i < n:
            if(arr[i-1]<arr[i]):
                i += 1
                continue
            elif(arr[i-1] == arr[i]):
                return False
            elif(arr[i-1]>arr[i]):
                i = i-1 # Mountain Point
                break
        
        if(i==n or i == 0): return False
        
        j = i + 1
        while j < n:
            #print(j)
            if(arr[j-1] > arr[j]):
                j += 1
                continue
            elif(arr[j-1] == arr[j]):
                return False
            elif(arr[j-1]<arr[j]):
                #print(arr[j-1],arr[j])
                return False
        
        return True