# https://leetcode.com/problems/generate-parentheses/


a1 = 3
a2 = ["((()))","(()())","(())()","()(())","()()()"]

b1 = 1
b2 = ["()"]


# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:

def _generateParenthesis(List,l,r,n):
    if n == 0:
        return List





def addParenthesis(s,l,n):
    List = []
    ln = []
    if l<n:
        List.append(s + "(")
        ln.append((l+1,n))

    if l > 0:
        List.append(s + ")")
        ln.append((l-1,n-1))

    if not List:
        return None

    return List,ln

def take_out_elements(List:list):



# n = 3,l=2
t1 = "(("

# n = 3, l=0
t2 = ""

print(addParenthesis(t1,2,3))
print(addParenthesis('(((',3,3))
print(addParenthesis('((()',2,2))
print(addParenthesis('((())',1,1))
print(addParenthesis('((()))',0,0))
print(addParenthesis(t2,0,3))











