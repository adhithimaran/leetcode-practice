
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif (not l1) and (not l2):
            return None 
        # add nodes to individual lists
        list1 = []
        list2 = []
        ptr1 = l1
        while ptr1:
            list1.append(ptr1.val)
            ptr1 = ptr1.next
        ptr2 = l2
        while ptr2:
            list2.append(ptr2.val)
            ptr2 = ptr2.next

        # pop off list and create string int of both lists
        int1 = ''
        while list1:
            int1+=str(list1.pop())
        int2 = ''
        while list2:
            int2+=str(list2.pop())
        # add and return
        Sum = int(int1)+int(int2)
        sum_list = list(str(Sum))
        print(sum_list)
        h = ListNode(sum_list.pop())
        ptr = h
        print(sum_list)
        
        count = len(sum_list)
        while count > 0:
            ptr.next = ListNode(sum_list.pop())
            print(sum_list)
            print(f'added node: {ptr.val}')
            count -=1
            ptr = ptr.next
        return h

