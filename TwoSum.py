A = [11,15,17,2,20,21,-10,-7,-5,-3,-1,7,0,3]
B = [3,2,4]
C = [3,3]
D = [3,2,5,3]
E = [-10,7,19,15]

#https://leetcode.com/problems/two-sum/description/

def findSum(start,end,numssorted,targ):
    mid = start + ((end-start)//2)
    deciding = numssorted[start] + numssorted[mid]

    if mid == start:
        #Case when the length is 2
        return numssorted[start],numssorted[end]

    if deciding == targ:
        return numssorted[start], numssorted[mid]



    elif mid + 1 == end:
        # Case when the length is 3
        if numssorted[mid] + numssorted[end] == targ:
            return numssorted[mid], numssorted[end]
        else:
            return numssorted[start], numssorted[end]





    if deciding >= targ:
        return findSum(start, mid, numssorted, targ)
    else:
        return findSum(mid, end, numssorted, targ)






def findIndices(List,numbers):
    indices = []
    i = 0
    while len(indices) < len(numbers):
        if List[i] == numbers[0] or List[i] == numbers[1]:
            indices.append(i)
        i += 1
    return indices






class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #O(nlogn)
        numsSorted = sorted(nums)
        print(numsSorted)
        #O(logn)
        sumNums = findSum(0,len(nums)-1,numsSorted,target)
        #O(n)
        Indices = findIndices(nums,sumNums)
        return Indices



'''    elif mid + 1 == end:
        #Case when the length is 3
        if deciding == targ:
            return numssorted[start],numssorted[mid]
        elif numssorted[mid] + numssorted[end] == targ:
            return numssorted[mid],numssorted[end]
        else:
            return numssorted[start],numssorted[end]'''


S = Solution()
print(S.twoSum(A,9))
print(S.twoSum(B,6))
print(S.twoSum(C,6))
print(S.twoSum(D,6))
print(S.twoSum(E,9))


