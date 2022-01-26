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
            output.append(root.val)
            self.helper(root.right,output)
        
        return
            
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output = []
        output1 = []
        output2 = []
        self.helper(root1,output1)
        self.helper(root2,output2)
        
        i,j = 0,0
        while i<len(output1) and j<len(output2):
            if(output1[i] <= output2[j]):
                output.append(output1[i])
                i+=1
            else:
                output.append(output2[j])
                j += 1
        #print(output1,output2)
        while (i<len(output1)):
            output.append(output1[i])
            i += 1
        while (j<len(output2)):
            #print(j)
            output.append(output2[j])
            j += 1
        
        return output