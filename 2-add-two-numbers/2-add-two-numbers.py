# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sum_digits = []
        add = 0
        carry = 0
        lin1 = 0
        lin2 = 0
        #Traverse through the List
        while(l1!=None or l2!=None):
            
            lin1 = l1.val if l1!=None else 0
            lin2 = l2.val if l2!=None else 0
            
            val = lin1 + lin2 + carry
            if(val>=10):
                carry = 1
                add = val - 10
            else:
                carry = 0
                add = val
            sum_digits.append(add)
            if(l1!=None):
                l1 = l1.next
            if(l2!=None):
                l2 = l2.next
        if carry > 0:
            sum_digits.append(carry)
        flag = 0
        temp2 = None
        for i in sum_digits:
            temp = ListNode(i)
            if flag == 0:
                head = temp
                temp2 = temp
            else:
                temp2.next = temp
                temp2 = temp
            flag = 1
        
        return head
            
            
            
            