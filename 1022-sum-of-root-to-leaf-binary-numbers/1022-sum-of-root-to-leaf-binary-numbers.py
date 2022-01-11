# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root,answer,string):
        if(root!=None):
            
            string += str(root.val)
            self.helper(root.left,answer,string)
            self.helper(root.right,answer,string)
            
            if(root.left == None and root.right == None):
                
                answer.append(string)
        
        return
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        answer = []
        self.helper(root,answer,"")
        s = 0
        for i in answer:
            s += int(i,2)
        return s
        
        