# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k==0 or head == None):
            return head
        #Find the length of the list
        temp = head
        count = 0
        stack = []
        while temp:
            #stack.append(temp)
            count += 1
            temp = temp.next
        
        breakPoint = k%count
        
        if breakPoint == 0:
            return head
        
        temp = main = head
        counter = count - breakPoint
        print(counter,breakPoint)
        while counter > 1:
            temp = temp.next
            counter -= 1
        
        temp2 = temp
        head2 = temp2.next
        print(head2.val)
        
        while breakPoint > 1:
            print(temp2.val)
            temp2 = temp2.next
            breakPoint -= 1
        
        temp2 = temp2.next
        temp.next = None
        temp2.next = main
        
        return head2
            