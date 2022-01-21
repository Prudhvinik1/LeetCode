# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root,output):
        if(root):
            self.helper(root.left,output)
            self.helper(root.right,output)
            output.append(root.val)
        
        return
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        self.helper(root,output)
        return output