#https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x<1:
            return 0

        def Sqrt(x,range = None):
            if range is None:
                range = [0,x]

            mid = (range[1] + range[0])/2
            value = mid*mid

            if range[1]-range[0]<0.00001:
                return int(range[1])

            mid = (range[1] + range[0])/2
            value = mid*mid

            if value == x:
                return int(mid)

            if value > x:
                range = [range[0],mid]

            if value < x:
                range = [mid,range[1]]

            return Sqrt(x,range=range)

        return Sqrt(x)
