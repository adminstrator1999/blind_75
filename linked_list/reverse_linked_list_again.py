
def reverse_linked_list(head):
    prev = None
    curr = head

    if curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def reverse_linked_list_recursive(head):
    if not head:
        return None
    new_head = head
    nxt = head.next
    if nxt:
        new_head = reverse_linked_list_recursive(head.next)
        nxt.next = head
    head.next = None
    return new_head
