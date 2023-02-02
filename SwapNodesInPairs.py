#https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None


        curr = head
        nxt = head.next

        if nxt is None:
            return head
        else:
            head = head.next
            curr.next = curr.next.next
            nxt.next = curr

            curr, nxt = nxt, curr
            prev = nxt

        try:
            while nxt.next.next is not None:
                nxt = nxt.next.next
                curr = curr.next.next

                prev.next = nxt
                curr.next = nxt.next
                nxt.next = curr

                curr,nxt = nxt,curr

                prev = prev.next.next

        except AttributeError:
            pass
        return head