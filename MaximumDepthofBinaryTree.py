#https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def check_depth(A,m):
    if not A:
        return m

    next = []
    m += 1
    for i in A:
        if i.left is not None and i.right is not None:
            next.append(i.left)
            next.append(i.right)
        elif i.left is not None:
            next.append(i.left)
        elif i.right is not None:
            next.append(i.right)
        else:
            pass
    return check_depth(next,m)




class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        m = 0
        A = [root]
        return check_depth(A,m)


