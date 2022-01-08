# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root): return True
        left = self.height(root.left)
        right = self.height(root.right)
        
        return abs(left-right) <2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def height(self,root):
        if(root==None):
            return 0
        else:
            return max(self.height(root.left),self.height(root.right)) + 1