class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        stack = []
        
        for i in path:
            if(stack and i == ".."):
                stack.pop()
            elif i not in ['.','','..']:
                stack.append(i)   
        
        return "/" + "/".join(stack) 