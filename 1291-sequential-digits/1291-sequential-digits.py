class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        low_length = len(str(low))
        high_length = len(str(high))
        output = []
        for i in range(low_length,high_length+1):
            for j in range(1,9-i+2):
                #print(j)
                num = [0] * i
                for k in range(i):
                    num[k] = j + k
                num = int("".join(map(str,num)))
                
                if num >= low and num <=high:
                    output.append(num)
        
        return output
                        