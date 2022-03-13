class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else: return None
        
class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = Stack()
        open = ["(","[","{"]
        matches = {
            "{":"}",
            "(":")",
            "[":"]"
            
        }
        
        for data in s:
            #check Open Or Close
            if data in open:
                #If open push into stack
                stack.push(data)
            
            #Else pop the stack and compare
            else:
                last_element = stack.pop() 
                if last_element != None:
                    if matches[last_element] != data:
                        return False
                        
                else:
                    return False
            #if matched continue else break and return 0
            
        if len(stack.stack) != 0:
            return False
        return True