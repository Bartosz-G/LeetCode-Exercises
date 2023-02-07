#https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        if height is None:
            return None

        M = 0
        j = len(height)-1
        i = 0

        while i <= j:
            a = height[i]
            b = height[j]

            vol = min(a,b)*abs(j-i)
            if vol > M:
                M = vol

            if a < b:
                i += 1
            else:
                j -= 1

        return M


