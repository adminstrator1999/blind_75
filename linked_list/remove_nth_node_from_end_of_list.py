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
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next"""
