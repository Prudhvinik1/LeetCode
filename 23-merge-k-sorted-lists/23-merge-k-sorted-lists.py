# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == []: return None
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap,head.val)
                head = head.next
        
        prev = None
        try:
            while heap:
                node = ListNode(heapq.heappop(heap))
                if(prev == None):
                    prev = node
                    head = prev
                else:
                    prev.next = node
                    prev = prev.next
        except Exception as e:
            print(e)
        
        return head
            
                