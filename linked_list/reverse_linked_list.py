from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = head
        nxt = head.next
        if nxt:
            new_head = self.reverseListRecursive(head.next)
            nxt.next = head
        head.next = None
        return new_head


