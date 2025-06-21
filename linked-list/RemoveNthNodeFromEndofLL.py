# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next 
            length +=1

        new_n = length - n
        # Edge case: removing the first node
        if new_n == 0:
            return head.next
        curr = head
        prev = None
        count = 0
        while (count < new_n):
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
        return head