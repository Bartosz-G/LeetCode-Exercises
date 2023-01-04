#https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        Answer = ""

        for i in reversed(Roman):
            Answer += ((num // i) * Roman.get(i))
            num = num % i

        Answer = Answer.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX",
            "XL").replace("VIIII", "IX").replace("IIII", "IV")
        return Answer
