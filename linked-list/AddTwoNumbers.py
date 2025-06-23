# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
        
        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next
        
        sum_num = int(num1) + int(num2)
        if sum_num == 0:
            return ListNode(0, None)
        
        dummy = ListNode(0)
        curr = dummy
        
        for digit_char in str(sum_num)[::-1]:  # Reverse the string to get digits in reverse order
            curr.next = ListNode(int(digit_char))
            curr = curr.next
        
        return dummy.next