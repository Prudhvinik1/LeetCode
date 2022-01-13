class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prev = 0
        count = 1
        curr = 1
        while curr < len(points):
            if(points[prev][1] >= points[curr][0]):
                
                curr += 1
                
            else:
                prev = curr
                count += 1
                
        return count
        
        