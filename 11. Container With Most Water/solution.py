from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        mp = len(height) - 1
        maxArea = 0
        while lp != mp:
            # width * height
            width = mp - lp
            lower = min(height[lp], height[mp])
            area = width * lower
            # print(area)
            if area > maxArea:
                maxArea = area
            if height[lp] < height[mp]:
                lp += 1
            else:
                mp -=1
        print(maxArea)
        return maxArea
    
Solution().maxArea([1,8,6,2,5,4,8,3,7])