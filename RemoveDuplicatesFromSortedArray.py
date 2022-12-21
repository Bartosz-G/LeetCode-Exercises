#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in reversed(range(len(nums)-1)):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
        return len(nums)
