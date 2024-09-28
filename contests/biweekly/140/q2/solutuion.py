from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        heights = {}

        for i in range(len(maximumHeight)):
            height = maximumHeight[i]
            if height in heights:
                res = self.updateHeight(height, heights)
                if res == -1:
                    return res
            else:
                heights[height] = height

        return heights.values()
    
    def updateHeight(self, height, heights):
        # if we are encountering a height for the second time and th
        if height in heights:
            existingHeight = heights[height]
            while existingHeight > 0:
                existingHeight -= 1
                if existingHeight not in heights:
                    heights[existingHeight] = existingHeight
                    print(f'updated heights: {heights}')
                    return 1
            return -1
            



print(Solution().maximumTotalSum([2,3,4,3]))