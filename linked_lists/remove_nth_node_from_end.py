from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        fast = curr_node
        slow = curr_node
        k = 1
        while k <= n + 1 and fast:
            fast = fast.next
            k += 1
        if not fast:
            if k == n + 1:
                head = slow.next
                return head
        while fast:
            slow = slow.next
            fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        else:
            return None
        return head