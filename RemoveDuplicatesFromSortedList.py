#https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        moving_node = head

        try:
            while True:
                while moving_node.val == moving_node.next.val:
                    moving_node.next = moving_node.next.next
                moving_node = moving_node.next
        except AttributeError:
            pass
        return head

