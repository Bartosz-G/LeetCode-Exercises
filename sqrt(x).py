#https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0

        value = x

        func = lambda a: a*a - x

        while True:
            next_val = value - (func(value)/(2*value))
            if next_val//1 == value // 1:
                return int(next_val//1)
            else:
                value = next_val





