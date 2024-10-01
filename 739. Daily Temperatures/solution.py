from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        for i in range(temperatures):
            temp = temperatures[i]
            count = 0
            ii = i + 1
            while ii < len(temperatures) and temp < temperatures[ii]:
                count += 1
                ii += 1
            

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))