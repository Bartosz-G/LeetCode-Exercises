#https://leetcode.com/problems/longest-common-prefix/

# LeetCode doesn't allow you to download reduce() from func, hence this is my implementation
def reduce(func,lst):
    if len(lst) < 2:
        return lst[0]
    el1 = lst.pop(0)
    el2 = lst.pop(0)
    nxt = func(el1,el2)
    if not lst:
        return nxt
    for el in lst:
        nxt = func(nxt,el)
    return nxt

def find_prefix(el1:str,el2:str) -> str:
    output = ""
    for (x,y) in zip(el1,el2):
        if x == y:
            output += x
        else:
            return output
    return output


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return reduce(find_prefix,strs)



