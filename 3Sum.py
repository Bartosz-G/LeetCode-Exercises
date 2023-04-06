#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        start = 0
        end = len(nums) - 1

        output = []

        #Outer loop
        while start <= end - 1:
            sel = nums[start]
            eel = nums[end]

            #First condition
            if sel + eel < 0:

                for i,element in enumerate(list(reversed(nums[start+1:end]))):

                    # if element == nums[i-1]:
                    #     continue

                    if element + sel + eel == 0:
                        try:
                            if output[-1] == [element,sel,eel]:
                                continue
                            else:
                                output.append([element, sel, eel])
                        except IndexError:
                            output.append([element, sel, eel])
                            continue

                    if element + sel + eel < 0:
                        start = start + 1
                        break
                else:
                    start = start + 1
            else:
                for i, element in enumerate(nums[start+1:end]):

                    # if element == nums[i+1]:
                    #     continue

                    if element + sel + eel == 0:
                        try:
                            if output[-1] == [element,sel,eel]:
                                continue
                            else:
                                output.append([element, sel, eel])
                        except IndexError:
                            output.append([element, sel, eel])
                            continue

                    if element + sel + eel > 0:
                        end = end - 1
                        break
                else:
                    start = start + 1

        return output











a1 = [-1,0,1,2,-1,-4]
a2 = [0,1,1]
a3 = [0,0,0]
a4 = [0,0,0,0]
a5 = [-1,0,1,2,-1,-4,-2,-3,3,0,4] #Expected: [-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]


S = Solution()

print(S.threeSum(a1))
print(S.threeSum(a2))
print(S.threeSum(a3))
print(S.threeSum(a4))
print(S.threeSum(a5))

