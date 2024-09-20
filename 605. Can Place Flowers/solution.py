from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            if n == 0:
                return True
            if n == 1 and flowerbed[0] == 0:
                return True
            return False
        for i in range(len(flowerbed)):
            if i > 0 and i != len(flowerbed)-1:
                if flowerbed[i-1] != 1 and flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    count+=1
                    flowerbed[i] = 1
            elif i == 0:
                if flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    count+=1
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] != 1 and flowerbed[i-1] != 1:
                    count+=1
                    flowerbed[i] = 1
        return count >= n

print(Solution().canPlaceFlowers([0,0,1,0,0], 1))
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))