#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x = str(x)
        j = len(x)-1
        b = len(x)//2

        for i in x:
            if x[j] != i:
                return False
            j -= 1
            if b >j:
                break

        return True
