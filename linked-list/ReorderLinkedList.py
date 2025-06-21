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

        list2 = middle.next 
        curr = list2
        # reverse 2nd LL
        while (curr and curr.next):
            next_node = curr.next
            next_iter = curr.next.next
            if (curr == list2): 
                curr.next = None
            next_node.next = curr
            curr = next_node