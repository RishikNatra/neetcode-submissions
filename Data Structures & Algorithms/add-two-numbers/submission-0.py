# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            i = num1 = num2 = 0
            while l1:
                num1 = num1 + (10**i)*(l1.val)
                i = i+1
                l1 = l1.next   
            i = 0
            while l2:
                num2 = num2 + (10**i)*(l2.val)
                i = i+1
                l2 = l2.next      
            new = num1 + num2

            if new == 0:
                return ListNode(0)
            head = None
            tail = None
            while new:
                digit = new % 10
                new //= 10
                node = ListNode(digit)
                if not head:
                    head = tail = node
                else:
                    tail.next = node
                    tail = tail.next
            
            return head

