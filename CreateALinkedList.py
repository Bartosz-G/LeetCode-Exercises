#Simple scripts for creating linked lists out of normal lists

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def MakeALinkedList(List:list) -> ListNode:
    if List is None:
        return None

    prev = None
    for i in reversed(List):
        current = ListNode(val=i,next = prev)
        prev = current
    return current


def PrintLinkedList(node):
    A = []
    while node is not None:
        A.append(node.val)
        node = node.next
    print(A)

def _PrintLinkedList(node):
    A = []
    while node is not None:
        A.append(node.val)
        node = node.next
    return A

