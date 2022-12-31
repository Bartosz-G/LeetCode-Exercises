#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        A = []
        for i in s:
            if not A:
                if i == ')' or i == ']' or i == "}":
                    return False
                else:
                    A.append(i)
                    continue

            current = A.pop()
            if current == '(':
                if i == ')':
                    continue
                elif i == ']' or i == '}':
                    return False
                else:
                    A.append(current)
                    A.append(i)
            if current == '[':
                if i == ']':
                    continue
                elif i == ')' or i == '}':
                    return False
                else:
                    A.append(current)
                    A.append(i)
            if current == '{':
                if i == '}':
                    continue
                elif i == ')' or i == '}':
                    return False
                else:
                    A.append(current)
                    A.append(i)

        return len(A)==0

