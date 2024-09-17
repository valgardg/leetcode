from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 0th kid
        maxCandies = max(candies)
        return ([candy + extraCandies >= maxCandies for candy in candies])

solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))