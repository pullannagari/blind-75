from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = self.reverseList(head.next)
        if new_head:
            curr_node = head.next
            curr_node.next = head
            curr_node.next.next = None
            return new_head
        return head
        

        # iterative solution
        # new_head = None
        # while head:
        #     curr_head = head
        #     head = head.next
        #     curr_head.next = new_head
        #     new_head = curr_head
        # return new_head
        