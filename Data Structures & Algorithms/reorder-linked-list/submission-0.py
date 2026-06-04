# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base Case: If the list has 0, 1, or 2 nodes, no reordering is needed
        if not head or not head.next or not head.next.next:
            return

        # 1. Use a while loop to find the SECOND-to-last node
        # (We need this node so we can sever the tail)
        prev_tail = head
        while prev_tail.next.next:
            prev_tail = prev_tail.next

        # 2. Isolate the tail node
        tail = prev_tail.next
        prev_tail.next = None  # Severing the tail cuts the list shorter!

        # 3. Insert the tail right after the current head
        tail.next = head.next
        head.next = tail

        # 4. RECURSIVE CALL (Outside the while loop!)
        # Pass the next inner head (which is now tail.next) to repeat the process
        self.reorderList(tail.next)
