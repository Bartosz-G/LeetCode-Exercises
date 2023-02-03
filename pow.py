#https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n == 1:
            return float(x)

        if n == -1:
            if x == 0:
                return None
            else:
                return float(1/x)

        if x == 1:
            return 1.0

        if x == -1:
            if n % 2 == 0:
                return 1.0
            else:
                return -1.0

        sign = -1 if n < 0 else 1
        n = n*sign
        val = x

        while n != 1:
            x = x*val
            n -= 1
            if -0.0000000000001 < x < 0.0000000000001:
                 return 0
            if not -10000000 < x < 10000000:
                if x < -1000:
                    return 0.0
                else:
                    return 0.0


        if sign < 0:
            x = 1/x

        return x

