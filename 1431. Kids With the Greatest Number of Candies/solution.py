from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 0th kid
        return ([candy + extraCandies >= max(candies) for candy in candies])

solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))