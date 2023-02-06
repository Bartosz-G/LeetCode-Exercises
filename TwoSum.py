#https://leetcode.com/problems/two-sum/



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        j = len(nums)

        #O(n)
        nums = [(nums[i],i) for i in range(j)]

        #O(nlogn)
        numsSorted = sorted(nums,key=lambda x: x[0])

        i = 0
        j = len(nums) - 1


        #O(n)
        while i < j:
            val = numsSorted[i][0] + numsSorted[j][0]

            if val == target:
                return [numsSorted[i][1],numsSorted[j][1]]

            if val > target:
                j -= 1

            if val < target:
                i += 1

