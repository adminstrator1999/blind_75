from typing import List, Optional

from linked_list.reverse_linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        left = self.mergeKLists(lists[0:len(lists) // 2])
        right = self.mergeKLists(lists[len(lists) // 2:])

        sorted_ll = self.merge(left, right)
        return sorted_ll

    def merge(self, left, right):
        curr = ListNode()
        res = curr
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return res.next
