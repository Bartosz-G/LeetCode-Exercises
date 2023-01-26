# https://leetcode.com/problems/generate-parentheses/



class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        List = ['*' * 2 * n]

        def _generateParenthesis(n,List):
            finish_condition = 0

            List_Out = []

            for element in List:
                left = 0
                for i, char in enumerate(element):
                    if char == '*':
                        if left < 2 * n - i:
                            List_Out.append(element[:i] + '(' + element[i + 1:])
                        if left > 0:
                            List_Out.append(element[:i] + ')' + element[i + 1:])
                        break
                    elif char == '(':
                        left += 1
                    else:
                        left -= 1
                else:
                    finish_condition += 1

            if finish_condition == len(List):
                return List

            List_Out
            return _generateParenthesis(n,List_Out)

        return _generateParenthesis(n=n,List=List)

