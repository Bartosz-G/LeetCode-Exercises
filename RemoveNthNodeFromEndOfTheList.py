#https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        moving_head = head
        nth_forward = moving_head


        for i in range(n):
            nth_forward = nth_forward.next

        if nth_forward is None:
            return moving_head.next


        try:
            while True:
                if nth_forward.next is None:
                    raise AssertionError
                else:
                    nth_forward = nth_forward.next
                    moving_head = moving_head.next

        except AssertionError:
            if n ==1:
                moving_head.next = None
            else:
                moving_head.next = moving_head.next.next

        return head

