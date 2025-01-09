# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        last = []

        curr = head
        count = 1
        while curr:
            count+=1
            curr = curr.next

        curr = head

        half_count = count // 2
        while half_count > 0:
            prev = curr
            curr = curr.next
            half_count-=1
        prev.next = None

        head2 = curr
        n_curr = head2
        while n_curr:
            last.append(n_curr)
            n_curr = n_curr.next

        ptr = head
        while ptr and last:
            connecting_node = last.pop()
            temp = ptr.next
            ptr.next = connecting_node
            connecting_node.next = temp
            ptr = temp