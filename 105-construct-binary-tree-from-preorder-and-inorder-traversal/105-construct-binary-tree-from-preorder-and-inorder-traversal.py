# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    i = 0
    
    def recurse(self,preorder,inorder,start,end):
        if (start>end):
            return None
        
        tree = TreeNode(preorder[self.i])
        
        #search index of root in inorder
        index = inorder.index(preorder[self.i])
        self.i += 1
        
        tree.left = self.recurse(preorder,inorder,start,index-1)
        tree.right = self.recurse(preorder,inorder,index+1,end)
        
        return tree
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        start = 0
        end = len(inorder)
        
        
        return self.recurse(preorder,inorder,start,end-1)