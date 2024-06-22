import copy
from typing import Optional

from linked_list.reverse_linked_list import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        # stop head here
        slow.next = None
        # I need to reverse right side of the linked list
        reverse = None
        while right:
            tmp = right.next
            right.next = reverse
            reverse = right
            right = tmp

        while reverse:
            t_rev = reverse.next
            t_head = head.next
            reverse.next = head.next
            head.next = reverse
            head = t_head
            reverse = t_rev
