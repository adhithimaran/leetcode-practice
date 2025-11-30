def sol(head):
    curr = head
    prev = None
    while curr:
        first = curr.next
        curr.next = prev
        prev = curr
        curr = first
    return prev