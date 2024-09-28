from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        if (max(maximumHeight)) < len(maximumHeight):
            return -1

        lowerCounter = []
        heights = {}
        csum = 0 # current sum

        for i in range(len(maximumHeight)):
            height = maximumHeight[i]
            if height in heights:
                res = self.updateHeight(height, heights, lowerCounter)
                if res == -1:
                    return res
                csum += res
            else:
                heights[height] = height
                if height not in lowerCounter:
                    lowerCounter.append(height)
                csum += height

        return csum
    
    def updateHeight(self, height, heights, lowerCounter):
        # if we are encountering a height for the second time and th
        existingHeight = height
        while existingHeight > 1:
            existingHeight -= 1
            if existingHeight not in heights:
                heights[existingHeight] = existingHeight
                # print(f'updated heights: {heights}')
                return existingHeight
        return -1
            



print(Solution().maximumTotalSum([2,3,4,3]))

print(Solution().maximumTotalSum([15,10]))

print(Solution().maximumTotalSum([2,2,1]))