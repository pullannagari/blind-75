from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        if not head:
            return
        slow = head
        if head.next:
            fast = head.next.next
        else:
            return head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None

        # shift the pointers in reverse from middle
        prev_node = slow
        curr_node = slow.next
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            if not next_node:
                new_head = curr_node
                curr_node = next_node
            else:
                curr_node = next_node
                next_node = curr_node.next
        slow.next = None

        # alternate the values from start and end
        curr_start = head
        curr_end = new_head
        while curr_end != slow:
            curr_start_next = curr_start.next
            curr_end_next = curr_end.next
            curr_start.next = curr_end
            curr_start.next.next = curr_start_next
            curr_end = curr_end_next
            curr_start = curr_start_next
            
        return head

        
            
        