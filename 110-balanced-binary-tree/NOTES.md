class Solution:
answer = True
def helper(self,root,height,lefth,righth,truth):
if(root==None):
height = 0
lefth = 0
righth = 0
truth = True
return
else:
#lefth =
self.helper(root.left,height,lefth,righth,truth)
#righth =
self.helper(root.right,height,lefth,righth,truth)
#print(lefth,righth)
height = max(lefth,righth) + 1
if(abs(lefth-righth)<=1 and truth!=False):
truth = True
else:
truth = False
self.answer = False
return
def isBalanced(self, root: Optional[TreeNode]) -> bool:
truth = True
self.helper(root,0,0,0,truth)
print(truth)
return self.answer