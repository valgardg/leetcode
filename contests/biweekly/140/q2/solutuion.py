from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        if (max(maximumHeight)) < len(maximumHeight):
            return -1

        heightl = []
        csum = 0 # current sum
        heights = {}

        for i in range(len(maximumHeight)):
            height = maximumHeight[i]
            # print(f'inspecting height {height}, i: {i}, maxheight: {maximumHeight}')
            if height not in heights:
                # print(f'height not in heights: {height}')
                # if we have discovered a new digit, we want to leave as much information in case another one comes along
                lowerterm = height - 1
                while lowerterm in heights:
                    lowerterm = heights[lowerterm]
                heights[height] = lowerterm
                csum += height
                heightl.append(height)
                # print(f'    set heights[{height}] = {height}')
                # print(f'    set heights[{height-1}] = {lowerterm}')
                # print(f'    added {height} to csum {csum}')
                # print(f'    appended {height} to heightl: {heightl}')
            else:
                # print(f'height found in heights: {height}')
                lowerterm = heights[height]
                while lowerterm in heights:
                    lowerterm = heights[lowerterm]
                csum += lowerterm
                # print(f'final lowerterm: {lowerterm}')
                if lowerterm == 0:
                    return -1
                heightl.append(lowerterm)
                heights[height] = lowerterm
                heights[lowerterm] = lowerterm - 1
                

        print(f'list at the end: {heightl}')
        return csum


print(Solution().maximumTotalSum([2,3,4,3]))
print(Solution().maximumTotalSum([5,5,4,5]))
print(Solution().maximumTotalSum([15,10]))
print(Solution().maximumTotalSum([2,2,1]))
print(Solution().maximumTotalSum([1, 10, 5, 1]))
print(Solution().maximumTotalSum([7,4,5,4,7,2,6]))