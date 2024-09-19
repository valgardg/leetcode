from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxAlt = 0
        maxAltPoint = 0
        for i in range(len(gain)):
            alt += gain[i]
            print(f'current altitude: {alt}, i: {i}, maxAlt: {maxAlt}')
            if alt > maxAlt:
                maxAlt = alt
                maxAltPoint = i
        
        print(maxAltPoint)
        return maxAlt

Solution().largestAltitude([-5,1,5,0,-7])