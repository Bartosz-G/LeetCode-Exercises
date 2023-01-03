#https://leetcode.com/problems/roman-to-integer/


Integer = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
DoubleInteger = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}



class Solution:
    def romanToInt(self, S: str) -> int:
        if S is None:
            return 0

        num = 0
        skip = False
        i = 0

        for s in S:
            i +=1
            if skip:
                skip = False
                continue

            if s == "I" or s == "X" or s == "C":
                try:
                    twoNumerals = DoubleInteger.get(s + S[i])
                    if twoNumerals is None:
                        pass
                    else:
                        skip = True
                        num += twoNumerals
                        continue

                except IndexError:
                    pass
            num += Integer.get(s)
        return num

