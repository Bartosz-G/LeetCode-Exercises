#https://leetcode.com/problems/add-two-numbers/



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Next = [l1 is not None,l2 is not None]
        carry_over = 0
        Head = None
        previous_pointer = None
        val = lambda x: x.val if x is not None else 0
        pointer = lambda x: x.next if x is not None else None

        if any(Next):
            sum = carry_over + val(l1) + val(l2)
            Head = ListNode(sum%10,None)
            previous_pointer = Head
            carry_over = sum // 10
            l1 = pointer(l1)
            l2 = pointer(l2)
            Next = [l1 is not None, l2 is not None]


        while any(Next):
            sum = carry_over + val(l1) + val(l2)
            Next = ListNode(sum%10,None)
            previous_pointer.next = Next
            previous_pointer = Next
            carry_over = sum // 10
            l1 = pointer(l1)
            l2 = pointer(l2)
            Next = [l1 is not None, l2 is not None]

        if carry_over != 0:
            Next = ListNode(carry_over,None)
            previous_pointer.next = Next

        return Head

