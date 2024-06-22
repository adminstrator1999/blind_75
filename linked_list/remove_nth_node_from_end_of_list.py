from typing import Optional

from linked_list.reverse_linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        slow, fast = ListNode(), head
        slow.next = head
        res = slow
        n -= 1
        while n:
            fast = fast.next
            n -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return res.next
    """
        slow, fast = ListNode(next=head), head
        res = slow
        while n > 0:
            fast = fast.next
            n -= 1
            
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return res.next"""
