# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        
        counter = 0
        l = []
        while temp!=None:
            l.append(temp.val)
            temp = temp.next
        temp = head
        
        for i in range(0,len(l),k):
            if i + k <= len(l): 
                l[i:i+k] = reversed(l[i:i+k])
        print(l)
        i = 0
        while temp!=None:
            temp.val = l[i]
            i += 1
            temp = temp.next
        
        return head