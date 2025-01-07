import itertools
from typing import List
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        intnums = []
        ans = 0
        for num in nums:
            intnums.append(bin(num))

        allperms = list(itertools.permutations(intnums, 3))
        for perm in allperms:
            permval = ''.join([p[2:] for p in perm])
            # print(permval)
            val = int(''.join([p[2:] for p in perm]), 2)
            if val > ans:
                ans = val

        return ans

print(Solution().maxGoodNumber([1,2,3]))