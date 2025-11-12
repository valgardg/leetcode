from typing import List
import sys


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dist = sys.maxsize
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and j != k and i != k:
                        if (
                            nums[i] == nums[j]
                            and nums[j] == nums[k]
                            and nums[i] == nums[k]
                        ):
                            test_min = abs(i - j) + abs(j - k) + abs(k - i)
                            if test_min < min_dist:
                                print(f"found good tuple ({i}, {j}, {k})")
                                min_dist = test_min
        if min_dist == sys.maxsize:
            return -1
        return min_dist


print(Solution().minimumDistance([1, 2, 1, 1, 3]))
print(Solution().minimumDistance([1, 1, 2, 3, 2, 1, 2]))
print(Solution().minimumDistance([1]))
