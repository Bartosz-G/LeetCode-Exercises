# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
l12 = ListNode(4)
l11 = ListNode(2,l12)
list1 = ListNode(1,l11)

l22 = ListNode(4)
l21 = ListNode(3,l22)
list2 = ListNode(1,l21)



def printListNode(list:ListNode):
    print(list.val)
    while list.next != None:
        list = list.next
        print(list.val)




class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #We will link them in-place on list1
        if list1.val <= list2.val:
            self.head = list1
            self.pointer_previous = list1
            self.inplace = list1.next
            self.otherlist = list2
            self.pointer_next = None
        else:
            self.head = list2
            self.pointer_previous = list2
            self.inplace = list2.next
            self.otherlist = list1
            self.pointer_next = None



        while self.inplace.next is not None or self.otherlist.next is not None:
            if self.inplace.val <= self.otherlist.val:
                self.pointer_previous = self.inplace
                self.inplace = self.inplace.next
            else:
                self.pointer_next = self.otherlist.next
                self.pointer_previous.next = self.otherlist
                self.otherlist.next = self.inplace
                self.otherlist = self.pointer_next

        if self.inplace.next is None:
            self.inplace.next = self.otherlist
        else:
            pass
        return self.head



#printListNode(list1)
#printListNode(list2)
S = Solution()

printListNode(S.mergeTwoLists(list1,list2))