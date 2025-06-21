# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of LL to separate
        fast = head
        slow = head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        middle = slow