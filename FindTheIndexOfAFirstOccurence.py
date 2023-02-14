#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack is None or needle is None:
            return -1


        for i,l in enumerate(haystack):
            if l == needle[0]:
                for j,n in enumerate(needle):
                    try:
                        if haystack[i+j] != n:
                            break
                    except IndexError:
                        return -1
                else:
                    return i
        else:
            return -1
