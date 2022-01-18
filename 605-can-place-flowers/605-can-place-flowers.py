class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = -1
        zeroes=0
       
        flowers=0
       
        if(len(flowerbed)==1 and flowerbed[0]==0 and n==1):
            return True
       
        for i in flowerbed:
            if(i==1):
                if(prev==-1):
                    prev=zeroes
                    flowers+=zeroes//2
                else:
                    flowers+= (zeroes-1)//2
                zeroes=0
            else:
                zeroes+=1
        if(prev==-1):
            flowers+=(zeroes+1)//2
        else:
            flowers+=zeroes//2
       
        return flowers>=n
        