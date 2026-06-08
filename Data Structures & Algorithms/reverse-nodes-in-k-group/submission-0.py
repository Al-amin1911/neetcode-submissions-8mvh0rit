# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        # 1. THE SCOUT LOOP
        # Check if there are at least 'k' nodes left in this group.
        # If we hit None early, we don't reverse anything and just return head as-is.
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        # At this point, 'curr' has walked exactly k steps forward, 
        # which means it is now sitting exactly on the head of the NEXT group!
        nghead = curr

        # 2. THE CLEAN REVERSAL
        # We start 'prev' at 'nghead'. This is the magic trick: the first node 
        # we reverse will automatically point to the next group, preventing orphans!
        prev = nghead
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(nghead, k)
        return prev
        

        
        

        
        



        