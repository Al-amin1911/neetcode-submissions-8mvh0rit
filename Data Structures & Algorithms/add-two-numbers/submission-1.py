# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:

        curr1, curr2 = l1, l2

        if not curr1 and not curr2:
            if carry == 1:
                return ListNode(1)
            return None

        if curr1 and curr2:
            if (curr1.val + curr2.val+carry) < 10:
                add_node = ListNode((curr1.val+curr2.val+carry))
                add_node.next = self.addTwoNumbers(curr1.next, curr2.next, 0)
            else:
                add_node = ListNode((curr1.val + curr2.val + carry)-10)
                add_node.next = self.addTwoNumbers(curr1.next, curr2.next, 1)
        elif curr1:
            if (curr1.val + carry) < 10:
                add_node = ListNode(curr1.val+carry)
                add_node.next = self.addTwoNumbers(curr1.next, None, 0)
            else:
                add_node = ListNode((curr1.val + carry)-10)
                add_node.next = self.addTwoNumbers(curr1.next, None, 1)
        elif curr2:
            if (curr2.val + carry) < 10:
                add_node = ListNode(curr2.val+carry)
                add_node.next = self.addTwoNumbers(None, curr2.next, 0)
            else:
                add_node = ListNode((curr2.val + carry)-10)
                add_node.next = self.addTwoNumbers(None, curr2.next, 1)
        else:
            if carry == 1:
               add_node = self.addTwoNumbers(None, None, 1) 
            
        return add_node



        