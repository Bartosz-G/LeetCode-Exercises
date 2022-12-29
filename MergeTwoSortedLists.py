#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



def printListNode(list:ListNode):
    A = []
    while list != None:
        A.append(list.val)
        list = list.next
    print(A)

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #We will link them in-place on list1
        try:
            if list1.val <= list2.val:
                self.head = list1
                self.pointer_previous = list1

                if list1.next is not None:
                    self.inplace = list1.next
                else:
                    self.inplace = list1

                self.otherlist = list2
                self.pointer_next = None
            else:
                self.head = list2
                self.pointer_previous = list2
                if list2.next is not None:
                    self.inplace = list2.next
                else:
                    self.inplace = list2
                self.otherlist = list1
                self.pointer_next = None
        except AttributeError:
            if list1 is None:
                return list2
            else:
                return list1


        while self.inplace.next is not None or self.otherlist.next is not None:
            if self.inplace.val <= self.otherlist.val:
                self.pointer_previous = self.inplace
                if self.inplace.next is not None:
                    self.inplace = self.inplace.next
                else:
                    break
            else:
                self.pointer_next = self.otherlist.next
                self.pointer_previous.next = self.otherlist
                self.otherlist.next = self.inplace
                self.otherlist = self.pointer_next
                self.pointer_previous = self.pointer_previous.next
                if self.otherlist is None:
                    break

        if self.inplace.next is None:
            try:
                if self.inplace.val > self.otherlist.val:
                    self.pointer_previous.next = self.otherlist
                    self.otherlist.next = self.inplace
                else:
                    raise AttributeError
            except AttributeError:
                self.inplace.next = self.otherlist
        else:
            pass
        return self.head