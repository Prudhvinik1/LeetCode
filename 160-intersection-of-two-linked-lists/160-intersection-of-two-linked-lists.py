# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_hash = defaultdict(int)
        tempA,tempB = headA,headB
        while tempA:
            if not node_hash[tempA]:
                node_hash[tempA] += 1
            
            tempA = tempA.next
        while tempB:
            if not node_hash[tempB]:
                node_hash[tempB] += 1
            else:
                return tempB
            
        
            tempB = tempB.next

        return None