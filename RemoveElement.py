#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = len(nums)-1
        for i in reversed(nums):
            if i == val:
                del nums[j]
            j -=1
        return len(nums)
