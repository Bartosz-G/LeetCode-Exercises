#https://leetcode.com/problems/string-to-integer-atoi/
#Test cases for this problem conflict with the description of a problem as raised by many users in the comments
#Below code is done based on the description not on what passes the test cases


class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None:
            return None

        checker = lambda x: True if x.isdigit() or x == "-" or x == "+" else False
        start = None
        end = None

        for i,letter in enumerate(s):
            if end:
                break

            if not isinstance(start,int):
                if checker(letter):
                    start = i
                    continue
                else:
                    continue
            else:
                if checker(letter):
                    continue
                else:
                    end = i

        if not end:
            end = len(s)

        return int(s[start:end])
