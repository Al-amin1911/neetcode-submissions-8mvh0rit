# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return 

        dummy = ListNode(0, head)
        fast = slow = dummy
        i = 1
        while i < n:
            fast = fast.next
            i += 1
        
        while fast and fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        sec_half = slow.next
        prev.next = sec_half
        
        return dummy.next


