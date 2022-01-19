# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow = fast = head
        flag = 0
        while fast and fast.next:
            if slow == fast and flag!=0:
                break
            flag = 1
            
            slow = slow.next
            fast = fast.next.next
        else:
            return None
        temp = head
        while temp != slow:
            temp = temp.next
            slow = slow.next
        return temp