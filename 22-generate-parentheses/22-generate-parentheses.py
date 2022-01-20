class Solution:
    
    def helper(self,n,opened,closed,current,output):
        
        #Base
        if(len(current) == 2*n):
            output.append(current)
            return
        
        #Choice Diagram
        if(opened<n):
            self.helper(n,opened+1,closed,current+"(",output)
        if(closed<opened):
            self.helper(n,opened,closed+1,current+")",output)
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        if n == 1:
            return ['()']
        
        self.helper(n,0,0,"",output)
        return output