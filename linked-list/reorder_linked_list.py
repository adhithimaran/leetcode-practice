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

        list2 = slow.next 
        slow.next = None
        curr = list2
        prev = None
        # reverse 2nd LL
        while curr:
            first = curr.next
            curr.next = prev
            prev = curr
            curr = first
        # tail is new head
        list2 = prev
        # merge lists
        list1 = head
        while list2:  # list2 will always be shorter or equal
            # Save next nodes
            next1 = list1.next
            next2 = list2.next
            
            # Connect current nodes
            list1.next = list2
            list2.next = next1
            
            # Move to next pair
            list1 = next1
            list2 = next2
