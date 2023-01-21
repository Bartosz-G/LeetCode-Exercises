#https://leetcode.com/problems/reverse-integer/



class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            return None


        if x < 0:
            y = -1
            x = x * y
        else:
            y = 1

        x = int(str(x)[::-1])*y
        return x if -2147483648 < x < 2147483647 else 0
