from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        canPlace = False
        planted = 0
        if(len(flowerbed) == 1):
            if(n > 1):
                return False
            if(n == 0):
                return True
            return not (flowerbed[0])
        for i in range(len(flowerbed)):
            if(i > 0 and i<len(flowerbed)-1):
                if flowerbed[i-1] != 1 and flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    planted += 1
            elif i == 0:
                if flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    planted +=1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] != 1 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    planted +=1
        return (planted >= n)
                

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1,0,0], 2))
print(solution.canPlaceFlowers([0], 1))
print(solution.canPlaceFlowers([1], 0))