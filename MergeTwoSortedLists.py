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




#Input: list1 = [], list2 = []
#Output: []
LN1, LN2 = None,None

#Input: list1 = [], list2 = [0]
#Output: [0]
LL1 , LL2 = None,ListNode(0)

#Input: list1 = [-3,-1,0,5,7], list2 = [-5,1,3,4,6]
#Output:


L14 = ListNode(7)
L13 = ListNode(5,L14)
L12 = ListNode(0,L13)
L11 = ListNode(-1,L12)
List1 = ListNode(-3,L11)


L24 = ListNode(6)
L23 = ListNode(4,L24)
L22 = ListNode(3,L23)
L21 = ListNode(1,L22)
List2 = ListNode(-5,L21)


#list1 = [2] list2 = [1]
n1 = ListNode(-9)
N1 = ListNode(3,n1)
n2 = ListNode(5)
N2 = ListNode(7,n2)




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
                self.inplace = self.inplace.next
            else:
                self.pointer_next = self.otherlist.next
                self.pointer_previous.next = self.otherlist
                self.otherlist.next = self.inplace
                self.otherlist = self.pointer_next
                self.pointer_previous = self.pointer_previous.next

        if self.inplace.next is None:
            self.inplace.next = self.otherlist
        else:
            pass
        return self.head



#printListNode(list1)
#printListNode(list2)
S = Solution()

printListNode(S.mergeTwoLists(list1,list2))
print(S.mergeTwoLists(LN1,LN2))
printListNode(S.mergeTwoLists(LL1,LL2))
output = S.mergeTwoLists(List1,List2)
printListNode(output)
printListNode(S.mergeTwoLists(N1,N2))