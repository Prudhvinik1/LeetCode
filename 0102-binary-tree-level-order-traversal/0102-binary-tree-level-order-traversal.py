# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []

        if not root:
            return output

        q = Queue()
        q.put(root)

        while q.qsize() > 0:
            count = q.qsize()
            secOutput = []
            for i in range(count):
                node = q.get()
                secOutput.append(node.val)

                if node.left != None: q.put(node.left)
                if node.right != None: q.put(node.right)
            
            output.append(secOutput)
        
        return output
            

        