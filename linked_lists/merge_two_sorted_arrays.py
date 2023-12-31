from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                curr_node = curr_node.next
                list1 = list1.next
            else:
                curr_node.next = list2
                curr_node = curr_node.next
                list2 = list2.next
        if list1:
            curr_node.next = list1
        elif list2:
            curr_node.next = list2
        return dummy.next
    
if __name__ == "__main__":
    for i in range(1, 5, 2):
        print(i)

        